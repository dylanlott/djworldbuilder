"""djworldbuilder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account', include('account.urls')),
    url(r'^worlds', include('worlds.urls')),
    url(r'^$', 'main.views.home', name="worldbuilder_home"), 
    url(r'^blog/', include('blog.urls')), 
]

urlpatterns += patterns(
	'django.contrib.auth.views', 

	url(r'^login/$', 'login',
		{'template_name': 'templates/login.html'},
		name='worldbuilder_login'),

	url(r'^logout/$', 'logout', 
		{'next_page': 'worldbuilder_home'},
		name="worldbuilder_logout"),
    
)