from django.shortcuts import render, HttpResponseRedirect, reverse

from datetime import datetime

from homepage.models import Post
from homepage.forms import AddPostForm


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        form.save()
        # if form.is_valid():
        #     data = form.cleaned_data
        #     new_post = Post.objects.create(
        #         is_boast=data.get('is_boast'),
        #         post_text=data.get('post_text'),
        #         up_votes=0,
        #         down_votes=0,
        #         submission_date=
        #     )
        return HttpResponseRedirect(reverse("homepage"))

    form = AddPostForm()
    return render(request, "generic_form.html", {"form": form})
