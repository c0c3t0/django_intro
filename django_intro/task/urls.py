from django.urls import path

from django_intro.task.views import home

urlpatterns = (
    path('', home),
)