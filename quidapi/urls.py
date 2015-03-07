from django.conf.urls import patterns, include, url
from django.contrib import admin
from quidapi.views import Index, Games, Teams

from rest_framework import routers
from quidapi.api import LeagueViewSet, TeamViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'leagues' , LeagueViewSet)
router.register(r'teams'   , TeamViewSet)

urlpatterns = patterns('' ,
    url(r'^$'      , Index.as_view() , name='index') ,
    url(r'^games/' , Games.as_view() , name='games') ,
    url(r'^teams/' , Teams.as_view() , name='teams') ,
)

urlpatterns += [
    url(r'^admin/'    , include(admin.site.urls))     ,
    url(r'^api/'      , include(router.urls))         ,
    url(r'^api-auth/' , include('rest_framework.urls' , namespace='rest_framework'))
]
