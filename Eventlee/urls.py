"""Eventlee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from ApplicationUsers import views
import ApplicationAdmin.views as view2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('contact/', views.Contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('adduser/',views.signup,name='appuser'),
    path('addevent/',view2.eventregister,name = "eventregisteration"),
    path('login/',views.login,name = "login")
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
