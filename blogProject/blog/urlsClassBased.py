from django.urls import path

urlpatterns = [
        #Leave as empty string for base url
	path('', HomeView.as_view(), name="home"),

]