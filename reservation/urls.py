from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
        path('login/', views.login, name="login"),
        path('registration/', views.registration, name="registration"),
]