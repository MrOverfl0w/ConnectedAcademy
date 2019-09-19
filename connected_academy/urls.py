"""connected_academy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='home'), name='home'),
    url(r'^home', views.Main, name='home'),
    url(r'^Authlogin', auth_views.login, {'template_name': 'LogIn.html'}, name='AuthLogIn'),
    url(r'^login', views.LogIn, name='LogIn'),
    url(r'^signup', views.SignUp, name='signup'),
    url(r'^check', views.check, name='check'),
    url(r'^logout', auth_views.logout, {'template_name': 'LogOut.html'}, name='logout'),
    url(r'^accounts/profile/', RedirectView.as_view(url='https://connected-academy-mr-overfl0w.c9users.io/check'), name='profile')
]
