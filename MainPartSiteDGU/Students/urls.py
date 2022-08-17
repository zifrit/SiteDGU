from django.urls import path, include
from .views import *

urlpatterns = [
    path('regist-student/', RegisterS.as_view(), name='home'),
]