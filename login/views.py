from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView, FormView
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from .models import User
from django.db.models import Count, Q
from .forms import UserForm, UserContactForm, FeedbackForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms_auth import UserSignUpForm


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

class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = "login/feedback.html"
    success_url = reverse_lazy("success-url")

    def form_valid(self, form):
        username = form.cleaned_data['username']
        feedback = form.cleaned_data['feedback']
        print(f"Feedback from {username}: {feedback}")
        return super().form_valid(form)

def success_view(request):
    return render(request, 'login/success.html')


def signup_view(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("user-list")
    else:
        form = UserSignUpForm()

    return render(request, "login/signup.html", {"form": form})