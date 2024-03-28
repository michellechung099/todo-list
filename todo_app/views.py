from django.views.generic import ListView 
from .models import ToDoList 

# display a list of to-do list titles
class ListListView(ListView): 
    # data model class thata you'd like to fetch
    model = ToDoList 
    # name of the template that will format the list into a displayable form
    template_name = "todo_app/index.html"






