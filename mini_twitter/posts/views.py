from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from registration.models import CustomUser
from .forms import PostForm

from django.views.generic import View
from django.contrib.contenttypes.models import ContentType
from .models import Like
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assign the currently logged-in user object to the post
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts, 'username': None})


def post_view(request, post_id=None):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_view.html', context)



def user_posts(request, user_id=None):
    user = get_object_or_404(CustomUser, id=user_id)
    posts = Post.objects.filter(user=user)
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'posts/user_posts.html', context)




class LikeView(View):
    def post(self, request, post_id):
        # Get the post object based on the post_id
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            # Handle the case where the post does not exist
            return redirect('http://127.0.0.1:8000/posts/post_list/')  # Redirect to the post list page or any other appropriate page

        # Create or get a Like object for the current user and the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        # Increment the likes count of the post if a new like is created
        if created:
            #post.likes_count += 1
            post.save()

        # Redirect the user back to the post list page
        return redirect('http://127.0.0.1:8000/posts/post_list/')


# def post_edit(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_view', post_id=post.id)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'posts/post_edit.html', {'form': form, 'post': post, 'post_id': post_id})



@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # Check if the current user is the author of the post
    if request.user != post.user:
        raise Http404("You are not authorized to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_view', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form, 'post': post, 'post_id': post_id})
