from django.urls import path, include
from .views import *

urlpatterns = [
    path('regist-student', index, name='home'),
]