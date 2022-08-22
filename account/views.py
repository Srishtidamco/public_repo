from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import UserRegistraionForm , UserLoginForm
# Create your views here.

def register(request):
    context={}
    if request.POST:
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form']=form

    else:
        form = UserRegistraionForm()
        context['register_form']=form 
    return render(request,"account/register.html",context)

def home_view(request):
    return render(request,"account/dashboard.html")
    
def login_view(request):
    context={}
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
        else:
            context['login_form'] = form
    else:
        form = UserLoginForm()
        context['login_form'] = form
    return render(request,"account/login.html",context)

def logout_view(request):
    logout(request)
    return redirect('login')


