from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mission.views import (
    MissionListView, MissionDetailView, MissionCreateView, MissionUpdateView, MissionDeleteView,
    ZoneDetailView
    )

from player.views import (
    PlayerListView, PlayerDetailView, PlayerCreateView, PlayerUpdateView, PlayerDeleteView,
    CharacterListView, CharacterDetailView,
    DMDetailView
)

from loot.views import (
    LootListView, LootDetailView,
)

urlpatterns = [
    path('', MissionListView.as_view()),

    path('mission/list/', MissionListView.as_view(), name='mission-list'),
    path('mission/<int:pk>/', MissionDetailView.as_view(), name='mission-detail'),
    path('mission/create/', MissionCreateView.as_view(), name='mission-create'),
    path('mission/<int:pk>/update/', MissionUpdateView.as_view(), name='mission-update'),
    path('mission/<int:pk>/delete/', MissionDeleteView.as_view(), name='mission-delete'),

    path('zone/<int:pk>', ZoneDetailView.as_view(), name='zone-detail'),

    path('player/', PlayerListView.as_view(), name='player-list'),
    path('player/list/', PlayerListView.as_view()),
    path('player/<int:pk>/', PlayerDetailView.as_view(), name='player-detail'),
    path('player/create/', PlayerCreateView.as_view(), name='player-create'),
    path('player/<int:pk>/update/', PlayerUpdateView.as_view(), name='player-update'),
    path('player/<int:pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),

    path('dm/<int:pk>', DMDetailView.as_view(), name='dm-detail'),

    path('character/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('character/', CharacterListView.as_view(), name='character-list'),

    path('loot/', LootListView.as_view(), name='loot-list'),
    path('loot/<int:pk>', LootDetailView.as_view(), name='loot-detail'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)