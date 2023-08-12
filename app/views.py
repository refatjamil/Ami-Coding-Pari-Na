from django.shortcuts import render, redirect
from django.views import View
from .forms import KhojForm
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


def welcome(request):
    return render(request, 'welcome.html')

def user_registration(request):
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            messages.success(request, 'Congratulation!! You have become a Author. Please Login.')
            registration_form.save()
    else:    
        registration_form = RegistrationForm()

    context = {'registration_form':registration_form}    
    return render(request, 'registration.html', context)

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            login_form = LoginForm(request=request, data=request.POST)
            if login_form.is_valid():
                uname = login_form.cleaned_data['username']
                upass = login_form.cleaned_data['password']
                user = authenticate(username= uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !')
                    return redirect('khoj')
        else:            
            login_form = LoginForm()

        context = {'login_form':login_form}
        return render(request, 'login.html', context)
    
    else:
        return redirect('/')
    
def user_logout(request):
    logout(request)
    return redirect('/')  

def khoj_result(input_values, search_value):
    list_of_values = [int(i) for i in input_values.split(',')]

    if int(search_value) in list_of_values:
        return True
    else:
        return False

class KhojView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        khoj_form = KhojForm
        context = {'khoj_form':khoj_form}
        return render(request, 'khoj.html', context)
    
    def post(self, request, *args, **kwargs):
        khoj_form = KhojForm(request.POST)
        if khoj_form.is_valid():
            input_values = khoj_form.cleaned_data['input_values']
            search_value = khoj_form.cleaned_data['search_value']

        context = {'khoj_result': khoj_result(input_values, search_value)}    
        return render(request, 'khoj.html', context)