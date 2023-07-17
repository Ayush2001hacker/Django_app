from django import forms

from .models import Post

class TaskForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Title', 'Description','start_date','end_date')