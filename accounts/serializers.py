from django.contrib.auth.models import User 
from .models import Profile
from rest_framework import serializers



class BasicUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id', 'email', 'is_staff','is_superuser']


class ProfileSerializer(serializers.ModelSerializer):
	user = BasicUserSerializer(many=False, read_only=True)
	class Meta:
		model = Profile
		fields = '__all__'


class BasicProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
	profile=BasicProfileSerializer(many=False, read_only=True);
	class Meta:
		model = User
		fields = ['username', 'id', 'email', 'is_staff','is_superuser', 'profile', 'password']
	def create(self, validated_data):
		
		#profile_data = validated_data.pop('profile')
		print(validated_data)
		password = validated_data['password']
		email = validated_data['email']
		username = validated_data['username']
		user = User(email=email, username=username)
		user.set_password(password)
		user.save()
		print(user.id)
		#user = User.objects.create(**validated_data)
		#profile = Profile(user=user)
		#profile.save()
		return user

	def update(self, instance, validated_data):
		print(validated_data)
		if(validated_data['password']):
			password = validated_data['password']
			instance.set_password(password)
			instance.save()
		return instance






