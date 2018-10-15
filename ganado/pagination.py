from rest_framework.pagination import PageNumberPagination


class AnimalPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000

class LotePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class FacturaPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class SaleNotePagination(PageNumberPagination):
	page_size = 20
	page_size_query_param = 'page_size'
	max_page_size = 1000


class AlimentoPagination(PageNumberPagination):
    page_size=24
    page_size_query_param='page_size'
    max_page_size = 1000