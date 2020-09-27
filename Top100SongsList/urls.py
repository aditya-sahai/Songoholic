from django.urls import path
from . import views


urlpatterns = [
    path('', views.top_100, name="top-100"),
]
