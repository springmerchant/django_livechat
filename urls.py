from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_livechat.views.home', name='home'),
    # url(r'^django_livechat/', include('django_livechat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^add/(?P<chat_id>\d{0,2})/$', 'chat.views.message'),
	url(r'^messages/(?P<chat_id>\d{0,2})/$', 'chat.views.view_messages'),
	url(r'^start/$', 'chat.views.start_chat_from')
)

