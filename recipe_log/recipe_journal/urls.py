"""Defines URL patterns for Recipe_journal."""
from django.urls import path
from .import views
from django.urls import include
from django.views.generic import RedirectView
from .views import LoginView, ProfileView, SearchView, Add_RecipeView

app_name='recipe_journal'
urlpatterns = [
    #homepage
    path('',views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('search/', SearchView.as_view(), name='search'),
    path('add_recipe/', Add_RecipeView.as_view(), name='add_recipe'),
]