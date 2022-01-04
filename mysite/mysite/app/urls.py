from typing import Pattern
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('',views.loginUser, name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('signup',views.signup,name="signup"),
    # path('loggedin',views.loggedin,name="loggedin"),
]