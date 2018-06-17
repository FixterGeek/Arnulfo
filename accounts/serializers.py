from django.contrib.auth.models import User 
from .models import Profile
from rest_framework import serializers



class BasicUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id', 'email', 'is_staff','is_superuser', 'first_name']


class ProfileSerializer(serializers.ModelSerializer):
	user = BasicUserSerializer(many=False, read_only=True)
	class Meta:
		model = Profile
		fields = '__all__'


class BasicProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = ['admin', 'ganado', 'vacunas', 'alimentos', 'cerdos', 'aves']#all sections

class UserSerializer(serializers.ModelSerializer):
	profile=BasicProfileSerializer(many=False, read_only=False);
	class Meta:
		model = User
		fields = ['username', 'id', 'email', 'is_staff','is_superuser', 'profile', 'password','is_active', 'first_name']
	def create(self, validated_data):
		
		profile_data = validated_data.pop('profile')
		print(validated_data)
		password = validated_data.pop('password')
		email = validated_data['email']
		username = validated_data['username']
		#user = User(email=email, username=username)
		user = User.objects.create(**validated_data)
		profile = Profile.objects.create(user=user, **profile_data)
		user.set_password(password)
		user.save()
		print(user.id)
		#user = User.objects.create(**validated_data)
		#profile = Profile(user=user)
		#profile.save()
		return user

	def update(self, instance, validated_data):
		print(validated_data)
		print(instance)
		if(validated_data['password']):
			password = validated_data['password']
			instance.set_password(password)
			instance.save()


		
		instance.email = validated_data.get('email', instance.email)
		
		instance.first_name = validated_data.get('first_name', instance.first_name)
		profile_data = validated_data.pop('profile')	
		profile = instance.profile
		profile.admin = profile_data.get('admin',profile.admin)
		profile.ganado = profile_data.get('ganado',profile.ganado)
		profile.vacunas = profile_data.get('vacunas',profile.vacunas)
		profile.alimentos = profile_data.get('alimentos',profile.alimentos)
		profile.cerdos = profile_data.get('cerdos',profile.cerdos)
		profile.aves = profile_data.get('aves',profile.aves)
		profile.save()
		instance.save()
		return instance
		







