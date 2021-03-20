from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('<pk>/', views.GameDetail.as_view(), name='game_detail'),
]
