from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('api/todos', views.ToDoListView.as_view())
]