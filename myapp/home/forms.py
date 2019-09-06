from django import forms 
from myapp.todo.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text','content']

        widgets={'text':forms.TextInput(attrs={"placeholder":'Add Title...'}),'content':forms.TextInput(attrs={"placeholder":'Add content ...'})}
