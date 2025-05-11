from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_bookmark/', views.add_bookmark, name='add_bookmark'),
    path('edit_bookmark/', views.edit_bookmark, name='edit_bookmark'), 
    
]