from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This points to the index view function
]
