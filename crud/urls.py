"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import settings
from django.conf.urls.static import static
from crudApp.views import * 
from crudApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,views.home,name="home"),
    path('game_charecters/' ,create_List.as_view(),name="get_create"),
    path('game_charecters/<int:id>' ,get_delete_update.as_view(),name="get_delete_update"),
    path('get_game_charecters/' ,views.search_by_name,name="get_create"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

