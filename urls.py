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
    url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^message/add/(?P<chat_id>\d{0,2})/$', 'chat.views.add_message'),
	url(r'^message/view/(?P<chat_id>\d{0,2})/$', 'chat.views.view_messages'),
	url(r'^chat/start/$', 'chat.views.start_chat'),
	url(r'^chat/view/(?P<chat_id>\d{0,2})/$', 'chat.views.view_chat'),
    url(r'^chat/view/list/$', 'chat.views.view_chat_list'),
    #url(r'^chat/take/$', 'chat.views.chat_take')
)
#(r'^accounts/', include('registration.backends.default.urls')),