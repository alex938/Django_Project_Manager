from django.urls import URLPattern, path
from typing import List
from . import views

app_name: str = 'tasks'

urlpatterns: List[URLPattern] = [
    path('add/', views.add, name='add'),
    path('<uuid:pk>/', views.tasklist, name='tasklist'),
    path('<uuid:pk>/edittasklist/', views.edittasklist, name='edittasklist'),
    path('<uuid:pk>/delete/', views.delete, name='delete'),
]