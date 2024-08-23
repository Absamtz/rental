from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserRegisterForm
from .models import Availability, Booking, Payment, Property, Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Index view
def index(request):
    return render(request, 'index.html', {'title': 'index'})

# Register view
def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            # Save the user
            user = form.save()
            
            # Authenticate the user
            user = authenticate(username=username, password=password1)
            if user is not None:
                signin_view(request, user)
                messages.success(request, "Account created and logged in successfully!")
                return redirect('account:login')  # Redirect to login page or wherever you want
            else:
                messages.error(request, "---------------")
                return redirect('account:signup')
            
        else:
            messages.error(request, 'Form is not valid.')
            return redirect('account:signup')
    else:
        form = UserRegisterForm()
        context = {
            'signUp_form': form
        }
        return render(request, 'signup.html', context)

# Signin view
def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('acccount:signin')  # Redirect to a valid view
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Please fill out both fields')
    
    return render(request, 'accounts/signin.html')

# Home view
def home_view(request):
    return render(request, 'index.html')

# Dashboard view
@login_required
def dashboard_view(request):
    availabilities = Availability.objects.all()
    bookings = Booking.objects.all()
    payments = Payment.objects.all()
    properties = Property.objects.all()
    reviews = Review.objects.all()
    
    context = {
        'availabilities': availabilities,
        'bookings': bookings,
        'payments': payments,
        'properties': properties,
        'reviews': reviews,
    }
    
    return render(request, 'account/dashboard.html', context)

# Logout view

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

# Booking view
def booking_view(request):
    template_name = 'booking_and_payment.html'
    context = {}
    return render(request, template_name, context)
