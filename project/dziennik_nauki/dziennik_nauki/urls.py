from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

class LogoutGETAllowed(LogoutView):
    http_method_names = ['get', 'post']

urlpatterns = [
    path('admin/', admin.site.urls),
    path('konto/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('konto/logout/', LogoutGETAllowed.as_view(), name='logout'),
    path('', include('nauka.urls')),
]
