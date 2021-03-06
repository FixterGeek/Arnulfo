from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from django.contrib.auth import authenticate, login, logout
from rest_framework import status, views, viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, BasicProfileSerializer


from django.contrib.auth.models import User
from .models import Profile

# Create your views here.


class LoginView(views.APIView):
	@method_decorator(csrf_protect)
	def post(self, request):
		user = authenticate(
				username=request.data.get('username'),
				password=request.data.get('password'))
		if user is None or not user.is_active:
			return Response({
				'status': 'Unauthorized',
				'message': 'Username or password incorrect'
				}, status=status.HTTP_401_UNAUTHORIZED)

		login(request, user)
		return Response(UserSerializer(user).data)


class LogoutView(views.APIView):
	def get(self, request):
		logout(request)
		return Response({}, status=status.HTTP_204_NO_CONTENT)

class UserView(views.APIView):
	def get(self, request):
		user = request.user
		return Response(UserSerializer(user).data)

class UsersViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = BasicProfileSerializer

	







