"""HealthRoutine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import routine
import loginsystem


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', routine.views.create_view),
    path('list/', routine.views.list_view),
    path('<int:post_id>/delete/', routine.views.delete_view),
    path('<int:post_id>/update/', routine.views.update_view),
    path('signIn/', loginsystem.views.signIn_view),
    path('signUp/',loginsystem.views.signUp_view),
    path('logout/',loginsystem.views.logout_view),
]