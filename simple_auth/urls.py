from django.conf.urls import patterns, include, url
# from django.contrib.admin import site
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^login/$', 'simple_auth.views.login_view'),
    url(r'^logout/$', 'simple_auth.views.logout_view'),
    url(r'^auth/$', 'simple_auth.views.auth_and_login'),
    url(r'^register/$', 'simple_auth.views.register'),
    url(r'^$', 'simple_auth.views.secured'),
    url(r'^language/(?P<lang>[a-z\-]+)/$', 'simple_auth.views.language'),
    url(r'^language/$', 'simple_auth.views.language'),
    # url(r'^admin/', include(site.urls)),
)
