"""Todo URL Configuration

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
from django.urls import path
from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.create,name='create1'),
    path('delete/<int:task_id>',views.delete,name='delete1'),
    path('update/<int:id>',views.update,name='update1'),
    path('delete_complete',views.delete_complete,name='delete_c'),    
    path('delete_all',views.delete_all,name='delete_all1'),


]
