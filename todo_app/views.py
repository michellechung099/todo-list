from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView 
from .models import ToDoList, ToDoItem

# display a list of to-do list titles
class ListListView(ListView): 
    # data model class that you'd like to fetch
    model = ToDoList 
    # name of the template that will format the list into a displayable form
    template_name = "todo_app/index.html"

class ItemListView(ListView): 
    model = ToDoItem 
    template_name = "todo_app/todo_list.html"

    def get_queryset(self): 
        # kwargs stand for keyword arguments (convention used to pass a variable number of keyword arguments to a fn)
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
    
    def get_context_data(self): 
        # return value from this is template's context (Python dictionary that determines what data is available for rendering)

        # called first so that new data can be merged with existing context 
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context 
    








