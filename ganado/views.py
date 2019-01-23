from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EditAnimalSerializer, AnimalSerializer, CorralSerializer, LoteSerializer, AlimentoSerializer, BasicAnimalSerializer, BasicLoteSerializer, PesoSerializer, BasicPesoSerializer, RazaSerializer, FacturaSerializer, SaleNoteSerializer, FierroOSerializer, FierroNSerializer, JustAnimalSerializer
from .models import Animal, Lote, GastoAnimal, Corral, Peso, Raza, Factura, SaleNote, FierroO, FierroN
from .pagination import AnimalPagination, LotePagination, FacturaPagination, SaleNotePagination ,AlimentoPagination
from django.db.models import Q, Avg, Count, Min,Max,  Sum
from django.db.models import FloatField, CharField, DecimalField
from datetime import datetime, timedelta, date
from django.core import serializers as dserializers

class FierroOViewSet(viewsets.ModelViewSet):
    queryset = FierroO.objects.all()
    serializer_class = FierroOSerializer

class FierroNViewSet(viewsets.ModelViewSet):
    queryset = FierroN.objects.all()
    serializer_class = FierroNSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    pagination_class = FacturaPagination

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        query_list = super(FacturaViewSet, self).get_queryset()
        if query:
            query_list = query_list.filter(
                Q(factura__icontains=query)
            ).distinct()
        return query_list


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    #queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    pagination_class = AnimalPagination

    def get_serializer_class(self):
        if self.action == 'update':
            return EditAnimalSerializer
        if self.action == 'partial_update':
            return EditAnimalSerializer
        return AnimalSerializer

    def get_queryset(self, *args, **kwargs):



        query = self.request.GET.get("q")
        lote_query = self.request.GET.get("lote")
        status = self.request.GET.get("s")
        queryset_list = super(AnimalViewSet,self).get_queryset()
        # if self.action == 'list':
        # 	queryset_list = queryset_list.filter(status=True)
        if query:
            queryset_list = queryset_list.filter(
                Q(arete_rancho__icontains=query)|
                Q(arete_siniga__icontains=query)|
                Q(owner__icontains=query)
                ).distinct()
        if lote_query:
            queryset_list = queryset_list.filter(Q(lote__name__iexact=lote_query))

        if status and status == 'false':
            queryset_list = queryset_list.filter(status=False)
        if self.action=='list' and (status != 'false' or not status):
            queryset_list = queryset_list.filter(status=True)
        return queryset_list

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    pagination_class = LotePagination


    def get_serializer_class(self):
        if self.action == 'list':
            return LoteSerializer
        if self.action == 'retrieve':
            return LoteSerializer
        return BasicLoteSerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")


        queryset_list = super(LoteViewSet,self).get_queryset()
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
                ).distinct()


            #lista.append(i)
        #

        return queryset_list

class CorralViewSet(viewsets.ModelViewSet):
    queryset = Corral.objects.all()
    serializer_class = CorralSerializer

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = GastoAnimal.objects.all()
    serializer_class = AlimentoSerializer
    pagination_class = AlimentoPagination

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        d1 = self.request.GET.get("d1")
        d2 = self.request.GET.get("d2")
        text = self.request.GET.get("text")
        lote = self.request.GET.get("lote")
        queryset_list = super(AlimentoViewSet, self).get_queryset()
        if lote:
            queryset_list = queryset_list.filter(animal__lote__name__iexact=lote)
        if query:
            queryset_list = queryset_list.filter(tipo=query)
        if d1 and d2:
            queryset_list = queryset_list.filter(created__range=[d1, d2])
        if text:
            queryset_list = queryset_list.filter(
                Q(animal__arete_rancho__icontains=text))

        return queryset_list

class PesoViewSet(viewsets.ModelViewSet):
    queryset = Peso.objects.all()
    #serializer_class = PesoSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PesoSerializer
        if self.action == 'retrieve':
            return PesoSerializer
        return BasicPesoSerializer





class RazasViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer

class SaleNoteViewSet(viewsets.ModelViewSet):
    queryset = SaleNote.objects.all()
    serializer_class = SaleNoteSerializer
    pagination_class = SaleNotePagination


class ResumenView(APIView):
    def get(self, request):

        #Básicos
        aretes = Animal.objects.all().filter(status=True)
        aretes_activos = aretes.aggregate(valor_inicial=Sum('costo_inicial'), count=Count('id'), gastos_cash=Sum('aliments__costo'))
        aretes_inactivos = len(Animal.objects.all().filter(status=False))
        ##mayores a 350kg
        proximos = Animal.objects.all().filter(pesadas__peso__gte=350, status=True).distinct()
        cuenta_proximos = len(proximos)
        proximos = AnimalSerializer(proximos, many=True)
        #gastos
        gastos = GastoAnimal.objects.all().filter(animal__status=True ).aggregate(suma_gastos=Sum('costo'))
        gastos_alimento = GastoAnimal.objects.all().filter(animal__status=True, tipo='Alimento').aggregate(costo_alimento=Sum('costo'), kg_alimento=Sum('cantidad'))
        gastos_vacuna = GastoAnimal.objects.all().filter(animal__status=True, tipo='Vacuna').aggregate(suma_gastos_vacuna=Sum('costo'))

        #gdp y esas formulas locas
        conversionPromedio = 0
        gdpPromedio = 0
        cdpPromediokg = 0
        cdpPromedioCash = 0
        # (ultima_pesada - peso_inicial)/(fecha_ultima_pesada - fecha_inicial) y luego promediar el de todos los aretes activos
        for a in aretes:
            a_alimentos_kg = 1
            a_alimentos_cash = 1
            a_vacunas_cash = 1
            if len(a.aliments.all()) >= 1:
                a_alimentos_kg = 0
                a_alimentos_cash = 0
                a_vacunas_cash = 0
                for ga in a.aliments.all():

                    if ga.tipo == 'Alimento':
                        a_alimentos_kg += ga.cantidad
                        a_alimentos_cash += ga.costo
                    if ga.tipo == 'Vacuna':
                        a_vacunas_cash += ga.costo
            if a.last_pesada() != None:
                diff_days=(a.last_pesada().created-a.fecha_entrada.date()).days
                if diff_days!= 0:
                    gdp = (a.last_pesada().peso-a.peso_entrada)/diff_days
                gdpPromedio += gdp
                #consumo diario promedio hasta la ultima pesada
                cdp = (a_alimentos_kg/diff_days)
                cdpCash = (a_alimentos_cash/diff_days)
                cdpPromedioCash += cdpCash
                cdpPromediokg += cdp
                #conversion por animal
                conversion = (a.last_pesada().peso-a.peso_entrada)/a_alimentos_kg
                conversionPromedio += conversion
        gdpPromedio = gdpPromedio/len(aretes)
        conversionPromedio = conversionPromedio/len(aretes)
        #let conversion = ((a.lastPesada()-a.peso_entrada)/a.alimentsQuantityTotal)



        data = {
            "aretes_activos":aretes_activos,
            "aretes_inactivos":aretes_inactivos,
            "cuenta_proximos":cuenta_proximos,
            "gdpPromedio":gdpPromedio,
            "conversionPromedio":conversionPromedio,
            "cdpPromediokg":cdpPromediokg,
            "cdpPromedioCash":cdpPromedioCash,
            "gastos":gastos,
            "gastos_alimento":gastos_alimento,
            "gastos_vacuna":gastos_vacuna,
            "proximos":proximos.data,


        }
        return Response(data)


#second try to do reportes chingones
class AggregatedSerializer(serializers.ModelSerializer):
    peso_final = serializers.DecimalField(max_digits=20, decimal_places=4)
    costo_alimentos = serializers.DecimalField(max_digits=20, decimal_places=4)
    costo_vacunas = serializers.DecimalField(max_digits=20, decimal_places=4)
    costos_total = serializers.DecimalField(max_digits=20, decimal_places=4)
    kg_alimento = serializers.DecimalField(max_digits=20, decimal_places=4)
    class Meta:
        model = Animal
        fields = '__all__'


class ReportesView(APIView):
    def get(self, request):
        #Getting the aretes, might add filters...
        vacas = Animal.objects.all()

        status = self.request.GET.get("status")
        d1 = self.request.GET.get("d1")
        d2 = self.request.GET.get("d2")
        aretes = self.request.GET.get("aretes")
        lote = self.request.GET.get("lote")
        
        if lote:
            vacas = vacas.filter(lote__name__iexact=lote)
        if status:
            vacas = vacas.filter(status=status)
        if d1 and d2:
            vacas = vacas.filter(created__range=[d1, d2])
        #if aretes:
         #   vacas = vacas.filter(
          #      Q(animal__arete_rancho__icontains=text))        


        #pesadas
        vacas = vacas.annotate(
            peso_final=(Max('pesadas__peso', output_field=DecimalField(max_digits=20, decimal_places=4))),
            costo_alimentos=(Sum('aliments__costo', output_field=DecimalField(max_digits=20, decimal_places=4), filter=Q(aliments__tipo='Alimento'))),
            kg_alimento=(Sum('aliments__cantidad', output_field=DecimalField(max_digits=20, decimal_places=4), filter=Q(aliments__tipo='Alimento'))),
            costo_vacunas=(Sum('aliments__costo', output_field=DecimalField(max_digits=20, decimal_places=4), filter=Q(aliments__tipo='Vacuna'))),
            costos_total=(Sum('aliments__costo', output_field=DecimalField(max_digits=20, decimal_places=4))),

            )
        for v in vacas:
            if(v.last_pesada()) and v.aliments:
                v.days_in_ranch = v.last_pesada().created - v.fecha_entrada.date()
                v.kg_hechos = v.peso_final - v.peso_entrada
                v.conversion = v.kg_hechos/v.kg_alimento
                v.rendimiento = v.kg_alimento/v.kg_hechos
                v.ganacia_diaria_promedio = 0
                v.costo_por_dia = 0
                #GDP y CDP
                if(v.days_in_ranch.days>0):
                    v.ganacia_diaria_promedio = v.kg_hechos/v.days_in_ranch.days
                    v.costo_por_dia = v.costos_total/v.days_in_ranch.days
                
                v.save()



        # selected vacas to show

        # conversion = kghechos/comida consumida)
        # rendimienti = comida consumida/kg hechos)

        # All global values
        #alimento = GastoAnimal.objects.all().filter(tipo='Alimento').aggregate(costo=Sum('costo'), kg=Sum('cantidad'))
        #vacunas = GastoAnimal.objects.all().filter(tipo='Vacuna').aggregate(costo=Sum('costo'))
        globals = vacas.aggregate(
                                Sum('peso_entrada', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('peso_entrada', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Sum('peso_final', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('peso_final', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('days_in_ranch', output_field=CharField(max_length=100)),
                                Sum('kg_hechos', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('kg_hechos', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('conversion', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('rendimiento', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Sum('kg_alimento', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('kg_alimento', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Sum('costo_alimentos', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('costo_alimentos', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Sum('costo_vacunas', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('costo_vacunas', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('costos_total', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Sum('costos_total', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('costo_por_dia', output_field=DecimalField(max_digits=20, decimal_places=4)),
                                Avg('ganacia_diaria_promedio', output_field=DecimalField(max_digits=20, decimal_places=4)))
        #pesos['kg_hechos'] = pesos['peso_final__sum'] - pesos['peso_entrada__sum']
        #conversion = pesos.kg_hechos/alimento['kg']
        #rendimiento = alimento['kg'] / pesos['kg_hechos']

        vacas_list = AggregatedSerializer(vacas, many=True)



        data = {
            "vacas":vacas_list.data,
            "globals": globals,
            #"alimento": alimento,
            #"vacunas": vacunas,
            #"conversion":conversion,
            #"rendimiento":rendimiento

        }
        return Response(data)







