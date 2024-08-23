from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import House
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def homePage(request):
    get_all_houses = House.objects.all()
    return render (request, template_name='index.html', context={'houses':get_all_houses})


@login_required
def dashboard_view(request):
    return render(request, 'accoutns/dashboard.html')


def signin(request):
    return render(request, 'signin.html')

def signup(request):
    print('-----------------')
    return render(request, 'signup.html')


def make_order(request, house_id):
    house = get_object_or_404(House, id=house_id)
    context = {
        'house': house
    }
    return render(request, 'make_order.html', context)

# views.py

@login_required
def confirm_order(request, house_id):
    # Ensure House model is correctly referenced
    house = get_object_or_404(House, id=house_id)
    
    # Your logic to handle the order confirmation
    return render(request, 'frontEnd/confirm_order.html', {'house': house})


def order_success(request, house_id):
    house = get_object_or_404(House, id=house_id)
    # Your logic here
    return render(request, 'order_success.html', {'house': house})


def logout_view(request):
    logout(request)
    return redirect('login')
