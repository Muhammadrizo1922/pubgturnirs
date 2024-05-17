from .models import Tournament
from modeltranslation.translator import TranslationOptions, register

@register(Tournament)
class TournamentTranslationOptions(TranslationOptions):
    fields = ('tournament_name', 'tournament_rules')