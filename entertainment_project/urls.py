
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # Панель администратора
    path('centers/', include('centers.urls')), # Все маршруты из приложения "centers"
]

