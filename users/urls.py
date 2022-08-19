from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name='users'
 
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.signup,name='login'),
    path('logout/',views.logout,name='logout')
]