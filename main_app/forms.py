from django import forms
from .models import Profile, Note

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content', 'date']