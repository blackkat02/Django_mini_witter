from django.shortcuts import render, get_object_or_404, redirect
from registration.models import CustomUser
#from .forms import CustomUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

#from django.views.generic import TemplateView


#class CsrfFailureView(TemplateView):
#    template_name = 'users/fault.html'


# class RegisterView(CreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'register.html'
#     success_url = 'users/user_list'
#
#     def form_valid(self, form):
#         # Створюємо користувача на основі даних з форми
#         user = form.save()
#         # Увійшовши користувача у систему після реєстрації
#         login(self.request, user)
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         # Повертаємо URL, на який ми хочемо перенаправити користувача після реєстрації
#         return reverse_lazy('users/user_list.html')
#
#
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
# from django.views.generic import FormView
# from .forms import CustomAuthenticationForm
#
#
# class CustomLoginView(LoginView):
#     form_class = CustomAuthenticationForm
#     template_name = 'login.html'
#     success_url = reverse_lazy('users/user_list.html')  # Замініть 'success_url_name' на ім'я вашого успішного URL

    # def form_valid(self, form):
    #     # Додайте власний код, який виконується, якщо форма є дійсною
    #     # Наприклад, ви можете виконати власні дії перед перенаправленням на успішну сторінку
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     # Додайте власний код, який виконується, якщо форма недійсна
    #     # Наприклад, ви можете відобразити додаткові повідомлення про помилки на сторінці входу
    #     return super().form_invalid(form)


@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_info(request, user_id=None):
    user = get_object_or_404(CustomUser, pk=user_id)
    context = {
        'user': user,
        # Додайте будь-які інші дані про користувача, які ви хочете відобразити
    }
    return render(request, 'users/user_info.html', context)



