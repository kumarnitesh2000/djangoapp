from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name="index"),
    path('addtodo/',views.addtodo,name="addtodo"),
    path('deletetodo/<int:todo_id>/',views.deletetodo,name="deletetodo"),
]
