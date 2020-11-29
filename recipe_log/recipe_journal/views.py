from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    """The home page for recipe_journal"""
    return render(request,'recipe_journal/index.html')
    
#class LoginView(generic.Detail.view):
#    model = Entry
#   template_name ='recipe_journal/login.html'