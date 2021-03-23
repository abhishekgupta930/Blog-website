from django.urls import path
from . import views


urlpatterns = [
        #Leave as empty string for base url
        path('', views.home, name="home"),
	path('home', views.home, name="home"),
        path('post/<slug>', views.detailView, name="post-detail"),
        path('home/signUp', views.signUp, name="signUp"),



]