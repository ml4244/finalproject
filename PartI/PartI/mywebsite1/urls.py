"""mywebsite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from user import views

from django.views import static
from django.conf import settings

urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),

    url(r'^map', views.to_map),
    url(r'sightings/stats', views.to_sightings_stats),
    url(r'sightings/query_data', views.query_data),
    url(r'^sightings', views.to_sightings),
    url(r'^query_data', views.query_data),
    url(r'^query_all_points', views.query_all_points),
    url(r'^$', views.to_sightings),
    path('admin/', admin.site.urls),
]
