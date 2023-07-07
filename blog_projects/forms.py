from django import forms

from .models import BlogPost, Description

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title']
        labels = {'text':''}

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
        