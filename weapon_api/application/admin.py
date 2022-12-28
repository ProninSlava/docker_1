from django.contrib import admin

from application.models import Weapon


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'strength', 'protection']

