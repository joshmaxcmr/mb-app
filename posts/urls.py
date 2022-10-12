from django.urls import path
from .views import PageAccueil

urlpatterns = [
    path('', PageAccueil.as_view(), name='home'),
]
