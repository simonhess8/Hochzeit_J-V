"""Hochzeit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from geschenke import views as views_g
from homepage import views as views_h

urlpatterns = [
    path('', views_h.home, name='home'),
    path('admin/', admin.site.urls),
    path('geschenke/', views_g.home, name='geschenke'),
    path('rückmeldung/', views_h.rückmeldung, name='rückmeldung'),
    path('infos/', views_h.infos, name='infos'),
    path('galerie/', views_h.galerie, name= 'galerie'),

        #Authentification
    path("signup/", views_h.signupuser, name="signupuser"),
    path("logout/", views_h.logoutuser, name="logoutuser"),
    path("login/", views_h.loginuser, name="loginuser"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)