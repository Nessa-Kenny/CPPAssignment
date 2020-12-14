"""Defines URL patterns for Recipe_journal."""
from django.urls import path
from .import views
from django.urls import include
from django.views.generic import RedirectView
#need to import views created in views.py
from .views import LoginView, ProfileView, SearchView, Add_RecipeView

app_name='recipe_journal'
urlpatterns = [
    #homepage
    path('',views.index, name='index'),
    #Login page
    path('login/', LoginView.as_view(), name='login'),
    #Profile page
    path('profile/', ProfileView.as_view(), name='profile'),
    #Search page
    path('search/', SearchView.as_view(), name='search'),
    #Add_Recipe page
    path('add_recipe/', Add_RecipeView.as_view(), name='add_recipe'),
]