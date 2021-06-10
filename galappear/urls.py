from django.urls import path
from .views import index, gaming, logo

urlpatterns = [
    path('', index, name='index'),
    path('gaming/', gaming, name='gaming'),
    path('logo/', logo, name='logo')
]
