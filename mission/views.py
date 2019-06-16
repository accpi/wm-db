from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Mission, Zone
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from history.models import History


class MissionListView(ListView):
    model = Mission


class MissionDetailView(ListView):
    model = History
    template_name = 'mission/mission_detail.html'

    def get_queryset(self):
        mission = get_object_or_404(Mission, pk=self.kwargs.get('pk'))
        return History.objects.filter(mission=mission)


class ZoneDetailView(ListView):
    model = History
    template_name='mission/zone_list.html'

    def get_queryset(self):
        zone = get_object_or_404(Zone, pk=self.kwargs.get('pk'))
        history_set = History.objects.all()
        cleaned_set = []

        for history in history_set:
            if history.mission.zone == zone:
                cleaned_set.append(history)

        return cleaned_set


class MissionCreateView(LoginRequiredMixin, CreateView):
    model = Mission
    fields = ['title', 'lfg', 'aar', 'date', 'level', 'dm']


class MissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Mission
    fields = ['title', 'lfg', 'aar', 'date', 'level', 'dm']


class MissionDeleteView(LoginRequiredMixin, DeleteView):
    model = Mission
    success_url = "/"
