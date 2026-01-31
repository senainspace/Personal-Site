from django.db import models


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
