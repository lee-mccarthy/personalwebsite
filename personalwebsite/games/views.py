from django.views.generic import DetailView, TemplateView

from .models import Game


class GameDetail(DetailView):
    template_name = 'games/game_detail.html'
    model = Game
