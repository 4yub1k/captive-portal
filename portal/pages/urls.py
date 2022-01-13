from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('error',views.error, name='error'),
    path('success',views.success, name='success')
 ]