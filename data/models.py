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
    teamA = models.ForeignKey(Team, related_name='gameA')
    teamB = models.ForeignKey(Team, related_name='gameB')

    # their calculated score
    scoreTeamA = models.IntegerField()
    scoreTeamB = models.IntegerField()

    # duration in seconds
    duration = models.IntegerField()

    # game officials
    snitchRunner = models.ForeignKey(Person, related_name='+')

    headReferee       = models.ForeignKey(Person, related_name='+')
    snitchReferee     = models.ForeignKey(Person, related_name='+')
    assistantRefereeA = models.ForeignKey(Person, related_name='+')
    assistantRefereeB = models.ForeignKey(Person, related_name='+')


class Score(models.Model):
    timestamp = models.DateTimeField()
    scoreType = models.CharField(max_length=1, choices=SCORE_TYPES)
    team      = models.ForeignKey(Team)
    game      = models.ForeignKey(Game)
    player    = models.ForeignKey(Person)
