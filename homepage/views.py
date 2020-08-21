from django.shortcuts import render, HttpResponseRedirect, reverse

from datetime import datetime

from homepage.models import Post
from homepage.forms import AddPostForm


def index(request):
    posts = Post.objects.all().order_by('-submission_date')
    return render(request, "index.html", {"posts": posts})


def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddPostForm()
    return render(request, "generic_form.html", {"form": form})


def add_upvote(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    post.up_votes += 1
    post.save()
    return HttpResponseRedirect(reverse("homepage"))


def add_downvote(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    post.down_votes -= 1
    post.save()
    return HttpResponseRedirect(reverse("homepage"))


def filter_boasts(request):
    boasts = Post.objects.filter(is_boast=True)
    return render(request, "index.html", {"posts": boasts})


def filter_roasts(request):
    roasts = Post.objects.filter(is_boast=False)
    return render(request, "index.html", {"posts": roasts})
