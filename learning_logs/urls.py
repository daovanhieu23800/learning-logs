"""define urls pattern for learing logs"""
#from django import urls
#from django.conf.urls import  as url
from django.urls import path, include

from learning_logs.models import Topic
from . import views
urlpatterns = [
    #homepage
    path ('', views.index, name='index'),
    #topics page
    path ('topics/', views.topics, name='topics'),
    #topic detail page
    path ('topics/<int:topic_id>/', views.topic, name='topic'),
    #create topic page
    path ('new_topic/', views.new_topic, name='new_topic'),
    #create new entru
    path ('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #edting entries
    path ('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
]
