from django import forms
from .models import Post
from pyuploadcare.dj.forms import ImageField

class PostForm(forms.ModelForm):
    cover = ImageField(label='Photo')
    class Meta:
        model = Post
        fields = ('title', 'content', 'cover')
        
