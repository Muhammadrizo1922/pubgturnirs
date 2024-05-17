from django.shortcuts import render, redirect
from .models import Tournament, MyApply, Round, Match, Player,TvVideo,Match
from .forms import MyApplyForm, MyApplyEditForm,AddPointForm, TournamentCreationForm,RoundCreationForm,MatchCreationForm
from django.views import generic
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

today = datetime.today()

def index(request):
    tours = Tournament.objects.all().filter(finished=False)
    notchecked = MyApply.objects.all().filter(status=None).count()
    context = {'tours':tours, 'notchecked':notchecked}
    return render(request, 'index.html', context)

def tourdetail(request,tour_id):
    tour = Tournament.objects.get(id=tour_id)
    rounds = Round.objects.all().filter(tournament=tour).order_by('date')
    context = {'tournament':tour, 'rounds':rounds}
    return render(request, 'tournament/abouttour.html', context)

def myapply(request):
    if request.method == 'POST':
        form = MyApplyForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            if Player.objects.filter(PubgID=new.PubgID).exists():
                new.save()
                return redirect('index')
            else:
                new.save()
                Player.objects.create(FullName=new.FullName,PubgName=new.PubgName,PubgID=new.PubgID)
                return redirect('index')
    else:
        form = MyApplyForm()
    context = {'form': form}
    return render(request, 'tournament/apply.html', context)

@login_required(login_url="warning")
def requests(request):
    requests = MyApply.objects.all().order_by('-applydate')
    notchecked = MyApply.objects.all().filter(status=None).count()
    rescount = MyApply.objects.all().count()
    return render(request, 'ForAdmin/requests.html', {'requests':requests, 'notchecked':notchecked,'rescount':rescount})

class CheckRes(LoginRequiredMixin,generic.UpdateView):
    model = MyApply
    form_class = MyApplyEditForm
    template_name = 'ForAdmin/check.html'
    success_url = reverse_lazy('requests')

def roundmatches(request, rnd_id):
    forround = Round.objects.get(id=rnd_id)
    matches = Match.objects.all().filter(forround=forround)
    context = {'matches':matches}
    return render(request, 'tournament/matches.html',context)

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        tours = Tournament.objects.filter(tournament_name__contains=search)
        players = Player.objects.filter(FullName__contains=search)
        return render(request, 'search.html', {'tours':tours,'players':players,'search':search})
    else:
        return render(request, 'search.html',)

def playerinfo(request,plr_id):
    player = Player.objects.get(id=plr_id)
    context = {'player':player}
    return render(request, 'tournament/player.html', context)

def leadersboard(request):
    players = Player.objects.all().order_by('-point')
    context = {"players":players}
    return render(request, 'tournament/leadersboard.html', context)

def videos(request):
    videos = TvVideo.objects.all().filter(remove=False)
    return render(request, 'TV/ourtv.html', {'videos':videos})

@login_required(login_url="warning")
def allplayers(request):
    allplayers = Player.objects.all()
    allplayerscount = Player.objects.all().count()
    return render(request, 'ForAdmin/players.html', {'allplayers':allplayers, 'allplayerscount':allplayerscount})

class Addpoint(LoginRequiredMixin,generic.UpdateView):
    model = Player
    form_class = AddPointForm
    template_name = 'ForAdmin/addpoint.html'
    success_url = reverse_lazy('allplayers')

@login_required(login_url="warning")
def tournaments(request):
    tournaments = Tournament.objects.all()
    return render(request, 'ForAdmin/tournaments.html', {'tournaments' : tournaments})

@login_required(login_url="warning")
def createtour(request):
    if request.method == 'POST':
        form = TournamentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TournamentCreationForm()
    return render(request, 'ForAdmin/createtour.html', {'form':form})

class TourEdit(LoginRequiredMixin,generic.UpdateView):
    model = Tournament
    form_class = TournamentCreationForm
    template_name = 'ForAdmin/edittour.html'
    success_url = reverse_lazy('tournaments')

@login_required(login_url="warning")
def allrounds(request):
    rounds = Round.objects.all()
    return render(request, 'ForAdmin/rounds.html', {"rounds":rounds})

@login_required(login_url="warning")
def createround(request):
    if request.method == 'POST':
        form = RoundCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rounds')
    else:
        form = RoundCreationForm()
    return render(request, 'ForAdmin/createround.html', {'form':form})

class RoundChange(LoginRequiredMixin,generic.UpdateView):
    model = Round
    form_class =RoundCreationForm
    template_name = 'ForAdmin/editround.html'
    success_url = reverse_lazy('rounds')

@login_required(login_url="warning")
def matches(request):
    matches = Match.objects.all()
    return render(request, 'ForAdmin/matches.html', {'matches':matches})

@login_required(login_url="warning")
def newmatch(request):
    if request.method == 'POST':
        form = MatchCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matches')
    else:
        form = MatchCreationForm()
    return render(request, 'ForAdmin/newmatch.html', {'form':form})

class UpdateMatch(LoginRequiredMixin,generic.UpdateView):
    model = Match
    form_class =MatchCreationForm
    template_name = 'ForAdmin/updatematch.html'
    success_url = reverse_lazy('matches')

def warning(request):
    return render(request, 'warning.html')