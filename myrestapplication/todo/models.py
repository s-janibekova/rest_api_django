from django.db import models

# Create your models here.
class TodoItem(models.Model):
    text = models.CharField(max_length=250)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'Todo {self.text} ({"" if self.done else "not"} done)'