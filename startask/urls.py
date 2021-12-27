from django.contrib import admin
from django.urls import path
from startask.views import mainpage, tasks

urlpatterns = [
    path('', tasks),
]
