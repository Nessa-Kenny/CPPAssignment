"""Defines URL patterns for Recipe_journal."""
from django.urls import path
from .import views
from django.urls import include
from django.views.generic import RedirectView

app_name='recipe_journal'
urlpatterns = [
    #homepage
    path('',views.index, name='index'),
]