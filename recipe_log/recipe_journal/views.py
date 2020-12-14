from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    """The home page for recipe_journal"""
    return render(request,'recipe_journal/index.html')

#Login view pointing to Login webpage
class LoginView(TemplateView):
    template_name ='recipe_journal/login.html'

#Profile view pointing to Profile webpage    
class ProfileView(TemplateView):
    template_name ='recipe_journal/profile.html'

#Search view pointing to Login webpage    
class SearchView(TemplateView):
    template_name ='recipe_journal/search.html'

#Add_Recipe view pointing to Add_recipe webpage    
class Add_RecipeView(TemplateView):
    template_name ='recipe_journal/add_recipe.html'