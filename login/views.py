from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import get_object_or_404, render
from .models import User

def user_list(request):
    users = User.objects.all()
    template = loader.get_template("login/user_list.html")
    context = {"users": users}
    output = template.render(context, request)
    return HttpResponse(output)


def user_list_render(request) :
    users = User.objects.all()
    return render(request, "login/user_list.html", {"users": users})

class UserListView(ListView):
    model = User
    template_name = "login/user_list.html"
    context_object_name = "users"

class UserDetailView(DetailView):
    model = User
    template_name = "login/user_detail.html"
    context_object_name = "user"
