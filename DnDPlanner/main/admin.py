"""
Describes which database tables should be visible in the admin pages and
further, how those fields should be represented.
"""

from django.contrib import admin
from .models import Campaign, Location, Encounter, Item, Creature, PlotMoment, Note, Skill, Tool, WeaponProperty, Map

admin.site.register(Campaign)
admin.site.register(Location)
admin.site.register(Encounter)
admin.site.register(Item)
admin.site.register(Creature)
admin.site.register(PlotMoment)
admin.site.register(Note)
admin.site.register(Skill)
admin.site.register(Tool)
admin.site.register(WeaponProperty)
admin.site.register(Map)
