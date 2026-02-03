from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    """
    Portfolio project shown on the website.
    Admin-friendly + CV-friendly: includes dates, tech tags, optional image and link.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    # NEW: When did you build this project?
    start_date = models.DateField(help_text="Project start date")
    end_date = models.DateField(blank=True, null=True, help_text="Leave empty if ongoing")

    # NEW: Tags like: "Python, OpenCV, MediaPipe"
    tech_stack = models.CharField(
        max_length=250,
        blank=True,
        help_text='Comma-separated tags, e.g. "Python, OpenCV, MediaPipe"',
    )
    # Links
    github_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)

    # Display options
    is_featured = models.BooleanField(
        default=False,
        help_text="Featured projects appear first on the website."
    )

    # Optional subtitle under the title
    role = models.CharField(
        max_length=200,
        blank=True,
        help_text='Optional: e.g. "Raidyn Team | Autonomous Navigation"'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-start_date", "-created_at"]

    def __str__(self):
        return self.title


class Experience(models.Model):
    """
    Experience / Education timeline item.
    Examples:
    - Internship
    - Student venture (VTOL)
    - University / High school (education entries)
    """

    title = models.CharField(max_length=200, help_text='Role or education title, e.g. "Software Engineering Intern"')
    organization = models.CharField(max_length=200, help_text='Company / University / Team name')
    location = models.CharField(max_length=120, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave empty if ongoing")

    # We'll store bullets as plain text lines (one per line) for simplicity.
    highlights = models.TextField(
        blank=True,
        help_text="Write one bullet per line. Example:\n- Did X\n- Built Y\n- Improved Z",
    )

    # Control ordering manually (top to bottom) in the admin.
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-start_date", "-created_at"]

    def __str__(self):
        return f"{self.title} · {self.organization}"

class Education(models.Model):
    school = models.CharField(max_length=160)
    degree = models.CharField(max_length=160, blank=True)
    department = models.CharField(max_length=160, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    description = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.school} — {self.department or self.degree}"
from django.db import models

class Competition(models.Model):
    title = models.CharField(max_length=200)  # yarışma adı
    organizer = models.CharField(max_length=200, blank=True)  # düzenleyen kurum/organizasyon
    date = models.DateField(null=True, blank=True)  # tek gün / başlangıç tarihi gibi kullan
    award = models.CharField(max_length=200, blank=True)  # derece/ödül (örn: Finalist, 2nd place)

    team_logo = models.ImageField(upload_to="competitions/", blank=True, null=True)
    team_name = models.CharField(max_length=200, blank=True)
    role = models.CharField(max_length=200, blank=True)  # senin rolün

    # ÖNERİ: takım üyelerini admin’de alt alta yaz (her satır 1 kişi)
    team_members = models.TextField(blank=True)

    description = models.TextField(blank=True)  # kısa özet
    highlights = models.TextField(blank=True)   # her satır 1 madde
    url = models.URLField(blank=True)  # yarışma sayfası / haber / repo vb.

    image = models.ImageField(upload_to="competitions/", blank=True, null=True)

    order = models.PositiveIntegerField(default=0)  # manuel sıralama (küçük olan üstte)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-date", "-created_at"]

    def __str__(self):
        return self.title


