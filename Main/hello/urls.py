from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("asd",views.pagal,name="pagal"),
    path("<str:name>",views.greet,name="greet"),
    path("prakhar",views.prakhar,name="prakhar"),
]