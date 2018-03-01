from django.conf.urls import url, include
from .views import LoginView, LogoutView, UserView
from rest_framework.authtoken import views
from rest_framework import routers
from .views import UsersViewSet, ProfileViewSet


app_name="accounts"

router = routers.DefaultRouter()
router.register('users', UsersViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns=[
	url('^', include(router.urls)),
	url(r'^login/$',LoginView.as_view()),
	url(r'^logout/$',LogoutView.as_view()),
	url(r'^token-auth/', views.obtain_auth_token),
	url(r'^me/',UserView.as_view())
]