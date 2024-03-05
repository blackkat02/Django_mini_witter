from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from users.models import User
from .forms import PostForm

from comments.models import Comment
from comments.forms import CommentForm

from django.contrib import messages
from django.urls import reverse

# from django.contrib.auth.decorators import login_required


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'posts/add_post.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts, 'username': None})


def post_view(request, post_id=None):
    #user = get_object_or_404(User, id=user_id)
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
        #'user': user,
    }
    return render(request, 'posts/post_view.html', context)



def user_posts(request, user_id=None):
    user = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(user=user)
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'posts/user_posts.html', context)


