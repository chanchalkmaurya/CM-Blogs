from django import forms
from .models import Blog


class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }