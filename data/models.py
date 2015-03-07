from django.db import models

SCORE_TYPES = (
    ('H' , 'Hoop')  ,
    ('S' , 'Snitch') ,
)

class League(models.Model):
    name = models.CharField(max_length = 64)
    code = models.CharField(max_length = 3)


class Team(models.Model):
    name   = models.CharField(max_length = 32)
    league = models.ForeignKey(League)


class Person(models.Model):
    name  = models.CharField(max_length = 32)
    email = models.EmailField()
    team  = models.ForeignKey(Team)


class Game(models.Model):
    # teams
    team_a = models.ForeignKey(Team)
    team_b = models.ForeignKey(Team)

    # their calculated score
    score_team_a = models.IntegerField()
    score_team_b = models.IntegerField()

    # duration in seconds
    duration = models.IntegerField()

    # game officials
    snitch_runner = models.ForeignKey(Person)

    head_referee        = models.ForeignKey(Person)
    snitch_refree       = models.ForeignKey(Person)
    assistant_referee_a = models.ForeignKey(Person)
    assistant_referee_b = models.ForeignKey(Person)


class Score(models.Model):
    timestamp  = models.DateTimeField()
    score_type = models.CharField(max_length=1, choices=SCORE_TYPES)
    team       = models.ForeignKey(Team)
    game       = models.ForeignKey(Game)
    player     = models.ForeignKey(Player)
