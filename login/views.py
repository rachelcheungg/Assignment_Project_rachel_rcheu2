from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import get_object_or_404, render
from .models import User
from django.db.models import Count, Q

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

        ctx["websites_per_user"] = (
            User.objects
            .annotate(n_favourites=Count("favorites"))
            .order_by("n_favourites")
        )

        return ctx

class UserDetailView(DetailView):
    model = User
    template_name = "login/user_detail.html"
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"


from django.shortcuts import render, redirect
from .forms import UserForm, UserContactForm

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user-list")
    else:
        form = UserForm()
    return render(request, "login/add_user.html", {"form": form})

def user_contact(request):
    if request.method == "POST":
        form = UserContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            return render(request, "login/success.html", {"name": name, "email": email})
    else:
        form = UserContactForm()
    return render(request, "login/user_contact.html", {"form": form})

def success_view(request):
    return render(request, 'success.html')
