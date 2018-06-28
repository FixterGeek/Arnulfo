from import_export import resources
from .models import Profile
from django.contrib.auth.models import User



class UserResource(resources.ModelResource):
    class Meta:
        model = User

class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile