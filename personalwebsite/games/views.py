from django.views.generic import DetailView

from .models import Game


class GameDetail(DetailView):
    template_name = 'games/game_detail.html'
    model = Game
