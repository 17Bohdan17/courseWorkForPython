
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # Панель администратора
    path('entertainment/', include('entertainment.urls')), # Все маршруты из приложения "entertainment"
]

