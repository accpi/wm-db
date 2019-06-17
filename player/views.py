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

        level_values = {
            'barbarian': 0,
            'bard': 0,
            'cleric': 0,
            'druid': 0,
            'fighter': 0,
            'monk': 0,
            'paladin': 0,
            'ranger': 0,
            'rogue': 0,
            'sorcerer': 0,
            'warlock': 0,
            'wizard': 0
        }

        try:
            character = Character.objects.get(id=self.kwargs.get('pk'))
            player = Player.objects.filter(id=character.player.id).first()
            history_set = History.objects.all()
            cleaned_set = []

            for history in history_set:
                if history.character.player == player:
                    cleaned_set.append(history)

            context['history'] = cleaned_set

            for history in cleaned_set:
                level_values['barbarian'] += history.character.barbarian
                level_values['bard'] += history.character.bard
                level_values['cleric'] += history.character.cleric
                level_values['druid'] += history.character.druid
                level_values['fighter'] += history.character.fighter
                level_values['monk'] += history.character.monk
                level_values['paladin'] += history.character.paladin
                level_values['ranger'] += history.character.ranger
                level_values['rogue'] += history.character.rogue
                level_values['sorcerer'] += history.character.sorcerer
                level_values['warlock'] += history.character.warlock
                level_values['wizard'] += history.character.wizard

            context['levels'] = level_values

            context['character'] = Character.objects.filter(player=player)
        except:
            context['history'] = History.objects.none()
            context['character'] = Character.objects.none()

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
        mission_keys = []

        for history in history_set:
            if history.mission.dm == dm:
                if history.mission.id not in mission_keys:
                    cleaned_set.append(history)
                    mission_keys.append(history.mission.id)

        return cleaned_set


class RaceListView(ListView):
    model = Character
    template_name = 'player/race_list.html'

    def get_queryset(self):
        race = get_object_or_404(Race, pk=self.kwargs.get('pk'))
        return Character.objects.filter(race=race)