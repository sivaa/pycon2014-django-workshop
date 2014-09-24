from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fav.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    # Demo
    url(r'^hello1/', 'demo.views.hello1'),
    url(r'^hello2/', 'demo.views.hello2'),
    url(r'^hello3/', 'demo.views.hello3'),
    url(r'^hello4/', 'demo.views.hello4'),
    url(r'^hello5/', 'demo.views.hello5'),
	url(r'^hello6/', 'demo.views.hello6'),
	url(r'^hello7/', 'demo.views.hello7'),

    # Movie
    url(r'^movies/$', 'movie.views.movies'),

    url(r'^movie/remove/(?P<movie_id>\d+)/$', 'movie.views.remove_movie'),
)
