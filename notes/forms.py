from .models import Note
from django import forms
from django.forms import TextInput

class NotesModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        current_title = self.cleaned_data.get('title')
        print(current_title)

        return current_title