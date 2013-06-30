"""
View Module
"""
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.utils.datastructures import SortedDict
from game.views import TView, LView
from game.models.session import Session


class HomeView(TView):
    """
    View class for home page
    """
    template_name = 'CartaTemplates/home.html'
    page_title = 'Love Letter - Home'


class CreateView(TView):
    """
    View class for game creation
    """
    template_name = 'CartaTemplates/create.html'
    page_title = 'Love Letter - Create New Game'
