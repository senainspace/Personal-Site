from django.contrib import admin
from django.utils.html import format_html

from .models import Project, Experience, Education, Competition, Community


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("school", "department", "degree", "education_period", "order")
    list_editable = ("order",)
    ordering = ("order", "-start_date")
    search_fields = ("school", "degree", "description")
    list_filter = ("start_date","end_date")

    fieldsets = (
        ("Education Info", {"fields": ("school", "department", "degree")}),
        ("Timeline", {"fields": ("start_date", "end_date", "order")}),
        ("Details", {"fields": ("description",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
    readonly_fields = ("created_at", "updated_at")

    def education_period(self, obj: Education):
        if obj.end_date:
            return f"{obj.start_date:%b %Y} – {obj.end_date:%b %Y}"
        return f"{obj.start_date:%b %Y} – Present"

    education_period.short_description = "Period"

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """
    Admin configuration for Experience.
    Keep it simple and match the Experience model fields.
    """

    list_display = ("title", "organization", "location", "experience_period", "start_date", "end_date")
    list_display_links = ("title",)
    list_filter = ("organization", "start_date")
    search_fields = ("title", "organization", "location", "highlights")
    ordering = ("-start_date",)

    fieldsets = (
        ("Experience Info", {"fields": ("title", "organization", "location")}),
        ("Timeline", {"fields": ("start_date", "end_date")}),
        ("Highlights", {"fields": ("highlights",)}),
    )

    def experience_period(self, obj: Experience):
        if obj.end_date:
            return f"{obj.start_date:%b %Y} – {obj.end_date:%b %Y}"
        return f"{obj.start_date:%b %Y} – Present"

    experience_period.short_description = "Period"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Clean listing + image preview for a professional look.
    """
    list_display = ("thumbnail", "title", "is_featured", "project_period", "created_at")
    list_editable = ("is_featured",)
    list_filter = ("is_featured", "start_date", "created_at")
    list_display_links = ("title",)
    search_fields = ("title", "description", "tech_stack")
    readonly_fields = ("preview_large", "created_at", "updated_at")

    fieldsets = (
        ("Project Info", {"fields": ("title", "description", "role")}),
        ("Links", {"fields": ("github_url", "demo_url", "url")}),
        ("Timeline & Tags", {"fields": ("start_date", "end_date", "tech_stack", "is_featured")}),
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

    preview_large.short_description = "Large Preview" # shows above the image upload field
    def project_period(self, obj: Project):
        if obj.end_date:
            return f"{obj.start_date:%b %Y} – {obj.end_date:%b %Y}"
        return f"{obj.start_date:%b %Y} – Present"

    project_period.short_description = "Period"

from django.contrib import admin
from django.utils.html import format_html

from .models import Competition


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ("title", "award", "date", "is_logo", "order")
    list_filter = ("date",)
    search_fields = ("title", "organizer", "award", "team_name", "role", "team_members")
    ordering = ("order", "-date", "-created_at")
    list_editable = ("order",)

    readonly_fields = ("team_logo_preview", "image_preview")

    fieldsets = (
        ("Temel Bilgiler", {
            "fields": ("title", "organizer", "date", "award", "url")
        }),
        ("Takım", {
            "fields": ("team_name", "team_logo", "team_logo_preview", "team_members")
        }),
        ("Senin Rolün", {
            "fields": ("role",)
        }),
        ("İçerik", {
            "fields": ("description", "highlights")
        }),
        ("Görsel", {
            "fields": ("image", "image_preview")
        }),
        ("Sıralama", {
            "fields": ("order",)
        }),
    )

    def team_logo_preview(self, obj):
        if obj.team_logo:
            return format_html(
                '<img src="{}" style="height:50px;width:50px;object-fit:contain;border-radius:8px;border:1px solid #ddd;" />',
                obj.team_logo.url
            )
        return "-"

    team_logo_preview.short_description = "Team Logo Preview"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:70px;width:120px;object-fit:cover;border-radius:10px;border:1px solid #ddd;" />',
                obj.image.url
            )
        return "-"

    image_preview.short_description = "Image Preview"

    def is_logo(self, obj):
        return bool(obj.team_logo)

    is_logo.boolean = True
    is_logo.short_description = "Logo?"

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "start_date", "end_date", "order")
    list_filter = ("role",)
    search_fields = ("name", "role", "organization")
    ordering = ("order", "-start_date")
    list_editable = ("order",)

