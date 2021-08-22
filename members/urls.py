from django.urls import path 
from .views import UserRegisterView , UserEditView ,PasswordsChangeView , ShowProfilePageView ,EditProfilePageView , CreateProfilePageViwe
#from django.contrib.auth import views as auth_views
from . import views

app_name = "members"
urlpatterns = [
    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/' , auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password'),
    path('password/',  PasswordsChangeView.as_view(template_name='registration/change-password.html'),name='password'),
    path('password_success/', views.password_success , name='password_success'),
    path('<int:pk>/profile/' ,  ShowProfilePageView.as_view() , name='show_profil_page'),
    path('<int:pk>/edit_profile_page/' ,EditProfilePageView.as_view() , name='edit_profil_page'),
    path('create_profil_page/' ,  CreateProfilePageViwe.as_view() , name='create_profil_page'),


    ###################### admin mastar ##############

 


]