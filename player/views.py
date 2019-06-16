from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Player, Character, Race
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from history.models import History


class PlayerListView(ListView):
    model = Player


class PlayerDetailView(ListView):
    model = History
    template_name = 'player/player_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PlayerDetailView, self).get_context_data(*args, **kwargs)
        try:
            character = Character.objects.get(id=self.kwargs.get('pk'))
            player = Player.objects.filter(id=character.player.id).first()
            history_set = History.objects.all()
            cleaned_set = []

            for history in history_set:
                if history.character.player == player:
                    cleaned_set.append(history)

            context['history'] = cleaned_set

            context['character'] = Character.objects.filter(player=player)
        except:
            context['history'] = History.objects.none()
            context['character'] = Character.objects.none()

        #character = get_object_or_404(Character, pk=self.kwargs.get('pk'))
        return context


class PlayerCreateView(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['reddit', 'discord', 'dm_bool']


class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ['reddit', 'discord', 'dm_bool']


class PlayerDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = "/"


class CharacterListView(ListView):
    model = Character

class CharacterDetailView(ListView):
    model = History
    template_name = 'player/character_detail.html'

    def get_queryset(self):
        character = get_object_or_404(Character, pk=self.kwargs.get('pk'))
        return History.objects.filter(character=character)


class DMDetailView(ListView):
    model = History
    template_name = 'player/dm_detail.html'

    def get_queryset(self):
        dm = get_object_or_404(Player, pk=self.kwargs.get('pk'))
        history_set = History.objects.all()
        cleaned_set = []

        for history in history_set:
            if history.mission.dm == dm:
                cleaned_set.append(history)

        return cleaned_set