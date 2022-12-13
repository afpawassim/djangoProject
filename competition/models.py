from django.db import models
from django.db import transaction
# Create your models here.


class Ligue(models.Model):
    titre = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=(
        ('0', 'active'), ('1', 'finie')), default='active')
    code_ligue = models.CharField(max_length=250, unique=True)
    year = models.IntegerField()

    def __str__(self):
        return self.titre


class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    #img = models.ImageField(upload_to = "images/")
    id_federation = models.BigIntegerField(unique=True)
    pays = models.CharField(max_length=50)
    ligues = models.ManyToManyField(Ligue)  # , through='EquipeLigue')

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        super(Equipe, self).save(*args, **kwargs)
        # if ligue added to equipe then create a season score for this equipe
        transaction.on_commit(lambda: createrow_season_score(self))


class Match(models.Model):
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE,
                              db_column='ligue', to_field='code_ligue')
    date = models.DateTimeField()
    id_locaux = models.ForeignKey('Equipe', on_delete=models.CASCADE, db_column='id_locaux',
                                  related_name='Equipe1', to_field='id_federation')
    id_visiteur = models.ForeignKey('Equipe', on_delete=models.CASCADE, db_column='id_visiteur',
                                    related_name='Equipe2', to_field='id_federation')
    score_locaux = models.IntegerField()
    score_visiteur = models.IntegerField()
    code_match = models.BigIntegerField(unique=True)
    local = models.CharField(max_length=50, choices=(
        ('0', 'alle'), ('1', 'retour')))

    def __str__(self):
        return str(self.id_locaux) + ' vs ' + str(self.id_visiteur) + ' ' + str(self.date) + ' ' + str(self.local)

    def save(self, *args, **kwargs):
        super(Match, self).save(*args, **kwargs)
        update_classement(self)


class SeasonScore(models.Model):
    # if OneToOneField is used to link a season to a ligue it would make ligue unique
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE,
                              db_column='ligue', to_field='code_ligue')
    equipe = models.ForeignKey(
        Equipe, on_delete=models.CASCADE, db_column='equipe', to_field='id_federation')
    rank_ligue = models.IntegerField(null=True)
    match_played = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    draws = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    goals_for = models.IntegerField(null=True)
    goals_against = models.IntegerField(null=True)
    goal_diff = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    points_per_match = models.FloatField(null=True)

    def __str__(self):
        return f"SeasonScore for >> {self.ligue} << @ {self.equipe} "


def update_rank_ligue_all():
    ''' Mettre à jour le classement de toutes les ligues'''
    for l in Ligue.objects.all():
        update_rank_ligue(l)


def update_rank_ligue(l):
    '''Mettre à jour le classement de la ligue l
    l'ordre est fait par points, goal_diff, goals_for'''
    season_scores = SeasonScore.objects.filter(
        ligue=l).order_by('-points', '-goal_diff', '-goals_for')
    for i, season_score in enumerate(season_scores):
        season_score.rank_ligue = i+1
        season_score.save()


def createrow_season_score(e: Equipe):
    '''Créer une ligne de classement pour chaque ligue de l'équipe e'''
    #import ipdb; ipdb.set_trace()
    # check if ligue exists, it s a manytomany field
    # self.ligues.select_related() self.ligues.prefetch_related()
    for ligue in Equipe.objects.get(nom=e.nom).ligues.all():
        SeasonScore.objects.create(ligue=ligue,
                                   equipe=e,
                                   rank_ligue=0,
                                   match_played=0,
                                   wins=0,
                                   draws=0,
                                   losses=0,
                                   goals_for=0,
                                   goals_against=0,
                                   goal_diff=0,
                                   points=0,
                                   points_per_match=0
                                   )


def update_classement(current_match: Match):
    '''Mettre à jour le classement de la ligue du match courant le rank_ligue est calculé à la volée'''
    visiteur_score = {
        'match_played': models.F('match_played') + 1,
        'wins': models.F('wins') + 1 if current_match.score_visiteur > current_match.score_locaux else models.F('wins'),
        'draws': models.F('draws') + 1 if current_match.score_visiteur == current_match.score_locaux else models.F('draws'),
        'losses': models.F('losses') + 1 if current_match.score_visiteur < current_match.score_locaux else models.F('losses'),
        'goals_for': models.F('goals_for') + current_match.score_visiteur,
        'goals_against': models.F('goals_against') + current_match.score_locaux,
        'goal_diff': models.F('goal_diff') + current_match.score_visiteur - current_match.score_locaux,
        'points': models.F('points') + 3 if current_match.score_visiteur > current_match.score_locaux
        else models.F('points') + 1 if current_match.score_visiteur == current_match.score_locaux
        else models.F('points') + 0,
        'rank_ligue': 1,
        # 'points_per_match': 0
        'points_per_match': 0 if ((models.F('points') == 0) or (models.F('match_played') == 0)) else models.F('points') / models.F('match_played')
    }
    locaux_score = {
        'match_played': models.F('match_played') + 1,
        'wins': models.F('wins') + 1 if current_match.score_locaux > current_match.score_visiteur else models.F('wins'),
        'draws': models.F('draws') + 1 if current_match.score_locaux == current_match.score_visiteur else models.F('draws'),
        'losses': models.F('losses') + 1 if current_match.score_locaux < current_match.score_visiteur else models.F('losses'),
        'goals_for': models.F('goals_for') + current_match.score_locaux,
        'goals_against': models.F('goals_against') + current_match.score_visiteur,
        'goal_diff': models.F('goal_diff') + current_match.score_locaux - current_match.score_visiteur,
        'points': models.F('points') + 3 if current_match.score_visiteur > current_match.score_locaux
        else models.F('points') + 1 if current_match.score_visiteur == current_match.score_locaux
        else models.F('points') + 0,
        'rank_ligue': 1,
        # 'points_per_match': 0
        'points_per_match': 0 if ((models.F('points') == 0) or (models.F('match_played') == 0)) else models.F('points') / models.F('match_played')
    }
    SeasonScore.objects.filter(
        ligue=current_match.ligue,
        equipe=current_match.id_visiteur).update(**visiteur_score)
    SeasonScore.objects.filter(
        ligue=current_match.ligue,
        equipe=current_match.id_locaux).update(**locaux_score)
    update_rank_ligue_all()
