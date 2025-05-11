from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_bookmark/', views.add_bookmark, name='add_bookmark'),
    path('edit_bookmark/<slug:slug>/', views.edit_bookmark, name='edit_bookmark'),
    path('delete_bookmark/<slug:slug>/', views.delete_bookmark, name='delete_bookmark'),
    
]