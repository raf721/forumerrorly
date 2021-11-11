from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    """Allows users to create a new thread."""
    class Meta:
        model = Thread
        fields = ['text']
        labels = {'text': ''}

class PostForm(forms.ModelForm):
    """Allows users to create a new post."""
    class Meta:
        model = Post
        fields = ['text']
        labels = {'text': 'Post:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}   # use HTML widget for text box