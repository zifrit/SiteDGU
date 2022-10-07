from django.urls import path, include
from .views import *

urlpatterns = [
    path('base_register/', BaseRegister.as_view(), name='base_register'),
    path('advanced_register/', AdvancedRegisterStudent.as_view(), name='advanced_register'),
    path('full_register/', FullRegisterStudent.as_view(), name='full_register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_system, name='logout'),
    path('main/', Main.as_view(), name='main'),
    path('detail_student/<int:pk>/', Test.as_view(), name='detail_student'),
    path('type_reg_student/', TypeRegisterStudent.as_view(), name='type_reg_student'),
]