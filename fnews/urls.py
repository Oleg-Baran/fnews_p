"""fnews URL Configuration

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
from django.contrib import admin
from django.urls import path, include #Add some apps urls
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from blog import schema

#Main urls
urlpatterns = [
    path('blog/', include('blog.urls')), #For find articles URL! 
    path('grappelli/', include('grappelli.urls')), #Design our admin panel
    path('admin/', admin.site.urls), #url our admin
    path('graphql/', GraphQLView.as_view(graphiql=True)),  #APIcalls
    path('', include('social_django.urls', namespace='social')), #For autintification users
]
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
