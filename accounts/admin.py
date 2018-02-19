from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.




class AdminProfile(admin.StackedInline):
	model = Profile

class AdminUser(UserAdmin):
	inlines = (AdminProfile,)

#admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, AdminUser)



