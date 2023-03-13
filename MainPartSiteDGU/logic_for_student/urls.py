from django.urls import path, include
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('create_events/', CreateEvents.as_view(), name='create_events'),
    path('detail_events/<int:pk>/', DetailEvent.as_view(), name='detail_events'),
    path('detail_events/<int:pk>/_edit/', EditEvent.as_view(), name='edit_detail_events'),
    path('', ListEvents.as_view(), name='list_events'),
]
