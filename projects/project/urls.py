from django.urls import URLPattern, path
from typing import List
from . import views

app_name: str = 'project'

urlpatterns: List[URLPattern] = [
    path('', views.project, name='project'),
    path('add_project/', views.add, name='add'),
    path('<uuid:primary_key>/', views.project_detail, name='project_detail'),
    path('<uuid:primary_key>/edit/', views.edit, name='edit'),
    path('<uuid:primary_key>/delete/', views.delete, name='delete'),
]