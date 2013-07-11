"""
View Module
"""
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.utils.datastructures import SortedDict
from django.shortcuts import redirect
from game.views import TView, LView
from game.models.session import Session
from game.models.user import UserProfile


class HomeView(TView):
    """
    View class for home page
    """
    template_name = 'CartaTemplates/home.html'
    page_title = 'Love Letter - Home'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["game_queue"] = Session.objects.filter(status="waiting")
        return context


class CreateView(TView):
    """
    View class for game creation
    """
    template_name = 'CartaTemplates/create.html'
    page_title = 'Love Letter - Create New Game'


class GameView(TView):
    """
    View class for gameplay
    """
    template_name = 'CartaTemplates/game.html'
    page_title = 'Love Letter - Game'

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)
        pk = kwargs.get("pk")
        session = Session.objects.get(id=pk)
        context["page_title"] = "%s ID # %s" % (self.__class__.page_title, pk)
        context["pk"] = pk
        context["name"] = session.name
        return context


def process_create(request):
    num_players = request.POST.get("num_players", 4)
    session = Session.objects.create(max_players=num_players)
    session.name = request.POST.get("name")
    session.password = request.POST.get("password")
    user_profile = request.user.profile
    session.add_player(user_profile)
    return redirect('/CartaDeAmor/game/%d/' % session.id)
