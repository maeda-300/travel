from django.urls import path
from .views import *

urlpatterns = [
    path('', Top.as_view(), name='top'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('mypage/<int:pk>', Mypage.as_view(), name='mypage'),
    path('user_update/<int:pk>', UserUpdate.as_view(), name='user_update'),
]