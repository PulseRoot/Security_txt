from django.urls import path
from .views import *
from . import views

app_name="parsing"
urlpatterns = [
    path('',views.viruslistView.as_view()),
]