from django.urls import path
from . import views

urlpatterns=[

path("",views.index),
path("destroy_session",views.clear),
path("add_two",views.add2),
path("add",views.add_by),


]