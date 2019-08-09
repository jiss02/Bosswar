from django.contrib import admin
from django.urls import path
import idea.views

urlpatterns = [
    
    path('', idea.views.ideaboard, name='ideaboard'),
    path('ideanew/', idea.views.ideanew, name='ideanew'),
    path('ideashow/<int:idea_id>', idea.views.ideashow, name='ideashow'),
    path('ideaedit/', idea.views.ideaedit, name='ideaedit'),
    path('ideacreate/', idea.views.ideacreate, name='ideacreate'),
    path('ideaupdate/', idea.views.ideaupdate, name='ideaupdate'),
    path('ideadelete/<int:idea_id>', idea.views.ideadelete, name='ideadelete'),
    
]
