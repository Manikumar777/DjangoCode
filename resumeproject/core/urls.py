from unicodedata import name
from django.urls import path
from .views import *
urlpatterns = [
    path('kumar/', sample, name="sample"),
    path('post-todo/', post_todo, name="post_todo")
    
]