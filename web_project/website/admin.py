from django.contrib import admin

from . import models
from .forms import CategoryAdminForm


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "slug"]
    list_display_links = ["pk", "name"]
    prepopulated_fields = {"slug": ("name",)}
    form = CategoryAdminForm
