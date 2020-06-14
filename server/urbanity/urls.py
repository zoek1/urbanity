"""firey_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path

from availability.views import create_POI, create_availability, create_feature, get_feature, get_availability, \
    list_POIs

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path(r'api/v0/poi/', create_POI),
    path(r'api/v0/poi/availability/', create_availability),
    path(r'api/v0/poi/features/', create_feature),
    re_path(r'api/v0/poi/(?P<pk>\d+)/features/', get_feature),
    re_path(r'api/v0/poi/(?P<pk>\d+)/availability/', get_availability),
    path(r'api/v0/POI', list_POIs)
]
