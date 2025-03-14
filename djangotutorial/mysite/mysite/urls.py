from django.contrib import admin
from django.urls import path, include  # импортируем include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),  # подключаем маршруты из приложения polls
]
