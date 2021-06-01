from django.urls import path
from .views import *

urlpatterns = [
    path('', Top.as_view(), name='top'),
    path('signup/', Signup.as_view(), name='signup')
]