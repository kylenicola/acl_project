from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'acl_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^acl_app', include('acl_app.urls')),
    url(r'^cs373', include('cs373.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
