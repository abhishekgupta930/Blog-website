from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from .models import Post

# Create your views here.
# ef home(request):
#    return render(request, 'home.html', context)
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
