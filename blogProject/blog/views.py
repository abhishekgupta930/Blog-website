from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Post

# Create your views here.
# ef home(request):
#    return render(request, 'home.html', context)
def home(request):
        print("In Home")
        posts = Post.objects.all()
        context = {'posts':posts}
        return render(request, 'home.html', context)
        
def detailView(request, slug):
        print("In detail view ")
        post = Post.objects.filter(slug=slug).first()

        context = {'post':post}
        return render(request, 'detail.html', context)

def signUp(request):
        print(request.body)
        if request.method == 'POST':

                username=request.POST['username']
                fname=request.POST['firstname']
                email=request.POST['email']
                lname=request.POST['lastname']
                pass1=request.POST['password1']
                pass2=request.POST['password2']

                print("username: ", username)
                print("email: ", email)

                print("firstname: ", fname)
                print("lastname:  ", lname)
                print("password1: ", pass1)
                print("password2: ", pass2)


        # Create New User 
                newUser = User.objects.create_user(username, email, pass1)
                newUser.first
                newUser.save()
                messages.success(request, "Your message has been successfully sent")


                return redirect("home")
        else:
                return HttpResponse("Error: Not Found")
        

