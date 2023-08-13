from django.contrib import admin
from django.urls import path, include
from app_one import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('app_one/', include('app_one.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('special', views.special, name='special'),
]
