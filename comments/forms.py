from django import forms
from django.forms import TextInput

from comments.models import Comment
from comments.widgets import StarRatingWidget


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    rating = forms.IntegerField(widget=StarRatingWidget, min_value=1, max_value=5)
    class Meta:
        model = Comment
        fields = ('content', 'rating')
