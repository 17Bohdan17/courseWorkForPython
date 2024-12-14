
from django.urls import path
from . import views

urlpatterns = [
    path('', views.center_list, name='center_list'),  # Список всех центров
    path('<int:pk>/', views.center_detail, name='center_detail'),  # Детали центра
    path('add/', views.center_add, name='center_add'),  # Добавление центра
    path('<int:pk>/edit/', views.center_edit, name='center_edit'),
    path('<int:pk>/delete/', views.center_delete, name='center_delete'),  # Удаление центра
    path('add-center-type/', views.add_center_type, name='add_center_type'),


]

