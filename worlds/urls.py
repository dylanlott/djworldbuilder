from django.conf.urls import patterns, include, url 

urlpatterns = patterns('worlds.views', 
    url(r'^$', 'view_worlds', name='view_worlds'),
    url(r'^create$', 'create_world', name='create_world')
)