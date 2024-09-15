from django import forms
from posts.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]



class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField()
    image = forms.ImageField()

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title.lower() == "python":
            raise forms.ValidationError("такое название нельзя")
        else:
            return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower() == content.lower():
            raise forms.ValidationError("titles and content must be different")

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", 'content', 'image']

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title.lower() == "python":
            raise forms.ValidationError("такое название нельзя")
        else:
            return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower() == content.lower():
            raise forms.ValidationError("titles and content must be different")
