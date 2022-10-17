from django.urls import path, include
from .views import *

urlpatterns = [
    path('base_register/', BaseRegister.as_view(), name='base_register'),
    path('advanced_register/', AdvancedRegisterStudent.as_view(), name='advanced_register'),
    path('full_register/', FullRegisterStudent.as_view(), name='full_register'),
    path('login/', Login.as_view(), name='login'),
    path('reg_user/', Register.as_view(), name='register'),
    path('logout/', logout_system, name='logout'),
    path('list_students/', ListStudent.as_view(), name='list_students'),
    path('create_events/', CreateEvents.as_view(), name='create_events'),
    path('list_events/', ListEvents.as_view(), name='list_events'),
    path('detail_events/<int:pk>/', DetailEvent.as_view(), name='detail_events'),
    path('detail_student/<int:pk>/', DetailStudent.as_view(), name='detail_student'),
    path('type_reg_student/', TypeRegisterStudent.as_view(), name='type_reg_student'),
]