from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView,
)
from .models import ToDoList, ToDoItem
from django.urls import reverse 

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
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
    
    def get_context_data(self): 
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context 

class ListCreate(CreateView): 
    model = ToDoList 
    fields = ["title"]
    
    def get_context_data(self):
        context = super(ListCreate, self).get_context_data() 
        context["title"] = "Add a new list"
        return context


    









