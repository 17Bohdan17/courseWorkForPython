from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Панель адміна
    path('entertainment/', include('entertainment.urls')),  # Список всіх маршрутів
]
