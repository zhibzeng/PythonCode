from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'firstsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$','firstsite.view.hello',name='hello'),
    url(r'^time/$','firstsite.view.current_datetime',name='current_datetime'),
     url(r'^time/plus/(\d{1,2})/$', 'firstsite.view.hours_add',name='time-plus'),
    url(r'^.*$','firstsite.view.hello',name='hello'),
	 url(r'^testtemplate/$','firstsite.handle.timenow',name='template'),
)
