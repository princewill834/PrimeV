from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .forms import RegistrationForm, LoginForm
# Create your views here.

def register(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    form = RegistrationForm()
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['password1']
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('customer_dashboard')

    context ={'form':form}
    return render(request,'registration/registration.html', context)

def loginView(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    form = LoginForm()
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['password']
            user = authenticate(email=email, password=raw_password)
            if user:
                login(request, user)
                return redirect('customer_dashboard')

    context ={'form':form}
    return render(request,'registration/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('index')
