from django.db import models

SCORE_TYPES = (
    ('H' , 'Hoop')  ,
    ('S' , 'Snitch') ,
)

class League(models.Model):
    name = models.CharField(max_length = 64)
    code = models.CharField(max_length = 3)
    def __unicode__(self):
        return self.name + " (" + self.code + ")"


class Team(models.Model):
    name   = models.CharField(max_length = 32)
    league = models.ForeignKey(League)
    def __unicode__(self):
        return self.name


class Person(models.Model):
    name  = models.CharField(max_length = 32)
    email = models.EmailField()
    team  = models.ForeignKey(Team)
    def __unicode__(self):
        return self.name


class Game(models.Model):
    # teams
    team_a = models.ForeignKey(Team, related_name='gameA')
    team_b = models.ForeignKey(Team, related_name='gameB')

    # their calculated score
    score_team_a = models.IntegerField()
    score_team_b = models.IntegerField()

    # duration in seconds
    duration = models.IntegerField()

    # game officials
    snitch_runner = models.ForeignKey(Person, related_name='+')

    head_referee        = models.ForeignKey(Person, related_name='+')
    snitch_referee      = models.ForeignKey(Person, related_name='+')
    assistant_referee_a = models.ForeignKey(Person, related_name='+')
    assistant_referee_b = models.ForeignKey(Person, related_name='+')
    def __unicode__(self):
        return self.team_a.name + " vs. " + self.team_b.name


class Score(models.Model):
    timestamp = models.DateTimeField()
    score_type = models.CharField(max_length=1, choices=SCORE_TYPES)
    team      = models.ForeignKey(Team)
    game      = models.ForeignKey(Game)
    player    = models.ForeignKey(Person)
    def __unicode__(self):
        return player.name + ": " + scoreType
