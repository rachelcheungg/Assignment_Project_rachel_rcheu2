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

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data(**kwargs)

        q = self.request.GET.get("q")

        if q:
            search_qs = User.objects.filter(username__icontains=q)
            ctx["users"] = search_qs
        else:
            search_qs = None

        ctx["q"] = q
        ctx["search_results"] = search_qs

        ctx["total_users"] = User.objects.count()

        return ctx

class UserDetailView(DetailView):
    model = User
    template_name = "login/user_detail.html"
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"