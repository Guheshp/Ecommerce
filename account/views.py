from django.shortcuts import render, redirect

from django.contrib import messages


# Create your views here.

def register(request):
    
    return render(request,'acc/register.html')

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