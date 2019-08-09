from django.urls import path
from . import views
import profiles.views
urlpatterns = [
    path('mypage/',profiles.views.mypage, name='mypage'),      
]
