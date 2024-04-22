from django.contrib import *
from django.urls import *
from .views import *

app_name="users"

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]