from django import forms
from .models import Goal, Note

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content', 'date']