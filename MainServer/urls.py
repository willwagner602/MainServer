"""MainServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('LandingPage.urls', namespace='LandingPage')),
    url(r'^admin', include(admin.site.urls)),
    url(r'^thud/', include('Thud.urls', namespace='Thud')),
    url(r'^thu2d', include('Thu2d.urls', namespace='Thu2d')),
    url(r'^jobs/', include('PyJobsDjango.urls', namespace='PyJobsDjango.py')),
    # url(r'^weblog/', include('zinnia.urls')),
    # url(r'^comments/', include('django_comments.urls')),
]