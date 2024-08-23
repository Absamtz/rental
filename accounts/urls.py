from django.urls import path
from . import views
from .views import  dashboard_view,logout_view, booking_view

app_name ='account'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),  
    path('login/', views.signin_view, name='login'), 
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('bookings/', booking_view, name ='bookings')
]    
