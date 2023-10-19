from django.urls import path
from .views import add_icecream, success

urlpatterns = [
    path('add/', add_icecream, name='add-icecream'),
    path('success/', success, name='success'),
]
