from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('about/', about_view, name='about'),
    path('delete/<int:pk>/', delete_url_view, name='delete_url'),
    path('<str:code>/', redirect_view, name='redirect'),
]

