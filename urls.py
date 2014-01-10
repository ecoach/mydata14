from django.conf.urls.defaults import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

hardmsg_patterns = patterns('',
    url(r'^home/',  login_required(home_view), name='home'),
    url(r'^',  login_required(home_view), name='default'),
)

mts_patterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),

    # staff apps
    url(r'^staff/',         include('mytournament15.urls', namespace='mystaff')),
    #url(r'^staff/',         include('mypublisher.urls', namespace='mystaff')),
    #url(r'^publisher/',     include('mypublisher.urls', namespace='mypublisher')),
    #url(r'^upload/',        include('myloader.urls', namespace='myloader')),
    #url(r'^export/',        include('myexporter.urls', namespace='myexporter')),
    #url(r'^nts/',           include('nts.urls', namespace='nts')),
    url(r'^emailer/',       include('myemailer.urls', namespace='myemailer')),
    #url(r'^copycat/',       include('mycopycat.urls', namespace='mycopycat')),
    #url(r'^curator/',       include('mycurator.urls', namespace='mycurator')),
    #url(r'^usage/',         include('myusage.urls', namespace='myusage')),
    url(r'^logger/',        include('mylogger.urls', namespace='mylogger')),
    url(r'^tournament/',    include('mytournament15.urls', namespace='tourney')),
    url(r'^download_mysql_db/', login_required(Download_Mysql_View), name='download_mysql'), # hack for now

    # message project
    #url(r'^',               redirect_to, {'url': '/tournament/'})
    #??url(r'^home/',          login_required(home_view), name='home'),
    #url(r'^',               login_required(home_view), name='default'),
    url(r'^',               include(hardmsg_patterns, namespace='default')),
    #url(r'^',               include('mycoach.urls', namespace='mycoach')),
)

urlpatterns = patterns('',
    url(r'^coach14/',          include(mts_patterns)),
    #url(r'^coach14/',          include(mts_patterns), name='mydata'),
    url(r'^coaches/',       include('myselector.urls', namespace='myselector')),
    #url(r'^',               redirect_to, {'url': '/coaches/'})
    #url(r'^',               redirect_to, {'url': '/coach14/'})
    url(r'^',               RedirectView.as_view(url='/coach14/')),

)

