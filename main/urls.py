from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:tour_id>/detail', views.tourdetail,name='tourdetail'),
    path('apply', views.myapply, name='myapply'),
    path('requests', views.requests, name='requests'),
    path('<uuid:pk>/edit/',views.CheckRes.as_view(), name='editres'),
    path('<uuid:rnd_id>/matches', views.roundmatches,name='roundmatches'),
    path('search', views.search, name='search'),
    path('<uuid:plr_id>/info', views.playerinfo,name='player'),
    path('leadersboard', views.leadersboard, name='leadersboard'),
    path('ourtv', views.videos, name='videos'),
    path('allplayers', views.allplayers, name='allplayers'),
    path('<uuid:pk>/addpoint/',views.Addpoint.as_view(), name='addpoint'),
    path('tournaments', views.tournaments, name='tournaments'),
    path('createtour', views.createtour, name='createtour'),
    path('<uuid:pk>/update/',views.TourEdit.as_view(), name='touredit'),
    path('allrounds', views.allrounds, name='rounds'),
    path('newround', views.createround, name='newround'),
    path('<uuid:pk>/change/',views.RoundChange.as_view(), name='roundchange'),
    path('matches', views.matches, name='matches'),
    path('newmatch', views.newmatch, name='newmatch'),
    path('<uuid:pk>/review/',views.UpdateMatch.as_view(), name='updatematch'),
    path('warning', views.warning, name='warning'),
#   path('fixtures', views.fixtures, name='fixtures')
]