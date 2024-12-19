from django.urls import path
from . import views

urlpatterns = [
    path('', views.center_list, name='center_list'),  # Список всіх центрів
    path('center/<int:pk>/', views.center_detail, name='center_detail'),  # Деталі конкретного центру
    path('add/', views.center_add, name='center_add'),  # Додавання нового центру
    path('<int:pk>/edit/', views.center_edit, name='center_edit'),  # Редагування центру
    path('<int:pk>/delete/', views.center_delete, name='center_delete'),  # Видалення центру
    path('center_type/add/', views.center_type_add, name='center_type_add'),  # Додавання нового типу центру
    path('events/', views.event_list, name='event_list'),
    path('event/add/', views.add_event, name='add_event'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),  # деталі події
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),





]
