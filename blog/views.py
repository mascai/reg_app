from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth . decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AdvUser
from .forms import RegisterUserForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .utilities import signer

def post_list(request):
    return render(request, 'blog/post_list.html', {})


class BBLoginView(LoginView):
    template_name = 'blog/login.html'

class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'blog/logout.html'

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'blog/register_user.html'
    form_class = RegisterUserForm
    success_url = '/register_done'

class RegisterDoneView(TemplateView):
    template_name = "blog/register_done.html"


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except:
        return render(request, 'blog/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'blog/user_is_activated.html'
    else:
        template = 'blog/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)