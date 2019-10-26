from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth . decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def post_list(request):
    return render(request, 'blog/post_list.html', {})


class BBLoginView(LoginView):
    template_name = 'blog/login.html'

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'blog/logout.html'

@login_required
def profile(request):
    return render(request, 'blog/profile.html')