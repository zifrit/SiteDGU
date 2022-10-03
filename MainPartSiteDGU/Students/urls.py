from django.urls import path, include
from .views import *

urlpatterns = [
    path('regist-student/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_system, name='logout'),
    path('main/', Main.as_view(), name='main'),
]