from django.urls import path
from .views import text_to_ascii


urlspatterns = [
    path('', text_to_ascii, name='text_to_ascii')
]