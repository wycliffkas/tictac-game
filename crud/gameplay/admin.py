# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Game,Move

# Register your models here.
# admin.site.register(Game)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id','first_player','second_player','status')
    list_editable = ('status',)
admin.site.register(Move)
