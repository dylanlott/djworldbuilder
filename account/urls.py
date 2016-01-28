from django.conf.urls import patterns, include, url 

urlpatterns = patterns('account.views', 
	url(r'', 'account', name='account_home')
)