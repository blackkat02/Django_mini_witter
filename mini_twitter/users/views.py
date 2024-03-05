from django.shortcuts import render, get_object_or_404
from users.models import User
from .forms import UserForm

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_info(request, user_id=None):
    user = get_object_or_404(User, pk=user_id)
    context = {
        'user': user,
        # Додайте будь-які інші дані про користувача, які ви хочете відобразити
    }
    return render(request, 'users/user_info.html', context)



