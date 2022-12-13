from django import forms

import datetime
from .models import Ligue
from .models import Equipe
from .models import Match


class LigueForm(forms.ModelForm):
    
        class Meta:
            model = Ligue
            fields = ('titre', 'code_ligue', 'year')
            #titre = forms.CharField(label='Titre', max_length=50)
            #code_ligue = forms.CharField(label='Code Ligue', max_length=250)
            #year = forms.IntegerField(label='Année', min_value=2000, max_value=2050)
            widgets = {
                'titre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Titre'}),
                'code_ligue': forms.TextInput(attrs={'class': 'form-control'}),
                'year': forms.TextInput(attrs={'class': 'form-control'}),
            }

            labels = {
                'titre': 'Titre',
                'code_ligue': 'Code Ligue',
                'year': 'Année',
            }


class MatchForm(forms.ModelForm):
        
            class Meta:
                model = Match
                fields = ('ligue', 'date', 'id_locaux', 'id_visiteur', 'score_locaux', 'score_visiteur','code_match', 'local')
                #ligue = forms.ModelChoiceField(queryset=Ligue.objects.all())
                ## input date html5 with helper
                ##date = forms.DateField(label='Date', default=datetime.date.today)#input_formats='2022-12-12 19:56:59+00:00 0', initial='2022-12-12 19:56:59+00:00 0') #help_text="format (yyyy-mm-dd)")
                #date = forms.DateTimeField(label='Date', initial=datetime.datetime.now) #,default=datetime.datetime.now
                #id_locaux = forms.ModelChoiceField(queryset=Equipe.objects.all())
                #id_visiteur = forms.ModelChoiceField(queryset=Equipe.objects.all())
                #score_locaux = forms.IntegerField(label='Score Locaux')
                #score_visiteur = forms.IntegerField(label='Score Visiteur')
                #code_match = forms.CharField(label='Code Match', max_length=50)
                ## local is choices=(('0', 'alle'), ('1', 'retour'))
                #local = forms.ChoiceField(label='Local', choices=(('0', 'alle'), ('1', 'retour')))
                widgets = {
                    'ligue': forms.Select(attrs={'class': 'form-control'}),
                    'date': forms.DateTimeInput(attrs={'class': 'form-control', 
                                                       #'placeholder': datetime.datetime.now,
                                                       'value': datetime.datetime.now,
                                                       }),
                    'id_locaux': forms.Select(attrs={'class': 'form-control'}),
                    'id_visiteur': forms.Select(attrs={'class': 'form-control'}),
                    'score_locaux': forms.NumberInput(attrs={'class': 'form-control'}),
                    'score_visiteur': forms.NumberInput(attrs={'class': 'form-control'}),
                    'code_match': forms.TextInput(attrs={'class': 'form-control'}),
                    'local': forms.Select(attrs={'class': 'form-control'}),
                }

class EquipeForm(forms.ModelForm):
        
            class Meta:
                model = Equipe
                fields = ('nom', 'id_federation', 'pays','ligues')
                nom = forms.CharField(label='Nom', max_length=50)
                id_federation = forms.IntegerField(label='ID Fédération')
                pays = forms.CharField(label='Pays', max_length=50)
                ligues = forms.ModelMultipleChoiceField(queryset=Ligue.objects.all())





            