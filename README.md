# django_Project

ceci est un projet académique pour apprendre django.

published on https://github.com/afpawassim/djangoProject

## Le jeu

Le jeu est une ligue de footbal classique.

- une ligue est composée de plusieurs équipes, elle est définie par une année et un status (en cours, terminée)

- une équipe a une id de la fifa et un pays. Une équipe peut participer à plusieurs ligues( premiére division et champions league par exemple).

- un match est défini par une date, un score, une équipe domicile et une équipe extérieur. Un match est joué dans une ligue. Suite à l'ajout d'une équipe à la ligue, il faut ajouter les matchs de la ligue. un match est crée alors sans score et une fois le match joué, on peut ajouter le score.

- une équipe est classée dans une ligue. Le classement est calculé à partir des scores des matchs de la ligue. Il est calculé à chaque fois qu'un match est joué. le classement va afficher:
    1. la ligue en question
    2. l'équipe en question
    3. le rang de l'équipe dans la ligue
    4. le nombre de matchs joués
    5. le nombre de victoires
    6. le nombre de matchs nuls
    7. le nombre de défaites
    8. le nombre de buts marqués
    9. le nombre de buts encaissés
    10. la différence de buts
    11. le nombre de points : 3 points pour une victoire, 1 point pour un match nul, 0 point pour une défaite
    12. le nombre de points par match



## Installation

pip install freeze.txt

## Lancement

python manage.py runserver 5555

 ou bien

 avec python myrun.py

 ## Users

 Admin : admin / admin
 no need for connection for other users

 ## Liens
http://127.0.0.1:5555/competition


http://127.0.0.1:5555/admin

 ## Classement dynamique

 dans competition/models.py j'ai définie les fonctions (appélées dans models.py et dans views.py) suivantes:

 ```python

def update_rank_ligue_all():
    ''' Mettre à jour le classement de toutes les ligues'''
    ...


def update_rank_ligue(l: Ligue):
    '''Mettre à jour le classement de la ligue l
    l'ordre est fait par points, goal_diff, goals_for''' 
    ...

def createrow_season_score(e: Equipe):
    '''Créer une ligne de classement pour chaque ligue de l'équipe e'''
    ...


def update_classement(current_match: Match):
    '''Mettre à jour le classement de la ligue du match courant le rank_ligue est calculé à la volée'''
 ```

 https://docs.google.com/spreadsheets/d/1U0jiIkfuGuQnkL0w0CU59JWGDt7027drrHwZKnyx8B0/edit#gid=0