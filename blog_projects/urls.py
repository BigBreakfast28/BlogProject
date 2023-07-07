"""Defines URL pattersn for blog_projects(apps)"""

from django.urls import path

from .import views

app_name = 'blog_projects'
urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('new_description/<int:blog_id>/', views.new_description, name='new_description'),
    path('edit_description/<int:description_id>/', views.edit_description, name='edit_description'),
    #Profiles 
    
]
