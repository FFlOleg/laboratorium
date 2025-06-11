from django.urls import path
from . import views
from .views import EdytujTemat, UsunTemat

urlpatterns = [
    path('', views.lista_tematow, name='lista'),
    path('dodaj/', views.dodaj_temat, name='dodaj_temat'),
    path('temat/<int:temat_id>/', views.szczegoly_temat, name='szczegoly'),
    path('temat/<int:temat_id>/dodaj_notatke/', views.dodaj_notatke, name='dodaj_notatke'),
    path('temat/<int:pk>/edytuj/', EdytujTemat.as_view(), name='edytuj_temat'),
    path('temat/<int:pk>/usun/', UsunTemat.as_view(), name='usun_temat'),
]
