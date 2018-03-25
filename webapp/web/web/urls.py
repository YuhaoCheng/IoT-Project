"""web URL Configuration

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
from console import views as console_views

urlpatterns = [
    url(r'^$',console_views.home,name='home'),
    #url(r'index.html',console_views.home),
    url(r'help.html',console_views.help),
    url(r'^retrieve.html',console_views.retrieve),
    url(r'analyze.html',console_views.analyze),
    url(r'^admin/', admin.site.urls),
    url(r'^ajax_data/$',console_views.ajax_data, name='ajax_data'),
]
