from django.views.generic import View
from django.shortcuts import render_to_response
from data.models import League, Team, Person, Game

class Index(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['leagues'] = League.objects.count()
        context['teams'] = Team.objects.count()
        context['players'] = Person.objects.count()
        context['games'] = Game.objects.count()
        return render_to_response("index.html", context)


class Games(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['games'] = Game.objects.all()
        return render_to_response("games.html", context)


class Teams(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['teams'] = Team.objects.all()
        return render_to_response("teams.html", context)
