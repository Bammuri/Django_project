from django.db import models

# For priority_flag
DEFAULT = 0
LOW = 1
NORMAL = 2
HIGH = 3
PRIORITIES = (
    (DEFAULT, ''),
    (LOW, 'Low'),
    (NORMAL, 'Normal'),
    (HIGH, 'High'),
)

# Create your models here.
class Todo(models.Model):

    text = models.CharField(max_length=32)
    content = models.TextField(max_length=32)
    dueDate = models.DateField(null=True, blank=True)
    priority_flag = models.IntegerField(default=0, choices=PRIORITIES)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text