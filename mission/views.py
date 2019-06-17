from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Mission, Zone
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from history.models import History


class MissionListView(ListView):
    model = Mission
    ordering = ['-date']


class MissionDetailView(ListView):
    model = History
    template_name = 'mission/mission_detail.html'

    def get_queryset(self):
        mission = get_object_or_404(Mission, pk=self.kwargs.get('pk'))
        return History.objects.filter(mission=mission)

    def get_context_data(self, *args, **kwargs):
        context = super(MissionDetailView, self).get_context_data(*args, **kwargs)
        mission = get_object_or_404(Mission, pk=self.kwargs.get('pk'))
        context['history'] = History.objects.filter(mission=mission)

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

        for history in History.objects.filter(mission=mission):
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
        return context


class ZoneDetailView(ListView):
    model = History
    template_name= 'mission/zone_detail.html'

    def get_queryset(self):
        zone = get_object_or_404(Zone, pk=self.kwargs.get('pk'))
        history_set = History.objects.all()
        cleaned_set = []
        mission_keys = []
        for history in history_set:
            if history.mission.zone == zone:
                if history.mission.id not in mission_keys:
                    cleaned_set.append(history)
                    mission_keys.append(history.mission.id)

        return cleaned_set


class ZoneListView(ListView):
    model = Zone
    template_name = 'mission/zone_list.html'


class MissionCreateView(LoginRequiredMixin, CreateView):
    model = Mission
    fields = ['title', 'zone', 'lfg', 'aar', 'date', 'level', 'dm']


class MissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Mission
    fields = ['title', 'zone', 'lfg', 'aar', 'date', 'level', 'dm']


class MissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Mission
    success_url = "/"
