from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .resources import UserResource, ProfileResource
from import_export.admin import ImportExportModelAdmin


# Register your models here.




class AdminProfile(admin.StackedInline):
	model = Profile	

class AdminProfileExIm(ImportExportModelAdmin):
	resource_class=ProfileResource

class AdminUser(ImportExportModelAdmin):
	resource_class = UserResource
	inlines = (AdminProfile,)

admin.site.register(Profile, AdminProfileExIm)
admin.site.unregister(User)
admin.site.register(User, AdminUser)




