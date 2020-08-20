from django import forms
from homepage.models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["is_boast", "post_text"]
