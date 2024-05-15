from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:tour_id>/detail', views.tourdetail,name='tourdetail'),
    path('apply', views.myapply, name='myapply'),
    path('requests', views.requests, name='requests'),
    path('<uuid:pk>/edit/',views.CheckRes.as_view(), name='editres'),
    path('<uuid:rnd_id>/matches', views.matches,name='matches'),
    path('search', views.search, name='search'),
    path('<uuid:plr_id>/info', views.playerinfo,name='player'),
#   path('fixtures', views.fixtures, name='fixtures')
]