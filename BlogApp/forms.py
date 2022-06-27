from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget





class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ("title", "subtitle", "author", "image", "content")