from django.urls import path, include
from .views import user_list, RegistrationView, UserLoginView, logout_view, ProfileEdit, ProfileView, MyProfileView
from .views import profile_list
#profile_edit  _view
#user_authentication_view#, login_user_view login_user_view

app_name = 'registration'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('user_authentication_view/', UserLoginView.as_view(), name='user_authentication_view'),
    path('profile_edit/<int:user_id>/', ProfileEdit.as_view(), name='profile_edit'),
    path('profile_view/<int:user_id>/', ProfileView.as_view(), name='profile_view'),
    path('my_profile/', MyProfileView.as_view(), name='my_profile'),
    #path('profile_edit/<int:user_id>/', profile_edit_view, name='profile_edit'),
    # path('registration/', UserAuthenticationView.as_view(), name='user_authentication_view'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('registration/', registration, name='registration'),
    #path('login/', login_user_view, name='login_user_view'),
    path('logout_view/', logout_view, name='logout_view'),
    #path('login/', user_authentication_view, name='user_authentication_view'),
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile_list/', profile_list, name='profile_list'),
    path('user_list/', user_list, name='user_list'),
]
