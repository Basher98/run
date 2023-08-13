from django.urls import path
from app_one import views

app_name = 'app_one'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('team/', views.team, name='team'),
    path('test/', views.test, name='test'),
]
