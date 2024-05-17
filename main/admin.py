from django.contrib import admin
from .models import Tournament, MyApply,Round,Match,Player,TvVideo

admin.site.register(Tournament)
admin.site.register(MyApply)
admin.site.register(Round)
admin.site.register(Match)  
admin.site.register(Player)
admin.site.register(TvVideo)