from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account', include('account.urls')),
    url(r'^worlds/', include('worlds.urls')),
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
