from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    """The home page for recipe_journal"""
    return render(request,'recipe_journal/index.html')

class LoginView(TemplateView):
    template_name ='recipe_journal/login.html'
    
class ProfileView(TemplateView):
    template_name ='recipe_journal/profile.html'
    
class SearchView(TemplateView):
    template_name ='recipe_journal/search.html'
    
class Add_RecipeView(TemplateView):
    template_name ='recipe_journal/add_recipe.html'