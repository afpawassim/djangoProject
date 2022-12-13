from django.http import HttpResponse
from django.shortcuts import render

import pandas as pd
import json
from .models import *
from .forms import EquipeForm, LigueForm, MatchForm
from django.core import serializers

from .models import createrow_season_score

# Create your views here.
def index(request):
    scores = SeasonScore.objects.all().order_by('ligue', 'rank_ligue')
    context = {'d': list(scores)}
    #to do add equipe & match    
    return render(request, 'competition/index_competition.html',context)
      


def form_ligue(request):
    #return HttpResponse("output") 
    #return render(request, 'competition/form_ligue.html',{})
    context = {}
    form = LigueForm(request.POST or None)
    #to do context['form'] = form
    context['formset'] = form

    if form.is_valid():
        # add other values
        form.instance.status = 'active'
        form.save()
        return HttpResponse("ligue saved")
    return render(request, "competition/form_ligue.html", context)

# view for form to edit an existing Ligue
def edit_ligue(request, ligue_id):
    ligue = Ligue.objects.get(id=ligue_id)
    context = {}
    form = LigueForm(request.POST or None, instance=ligue)
    context['formset'] = form
    if form.is_valid():
        form.save()
        return HttpResponse("ligue saved")
    return render(request, "competition/form_ligue.html", context)

def form_equipe(request):
    context = {}
    form = EquipeForm(request.POST or None)
    context['formset'] = form
    if form.is_valid():
        form.save()
        createrow_season_score(form.instance)
        return HttpResponse("equipe saved")
    return render(request, "competition/form_equipe.html", context)

def form_match(request):
    context = {}
    form = MatchForm(request.POST or None)
    context['formset'] = form
    if form.is_valid():
        form.save()
        update_classement(form.instance)
        return HttpResponse("match saved")
    return render(request, "competition/form_match.html", context)

def table_ligue(request):
    ligues = Ligue.objects.all()
    context = {'d': list(ligues)}
    #to do add equipe & match
    return render(request, 'competition/tligues.html', context)

def table_match(request):
    matches = Match.objects.all()
    context = {'d': list(matches)}
    #to do add equipe & match
    return render(request, 'competition/tmatches.html', context)    

def table_equipe(request):
    equipes = Equipe.objects.all()
    context = {'d': list(equipes)}
    #to do add equipe & match
    return render(request, 'competition/tequipes.html', context)