from django.urls import path
from . import views
from .views import BBLoginView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
]