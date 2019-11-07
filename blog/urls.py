from django.urls import path
from . import views
from .views import BBLoginView, BBLogoutView, profile, RegisterUserView, RegisterDoneView, ChangeUserInfoView, user_activate

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),

    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('account/profile/change/', ChangeUserInfoView.as_view(), name='profile_change')

]