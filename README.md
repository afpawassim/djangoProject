# django_Project

ceci est un projet académique pour apprendre django

## Le jeu

Le jeu est une ligue de footbal classique.

- une ligue est composée de plusieurs équipes, elle est définie par une année et un status (en cours, terminée)

- une équipe a une id de la fifa et un pays. Une équipe peut participer à plusieurs ligues( premiére division et champions league par exemple).

- un match est défini par une date, un score, une équipe domicile et une équipe extérieur. Un match est joué dans une ligue. Suite à l'ajout d'une équipe à la ligue, il faut ajouter les matchs de la ligue. un match est crée alors sans score et une fois le match joué, on peut ajouter le score.

classement =(   ligue ,    equipe ,    rank_ligue ,    match_played ,    wins ,    draws ,    losses ,    goals_for ,    goals_against ,    goal_diff ,    points ,    points_per_match )

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