from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from . import models
from .forms import RegistrationForm, LoginForm


def render_home_page(request):
    return render(request, "website/index.html")


def render_categories_page(request, slug):
    category = models.Category.objects.get(slug=slug)
    context = {
        "category": category,
    }
    return render(request, "website/categories.html", context)


def render_login_page(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()

    context = {
        "form": form,
    }
    return render(request, "website/login.html", context)


def render_registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()

    context = {
        "form": form,
    }
    return render(request, "website/registration.html", context)


def logout_user(request):
    logout(request)
    return redirect("home")
