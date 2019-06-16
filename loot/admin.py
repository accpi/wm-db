from django.contrib import admin
from .models import Type, Rarity, Loot


admin.site.register(Type)
admin.site.register(Rarity)
admin.site.register(Loot)