from django import forms
from django.forms import ModelForm
from .models import Tournament, MyApply,Player, Round, Match

class MatchCreationForm(ModelForm):

    class Meta:
        model = Match
        fields = ('player_1', 'player_2', 'forround', 'overall_1', 'overall_2', 'matchvideo', 'tournament_winner')
        labels = {
            'player_1': 'Player 1',
            'player_2' : 'Player 2',
            'forround' : 'For Round',
            'overall_1' : 'Overall 1',
            'overall_2' : 'Overall 2',
            'matchvideo' : 'Match Video',
            'tournament_winner' : 'Chempion Name'
        }
        widgets = {
            'player_1' : forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder' : 'Player 1'}),
            'player_2' : forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder' : 'Player 2'}),
            'forround' : forms.Select(attrs={'class': 'form-control my-1', 'placeholder' : 'Player 1'}),
            'overall_1' : forms.NumberInput(attrs={'class': 'form-control my-1', 'placeholder' : 'Overall 1'}),
            'overall_2' : forms.NumberInput(attrs={'class': 'form-control my-1', 'placeholder' : 'Overall 2'}),
            'matchvideo' : forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder' : 'Match Video link'}),
            'tournament_winner' : forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder' : 'Chempion Name'}),
        }

class RoundCreationForm(ModelForm):

    class Meta:
        model = Round
        fields = ('round_number', 'tournament', 'finished')
        labels = {
            'round_number' : 'Round number',
            'tournament' : 'Tournament ',
            'finished': 'Finished ?'
        }
        widgets = {
            'round_number':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Round number'}),
            'tournament': forms.Select(attrs={'class':'form-control my-1', 'placeholder':'Tournament Name'}),
            'finished' : forms.CheckboxInput(attrs={'class':'form-check','placeholder':'Finished ?'}),
        }

class TournamentCreationForm(ModelForm):
    
    class Meta:
        model = Tournament
        fields = ('tournament_name',
                  'Prize',
                  'tournament_rules',
                  'participants',
                  'squad', 
                  'weapon', 
                  'started',
                  'start_date',
                  'end_date' ,
                  'finished' ,
                  'available',
                  'isfull'
                  )
        labels = {
            'tournament_name':"Tournament Name",
            'Prize':"Prize",
            'tournament_rules':"Tournament Rules",
            'participants':"Participants",
            'squad':"Squad type", 
            'weapon':"Weapon", 
            'started':"Started ?",
            'start_date':"Start date",
            'end_date' :"End date",
            'finished' :"Finished ?",
            'available':"Available ?",
            'isfull':"Full ?"
        }
        widgets = {
            'tournament_name':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Tournament Name'}),
            'Prize':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Prize'}),
            'tournament_rules': forms.Textarea(attrs={'class':'form-control my-1', 'placeholder':'Tournament Rules'}),
            'participants' : forms.Textarea(attrs={'class':'form-control my-1', 'placeholder':'Participants'}),
            'squad' : forms.Select(attrs={'class':'form-control my-1', 'placeholder':'Squad type'}),
            'weapon' : forms.Select(attrs={'class':'form-control my-1', 'placeholder':'Weapon type'}),
            'started' : forms.CheckboxInput(attrs={'class':'form-check my-1','placeholder':'Started ?'}),
            'start_date' : forms.DateInput(attrs={'class':'form-control my-1','placeholder':'Started date','type':'date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control my-1', 'placeholder':'Ending date','type':'date'}),
            'finished' : forms.CheckboxInput(attrs={'class':'form-check','placeholder':'Finished ?'}),
            'available' : forms.CheckboxInput(attrs={'class':'form-check my-1', 'placeholder': 'Available'}),
            'isfull' : forms.CheckboxInput(attrs={'class':'form-check my-1', 'placeholder': 'Available'})
            }

class MyApplyForm(ModelForm):
    """
    def __init__(self, MyApplyForm, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tournament_name"].queryset = Tournament.objects.filter(finished=False)
    """
    class Meta:
        model = MyApply
        fields = ('FullName', 'PubgName', 'PubgID','tgusername', 'tournament_name')
        labels = {
            'FullName' : 'Full Name',
            'PubgName' : 'Pubg Name',
            'PubgID' : 'Pubg ID',
            'tgusername' : 'Tg Username',
            'tournament_name' : 'Choose tournament'
        }
        widgets = {
            'FullName':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Full Name'}),
            'PubgName':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Pubg Name'}),
            'PubgID':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Pubg ID'}),
            'tgusername' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Telegram username'}),
            'tournament_name': forms.Select(attrs={'class':'form-control my-1', 'placeholder':'Tournament Name'}),
        }

class MyApplyEditForm(ModelForm):

    class Meta:
        model = MyApply
        fields = ('FullName', 'PubgName', 'PubgID', 'tgusername','tournament_name', 'status')
        labels = {
            'FullName' : 'Full Name',
            'PubgName' : 'Pubg Name',
            'PubgID' : 'Pubg ID',
            'tournament_name' : 'Choose tournament',
            'tgusername' : 'Tg Username',
            'status' : 'Confirm'
        }
        widgets = {
            'FullName':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Full Name'}),
            'PubgName':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Pubg Name'}),
            'PubgID':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Pubg ID'}),
            'tgusername' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Telegram username'}),
            'tournament_name': forms.Select(attrs={'class':'form-control my-1', 'placeholder':'Tournament Name'}),
            'status' : forms.CheckboxInput(attrs={'class':'form-check', 'placeholder':'Confirm or Not'})
        }
    
class AddPointForm(ModelForm):

    class Meta:
        model = Player
        fields = ('FullName', 'PubgName', 'PubgID','point','win', 'lose', 'played', 'trophy')
        labels = {
            'FullName': "Full Name",
            'PubgName' : "Pubg Name",
            'PubgID' : 'Pubg ID',
            'point' : 'Points',
            'win' : 'Wins',
            'lose' : 'Loses',
            'played' : "Played",
            'trophy' : 'Trophy'
        }
        widgets = {
            'FullName':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Full Name'}),
            'PubgName':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Pubg Name'}),
            'PubgID':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Pubg ID'}),
            'point' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Point'}),
            'win' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Win'}),
            'lose' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Lose'}),
            'played' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Played'}),
            'trophy' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Trophy'}),
        }
