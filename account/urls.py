from django.conf.urls import patterns, include, url 

urlpatterns = patterns('account.views', 
	url(r'^home$', 'home', name='account_home')
)