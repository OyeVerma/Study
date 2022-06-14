from django import forms
from .models import *

class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = "__all__"

        widgets = {
            'title':forms.TextInput(attrs={'autocomplete':'new-password'}),
            'text':forms.Textarea(attrs={'cols':30, 'autocomplete':'new-password'}),
        }
