from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from registration.models import CustomUser
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from posts.forms import PostForm
from registration.forms import CustomUserCreationForm



@login_required
def add_comment_form(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # Set the user and post ID before saving the comment
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post_id = post_id
            comment.save()
            return redirect('comment_list')
    else:
        form = CommentForm()

    return render(request, 'comments/add_comment_form.html', {'form': form})


# @login_required
# def add_comment_form(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('comment_list')
#     else:
#         form = CommentForm()
#
#     return render(request, 'comments/add_comment_form.html', {'form': form})


#
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comments/comment_list.html', {'comments': comments})


def comment_list_for_user(request, user_id=None):
    """

    :type user_id: object
    """
    user = get_object_or_404(CustomUser, id=user_id)
    comments = Comment.objects.filter(user_id=user_id)
    return render(request, 'comments/comment_list_for_user.html', {'comments': comments})


def comment_list_for_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = post.comment_set.all()  # Assuming you have a ForeignKey from Comment to Post
        return render(request, 'comments/comment_list_for_post.html', {'post': post, 'comments': comments})
    except Post.DoesNotExist:
        return render(request, 'comments/comment_list_for_post.html', {'error_message': 'The post does not exist.'})
    except CustomUser.DoesNotExist:
        return render(request, 'comments/comment_list_for_post.html', {'error_message': 'The user does not exist.'})
    except ValueError:
        return render(request, 'comments/comment_list_for_post.html', {'error_message': 'Invalid post ID.'})


def edit_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/edit_comment.html', {'form': form, 'comment': comment})


def delete_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment_list')

    return render(request, 'comments/delete_comment.html', {'comment': comment})

