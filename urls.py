from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from myapp.views import index
from blog.models import Post
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),
    url(r'^$',index),
    url(r'^blog/$',ListView.as_view(model=Post)),
    url(r'^blog/(?P<id>/d+)/$',DetailView.as_view(model=Post)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
