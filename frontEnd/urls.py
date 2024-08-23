
from django.urls import path
from . import views
from .views import  dashboard_view

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('make_order/<int:house_id>/', views.make_order, name='make_order'),
    path('confirm_order/<int:house_id>/', views.confirm_order, name='confirm_order'), 
    path('order_success/', views.order_success, name='order_success'),
        path('dashboard/', dashboard_view, name='dashboard'),

]
