from django.shortcuts import render, redirect
from . forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import (authenticate,
                                login as auth_login,
                                logout as auth_logout,
                                update_session_auth_hash,
                                )

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Registration Completed!')
            return redirect('login') 
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(request,'acc/register.html', context)

def login(request):  
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("Email:", email)  # Debug output
        print("Password:", password)  # Debug output

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other desired page
            return redirect('success_url')
        else:
            # Display an error message if authentication fails
            messages.error(request, 'Invalid email or password.')
            print("Authentication failed")  # Debug output
 

    return render(request,'acc/login.html')

def logout(request):  
    return 