from django.urls import path
from . import views

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('mypage/<int:pk>', views.Mypage.as_view(), name='mypage'),
    path('user_update/<int:pk>', views.UserUpdate.as_view(), name='user_update'),
    path('user_delete/<int:pk>', views.UserDelete.as_view(), name='user_delete'),
    path('memory_create/', views.MemoryCreate.as_view(), name='memory_create'),
    path('memory_detail/<int:pk>', views.MemoryDetail.as_view(), name='memory_detail'),
    path('memory_update/<int:pk>', views.MemoryUpdate.as_view(), name='memory_update'),
    path('memory_delete/<int:pk>', views.MemoryDelete.as_view(), name='memory_delete'),
    path('memory_detail/<int:pk>/comment_create/', views.comment_create, name='comment_create'),
]