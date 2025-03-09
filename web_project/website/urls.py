from django.urls import path

from . import views


urlpatterns = [
    path("", views.render_home_page, name="home"),
    path("categories/<slug:slug>/", views.render_categories_page, name="categories"),
    path("login/", views.render_login_page, name="login"),
    path("registration/", views.render_registration_page, name="registration"),
    path("logout/", views.logout_user, name="logout"),
]
