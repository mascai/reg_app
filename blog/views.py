from django.shortcuts import render
from django.contrib.auth.views import LoginView


def post_list(request):
    return render(request, 'blog/post_list.html', {})


class BBLoginView(LoginView):
    template_name = 'blog/post_list.html'
