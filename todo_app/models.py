from django.utils import timezone
from django.db import models
# obtain URL path as a string from given view name and optional parameters
# instead of hardcoding URLs in your views and templates, you use the name of the URL pattern and optionally any args to resolve the URL
from django.urls import reverse

# utility function for setting ToDoItem default due dates 
def one_week_hence(): 
    return timezone.now() + timezone.timedelta(days=7)

# extends django.db.models.Model superclass 
class ToDoList(models.Model): 
    # define data fields in model 
    title = models.CharField(max_length=100, unique=True)

    # constructs a URL for individual to-do list 
    # self.id: auto generated unique identifier for each object
    def get_absolute_url(self): 
        return reverse("list", args=[self.id])
    
    # returns a string representation of an object
    def __str__(self): 
        return self.title

# linked to a particular list
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    # auto set .created_date to the current date the first time ToDoItem object is saved 
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    # links ToDoItem back to its ToDoList (one-to-many relationship)
    # on_delete: ensures if to-do list is deleted, all associated to-do item will be deleted as well 
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    # returns URL for particular data item 
    def get_absolute_url(self): 
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )
    
    def __str__(self): 
        return f"{self.title}: due {self.due_date}"
    
    # set a default ordering for ToDoItem records 
    class Meta: 
        ordering = ["due_date"]
    


