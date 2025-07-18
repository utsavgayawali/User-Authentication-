"""
URL configuration for userauth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('main.urls')),
    # so when after doing this when if had url just  http://127.0.0.1:8000/ it automatically render it to register page it is need for deployment 
     path('', RedirectView.as_view(url='/register/',permanent=False)),
     path('accounts/', include('django.contrib.auth.urls')),
]
