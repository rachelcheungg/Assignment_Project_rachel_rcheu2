from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.shortcuts import render
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

# I asked chatgpt for help here to make sure the data showed on the website
class UserListView(ListView):
    model = User
    template_name = "login/user_list.html"
    context_object_name = "users"
