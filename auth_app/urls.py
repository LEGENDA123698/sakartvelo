from django.urls import path
from auth_app import views
from booking_app import *

urlpatterns = [
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register, name = "register"),
    path('profile/', views.profile_menu, name='profile-menu'),
    path('profile/info/', views.ProfileInfoView.as_view(), name="profile-info"),
    path('profile/edit/', views.UserProfileUpdateView.as_view(), name='edit-profile-info')
]