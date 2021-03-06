"""rapidtaskbackend URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

api_urls = [
    url(r'^v0.1/', include('rapidtaskbackend.api.v0-1.subscriptions.urls')),
]

urlpatterns = [
    # url patterns with honey-pot admin page
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    # Django Admin access url
    url(r'^rapidtaskadminaccess/', admin.site.urls),

    # Rest Framework
    url(r'^', include(api_urls)),
]
