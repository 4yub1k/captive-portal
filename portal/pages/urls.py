from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('error',views.error, name='error'),
    path('success',views.success, name='success')
 ]