"""devs_pro URL Configuration

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
<<<<<<< HEAD
# hi
=======
# hello
>>>>>>> 6bc7b3e5aa8abfe9b0f30f99ac338d3bf6eb34b2
# how are you
from django.contrib import admin
from django.urls import path
from devs_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
