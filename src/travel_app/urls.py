from django.urls import path
from .views import *

urlpatterns = [
    path('', Top.as_view(), name='top'),
]