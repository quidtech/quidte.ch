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
