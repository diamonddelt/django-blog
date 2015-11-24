from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # in Python, writing a regex beginning with 'r'
    # signifies that the regex may have special characters
    # and that they are intended for the regex pattern itself
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
