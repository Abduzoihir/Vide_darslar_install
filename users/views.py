from django.shortcuts import *
from .form import *
from django.urls import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required

def signup(request):
    sign=SignUpForm()
    if request.method == 'POST':
        sign=SignUpForm(request.POST, request.FILES)       
        if sign.is_valid():
            sign.save()
            return redirect(reverse('video_dars_app:home'))
        else:
            return render(request, "auth/signup.html", {'form':sign})   
    return render(request, "auth/signup.html", {'form':sign})

def login_required_decorator(func):
    return login_required(func, login_url='login')

@login_required_decorator
def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    errors=""
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('video_dars_app:home')
        else:
            errors+="Login yoki parol xato. Iltimos qaytadan kiriting!"
            return render(request, 'auth/login.html', {'errors':errors})
    return render(request, 'auth/login.html')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect(reverse('video_dars_app:home'))