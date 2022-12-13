from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Match)


class LiguesAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'status', 'code_ligue', 'year')
admin.site.register(Ligue, LiguesAdmin)


class EquipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'id_federation', 'pays')

admin.site.register(Equipe, EquipeAdmin)

class SeasonScoreAdmin(admin.ModelAdmin):
    list_display = ('ligue', 'equipe', 'rank_ligue', 'match_played', 'wins', 'draws',
                    'losses', 'goals_for', 'goals_against', 'goal_diff', 'points', 'points_per_match')
    list_filter = ('ligue', 'equipe')    
    search_fields = ('ligue', 'equipe')    
    ordering = ('rank_ligue', 'ligue', 'equipe')


admin.site.register(SeasonScore, SeasonScoreAdmin)
