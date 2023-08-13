from django.shortcuts import render, redirect
from django.views import View
from .forms import KhojForm
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Khoj
from django.contrib import messages

def welcome(request):
    """ Welcome to user """
    return render(request, 'welcome.html')

def user_registration(request):
    """ Register a new user account. """

    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            messages.success(request, 'Congratulation!! You have become a Author. Please Login.')
            registration_form.save()
            return redirect('login')
    else:    
        registration_form = RegistrationForm()

    context = {'registration_form':registration_form}    
    return render(request, 'registration.html', context)

def user_login(request):
    """  Authenticate a user and log them in. """

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
    """ Log out the currently authenticated user. """

    logout(request)
    return redirect('/')  




class KhojView(LoginRequiredMixin, View):
    """
    This class-based view, `KhojView`, provides functionality for searching an input list of integers for a specific value.

    When accessed via a GET request, the view renders a form (`KhojForm`) to input a list of integers and a search value.

    Upon receiving a POST request with valid form data:
    - It extracts the input values and the search value from the form.
    - It processes the input values, checking if the search value is present in the list.
    - If the search value is found, `khoj_result` is set to True; otherwise, it's set to False.
    - The input values are then sorted in descending order and stored as a string in the database along with the user ID.
    - Finally, the rendered HTML page is updated with the search result (`khoj_result`).

    """

    def get(self, request, *args, **kwargs):
        khoj_form = KhojForm
        context = {'khoj_form':khoj_form}
        return render(request, 'khoj.html', context)
    
    def post(self, request, *args, **kwargs):
        khoj_form = KhojForm(request.POST)
        if khoj_form.is_valid():
            input_values = khoj_form.cleaned_data['input_values']
            search_value = khoj_form.cleaned_data['search_value']

            list_of_values = []
            for i in input_values.split(','):
                try:
                    integer = int(i)
                    list_of_values.append(integer)
                    if int(search_value) in list_of_values:
                        khoj_result = True
                    else:
                        khoj_result = False
                except ValueError:
                    messages.error(request, "Please enter a valid integer.")
                    return redirect('khoj')

            desorted_input_values = sorted(list_of_values, reverse=True) # sorted 'list_of_values' in descending order
            sorted_string_input_values = ", ".join([str(num) for num in desorted_input_values]) # desorted_input_values >>> type:list  to type:str >>> sorted_string_input_values
            Khoj(user_id=request.user, input_values=sorted_string_input_values).save() # 'sorted_string_input_values' store in database as string

        context = {'khoj_result': khoj_result}    
        return render(request, 'khoj.html', context)