from django.shortcuts import render, get_object_or_404, redirect
from .models import Follower
#from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from registration.models import UserProfile
#from django.http import Http404
from django.views.generic import View


@login_required
def following_list(request, user_id=None):
    user_profile = get_object_or_404(UserProfile, user__id=user_id)
    following_users = user_profile.following.all()
    return render(request, 'follower_list.html', {'following_users': following_users})



@login_required
def follower_list(request, user_id=None):
    user_profile = get_object_or_404(UserProfile, user__username=user_id)
    follower_user = user_profile.follower.all()
    return render(request, 'following_list.html', {'follower_user': follower_user})


from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Follower

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(get_user_model(), pk=user_id)

    # Check if the user is already being followed
    if request.user.profile.following.filter(pk=user_id).exists():
        # User is already being followed, handle this case (e.g., display a message)
        pass
    else:
        # Create a new follow relationship
        Follower.objects.create(user=request.user, followed_user=user_to_follow)

    # Redirect back to the user profile or any other appropriate page
    return redirect('profile_view', username=user_to_follow.username)



# @login_required
# def follow_user(request, user_id):
#     if request.method == 'POST':
#         user = UserProfile.objects.get(pk=user_id)
#         request.user.profile.following.add(user)
#         return redirect('registration:profile_view', user_id=user_id)

# def follow_user(request, user_id):
#     if request.method == 'POST':
#         user = UserProfile.objects.get(pk=user_id)
#         request.user.profile.following.add(user)
#         # Redirect to user profile after successful follow
#         return redirect('user_profile', user_id=user_id)

# class FollowUser(View):
#     def post(self, request, post_id):
#         # Get the post object based on the post_id
#         try:
#             post = UserProfile.objects.get(pk=post_id)
#         except UserProfile.DoesNotExist:
#             # Handle the case where the post does not exist
#             return redirect('http://127.0.0.1:8000/posts/post_list/')  # Redirect to the post list page or any other appropriate page
#
#         # Create or get a Like object for the current user and the post
#         like, created = UserProfile.objects.get_or_create(user=request.user, post=post)
#
#         # Increment the likes count of the post if a new like is created
#         if created:
#             #post.likes_count += 1
#             post.save()
#         return redirect('http://127.0.0.1:8000/posts/post_list/')