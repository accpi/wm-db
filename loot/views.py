from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Loot
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from history.models import History


class LootListView(ListView):
    model = Loot


class LootDetailView(DetailView):
    model = Loot
