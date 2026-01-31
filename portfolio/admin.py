from django.contrib import admin
from django.utils.html import format_html

from .models import Project, Experience


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Clean listing + image preview for a professional look.
    """

    list_display = ("thumbnail", "title", "project_period", "url", "created_at")
    list_display_links = ("title",)
    list_filter = ("start_date", "created_at")
    search_fields = ("title", "description", "tech_stack")
    readonly_fields = ("preview_large", "created_at", "updated_at")

    fieldsets = (
        ("Project Info", {"fields": ("title", "description", "url")}),
        ("Timeline & Tags", {"fields": ("start_date", "end_date", "tech_stack")}),
        ("Image", {"fields": ("image", "preview_large")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    def thumbnail(self, obj: Project):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:56px;height:56px;object-fit:cover;border-radius:10px;" />',
                obj.image.url,
            )
        return "—"

    thumbnail.short_description = "Preview"

    def preview_large(self, obj: Project):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width:420px;width:100%;height:auto;'
                'border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,0.15);" />',
                obj.image.url,
            )
        return "No image uploaded."

    preview_large.short_description = "Large Preview"

    def project_period(self, obj: Project):
        if obj.end_date:
            return f"{obj.start_date:%b %Y} – {obj.end_date:%b %Y}"
        return f"{obj.start_date:%b %Y} – Present"

    project_period.short_description = "Period"


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "organization", "experience_period", "location")
    list_display_links = ("title",)
    list_editable = ("order",)
    search_fields = ("title", "organization", "location", "highlights")
    list_filter = ("start_date",)

    fieldsets = (
        ("Main", {"fields": ("title", "organization", "location")}),
        ("Timeline", {"fields": ("start_date", "end_date", "order")}),
        ("Highlights", {"fields": ("highlights",)}),
    )

    def experience_period(self, obj: Experience):
        if obj.end_date:
            return f"{obj.start_date:%b %Y} – {obj.end_date:%b %Y}"
        return f"{obj.start_date:%b %Y} – Present"

    experience_period.short_description = "Period"
