from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth import get_user_model  

User = get_user_model()  

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')

        user = User.objects.create_user(email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        login(request, user)
        return redirect('admin_dashboard')

    return render(request, 'authentication/register.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('admin_dashboard') 
            else:
                messages.error(request, "Invalid password. Please try again.")
                return redirect('login')

        except User.DoesNotExist:
            messages.error(request, "Email not registered. Please check the email or register.")
            return redirect('login')

    return render(request, 'authentication/login.html')



