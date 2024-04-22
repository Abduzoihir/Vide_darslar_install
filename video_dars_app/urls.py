from django.urls import path
from .views import *

app_name='video_dars_app'

urlpatterns = [
    path('',home,name='home'),
    path('lesson/<str:title>/',mavzular,name='mavzular'),
]
