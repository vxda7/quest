"""quest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('<int:id>/like/', views.like, name="like"),
    path('<int:id>/comment_create', views.comment_create, name="comment_create"),
    path('<int:id>/update', views.update, name="update"),
    path('<int:id>/comment_delete', views.comment_delete, name="comment_delete"),
]
