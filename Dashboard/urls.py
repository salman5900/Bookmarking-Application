from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_bookmark/', views.add_bookmark, name='add_bookmark'),
    path('files/', views.files, name='files'),
     path('other_files/', views.other_files, name='other_files'),
    path('edit_bookmark/<slug:slug>/', views.edit_bookmark, name='edit_bookmark'),
    path('delete_bookmark/<slug:slug>/', views.delete_bookmark, name='delete_bookmark'),
    path('acces_each_file/<slug:slug>/', views.acces_each_file, name='acces_each_file'),
    path('delete_file/<slug:slug>/', views.delete_file, name='delete_file'),
   
]