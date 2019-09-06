from django import forms 
from myapp.todo.models import Todo

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

class TodoForm(forms.ModelForm):
    priority_flag = forms.TypedChoiceField(choices=PRIORITIES, widget=forms.Select)
    class Meta:
        model = Todo
        fields = ['text','content','dueDate','priority_flag']

        widgets={'text':forms.TextInput(attrs={"placeholder":'Add Title...'}),
                 'content':forms.TextInput(attrs={"placeholder":'Add content ...'}),
                 'dueDate':forms.DateInput(format=('%Y-%m-%d'), attrs={"placeholder":'Input a due date..(ex:YYYY-MM-DD) If no need, keep blank'})}