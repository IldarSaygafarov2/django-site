from django.shortcuts import render
from . import models


def render_home_page(request):
    return render(request, "website/index.html")


def render_categories_page(request, slug):
    category = models.Category.objects.get(slug=slug)
    context = {
        "category": category,
    }
    return render(request, "website/categories.html", context)


def render_login_page(request):
    return render(request, "website/login.html")


def render_registration_page(request):
    return render(request, "website/registration.html")
