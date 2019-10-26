from django.urls import path
from . import views
from .views import BBLoginView, BBLogoutView, profile

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
]