from django.shortcuts import render, redirect
from .models import Tournament, MyApply, Round, Match, Player
from .forms import MyApplyForm, MyApplyEditForm
from django.views import generic
from django.urls import reverse_lazy

def index(request):
    tours = Tournament.objects.all().filter(finished=False)
    notchecked = MyApply.objects.all().filter(status=None).count()
    context = {'tours':tours, 'notchecked':notchecked}
    return render(request, 'index.html', context)

def tourdetail(request,tour_id):
    tour = Tournament.objects.get(id=tour_id)
    rounds = Round.objects.all().filter(tournament=tour)
    context = {'tournament':tour, 'rounds':rounds}
    return render(request, 'tournament/abouttour.html', context)

def myapply(request):
    if request.method == 'POST':
        form = MyApplyForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            Player.objects.create(FullName=new.FullName,PubgName=new.PubgName,PubgID=new.PubgID)
            return redirect('index')
    else:
        form = MyApplyForm()
    context = {'form': form}
    return render(request, 'tournament/apply.html', context)

def requests(request):
    requests = MyApply.objects.all().order_by('-applydate')
    notchecked = MyApply.objects.all().filter(status=None).count()
    rescount = MyApply.objects.all().count()
    return render(request, 'ForAdmin/requests.html', {'requests':requests, 'notchecked':notchecked,'rescount':rescount})

class CheckRes(generic.UpdateView):
    model = MyApply
    form_class = MyApplyEditForm
    template_name = 'ForAdmin/check.html'
    success_url = reverse_lazy('requests')

def matches(request, rnd_id):
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