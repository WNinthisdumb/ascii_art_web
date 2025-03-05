from django.urls import path
from textart.views import text_to_ascii

urlpatterns =[
    path('', text_to_ascii, name='text_to_ascii')
]