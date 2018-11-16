"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^sign-in/$',login, {'template_name': 'login.html'}, 'login'),
    url(r'^login/$',login, {'template_name': 'login.html'}, 'login'),
    url(r'^accounts/login/$',login, {'template_name': 'login.html'}, 'login'),
    url(r'^logout/$', logout_page),
    url(r'^registration/',registration),
    url(r'^customer_dashboard/',customer_dashboard),
    url(r'^product_view/',product_view),
    url(r'^cart_view/',cart_view),
    url(r'^cart_view_data/',cart_view_data),
    url(r'^login_status/',cart_view_data),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
