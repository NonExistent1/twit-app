from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    """Comment Form"""
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''
        

    class Meta:
        model = Comment
        fields = ("body",)