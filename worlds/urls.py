from django.conf.urls import patterns, include, url 

urlpatterns = patterns('worlds.views', 
    url(r'', '', name='view_worlds')
)