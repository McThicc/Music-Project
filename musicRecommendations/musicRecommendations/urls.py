"""
URL configuration for musicRecommendations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# ^ Should I take that out?

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #I only have one "app" at the moment so there's not much to do here
    path("songs/", include("songs.urls")),
    path("users/", include("users.urls")),
    path('admin/', admin.site.urls),
]
