from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import *

urlpatterns = [
    path('list_students/', ListStudents.as_view(), name='api_list_students'),
    path('test/', test.as_view(), name='api_list_students'),
    path('student/<int:pk>', DitailStudents.as_view(), name='api_ditail_students'),
    path('login/', MyTokenObtainView.as_view(), name='api_token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='api_token_verify'),
]