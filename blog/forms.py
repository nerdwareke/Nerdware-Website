from django import forms
from .models import Comment, Post


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'body', 'status', 'tags']


class SearchForm(forms.Form):
    query = forms.CharField()

class SavePost(forms.ModelForm):
    title = forms.Textarea()
    slug = forms.Textarea()
    author = forms.Textarea()
    body = forms.Textarea()
    status = forms.ChoiceField(help_text = "Status Field is required.", choices = (('DF', 'Draft'), ('PB', 'Published')))

    def __init__(self, *args, **kwargs):
        super(SavePost, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ('author','title', 'slug', 'body','status','banner')
