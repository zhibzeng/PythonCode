# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^bloglist/$', 'blog.views.blog_list', name='bloglist'),
    url(r'^blog/(?P<id>\d+)/$', 'blog.views.blog_show', name='detailblog'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'F:/GitRepository/PythonCode/Django/myblog/static'}),
    url(r'^blog/tag/(?P<id>\d+)/$', 'blog.views.blog_filter', name='filtrblog'),
    url(r'^blog/add/$', 'blog.views.blog_add', name='addblog'),
    url(r'^blog/(?P<id>\w+)/update/$', 'blog.views.blog_update', name='updateblog'),
    url(r'^blog/(?P<id>\w+)/del/$', 'blog.views.blog_del', name='delblog'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/$','blog.views.blog_list',name='blogmain'),
)
