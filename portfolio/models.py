from django.db import models


class Project(models.Model):
    title    = models.CharField(max_length=200, help_text="Başlık (TR)")
    title_en = models.CharField(max_length=200, blank=True, help_text="Title (EN) — boşsa TR kullanılır")

    description    = models.TextField()
    short_description    = models.CharField(max_length=220, blank=True, help_text="Kart özeti (TR)")
    short_description_en = models.CharField(max_length=220, blank=True, help_text="Card summary (EN) — boşsa TR kullanılır")

    long_description    = models.TextField(blank=True, help_text="Modal açıklama (TR)")
    long_description_en = models.TextField(blank=True, help_text="Modal description (EN) — boşsa TR kullanılır")

    image    = models.ImageField(upload_to="projects/", blank=True, null=True)
    url      = models.URLField(blank=True, null=True)

    start_date = models.DateField(help_text="Proje başlangıç tarihi")
    end_date   = models.DateField(blank=True, null=True, help_text="Devam ediyorsa boş bırak")

    tech_stack = models.CharField(
        max_length=250, blank=True,
        help_text='Virgülle ayır: "Python, OpenCV, MediaPipe"',
    )

    github_url = models.URLField(blank=True, null=True)
    demo_url   = models.URLField(blank=True, null=True)

    is_featured = models.BooleanField(default=False, help_text="Öne çıkan projelerde göster")

    role    = models.CharField(max_length=200, blank=True, help_text='Örn: "Raidyn Team | Otonom Navigasyon" (TR)')
    role_en = models.CharField(max_length=200, blank=True, help_text="Role (EN)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-start_date", "-created_at"]

    def __str__(self):
        return self.title


class Experience(models.Model):
    title           = models.CharField(max_length=200, help_text='Pozisyon (TR): "Yazılım Mühendisi Stajyeri"')
    title_en        = models.CharField(max_length=200, blank=True, help_text="Title (EN)")
    organization    = models.CharField(max_length=200, help_text="Şirket / Üniversite (TR)")
    organization_en = models.CharField(max_length=200, blank=True, help_text="Organization (EN)")
    location        = models.CharField(max_length=120, blank=True)

    start_date = models.DateField()
    end_date   = models.DateField(blank=True, null=True, help_text="Devam ediyorsa boş bırak")

    highlights    = models.TextField(blank=True, help_text="Madde madde, satır başına bir madde (TR):\n- Yaptım X\n- Geliştirdim Y")
    highlights_en = models.TextField(blank=True, help_text="Highlights (EN) — boşsa TR kullanılır")

    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-start_date", "-created_at"]

    def __str__(self):
        return f"{self.title} · {self.organization}"


class Education(models.Model):
    school        = models.CharField(max_length=160, help_text="Okul adı (TR)")
    school_en     = models.CharField(max_length=160, blank=True, help_text="School name (EN)")
    degree        = models.CharField(max_length=160, blank=True, help_text="Derece (TR): Lisans, Yüksek Lisans…")
    degree_en     = models.CharField(max_length=160, blank=True, help_text="Degree (EN): Bachelor's, Master's…")
    department    = models.CharField(max_length=160, blank=True, help_text="Bölüm (TR)")
    department_en = models.CharField(max_length=160, blank=True, help_text="Department (EN)")

    start_date = models.DateField()
    end_date   = models.DateField(blank=True, null=True)

    description    = models.TextField(blank=True, help_text="Notlar / maddeler (TR)")
    description_en = models.TextField(blank=True, help_text="Notes (EN) — boşsa TR kullanılır")

    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.school} — {self.department or self.degree}"


class Competition(models.Model):
    title        = models.CharField(max_length=200, help_text="Yarışma adı (TR)")
    title_en     = models.CharField(max_length=200, blank=True, help_text="Competition name (EN)")
    organizer    = models.CharField(max_length=200, blank=True)
    date         = models.DateField(null=True, blank=True)
    award        = models.CharField(max_length=200, blank=True, help_text="Derece/ödül (TR): Finalist, 2. lik")
    award_en     = models.CharField(max_length=200, blank=True, help_text="Award (EN)")

    team_logo  = models.ImageField(upload_to="competitions/", blank=True, null=True)
    team_name  = models.CharField(max_length=200, blank=True)
    role       = models.CharField(max_length=200, blank=True, help_text="Rolün (TR)")
    role_en    = models.CharField(max_length=200, blank=True, help_text="Your role (EN)")

    team_members = models.TextField(blank=True, help_text="Satır başına bir kişi")

    description    = models.TextField(blank=True, help_text="Kısa özet (TR)")
    description_en = models.TextField(blank=True, help_text="Short summary (EN)")
    highlights     = models.TextField(blank=True, help_text="Maddeler (TR)")
    highlights_en  = models.TextField(blank=True, help_text="Highlights (EN)")

    url   = models.URLField(blank=True)
    image = models.ImageField(upload_to="competitions/", blank=True, null=True)

    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-date", "-created_at"]

    def __str__(self):
        return self.title


class Community(models.Model):
    name        = models.CharField(max_length=200, help_text="Kulüp adı (TR)")
    name_en     = models.CharField(max_length=200, blank=True, help_text="Club name (EN)")
    role        = models.CharField(max_length=200, blank=True, help_text="Rolün (TR): Üye, Çekirdek Ekip…")
    role_en     = models.CharField(max_length=200, blank=True, help_text="Role (EN)")

    start_date = models.DateField(null=True, blank=True)
    end_date   = models.DateField(null=True, blank=True)

    organization = models.CharField(max_length=200, blank=True)

    description    = models.TextField(blank=True, help_text="Kısa özet (TR)")
    description_en = models.TextField(blank=True, help_text="Short summary (EN)")
    highlights     = models.TextField(blank=True, help_text="Maddeler (TR)")
    highlights_en  = models.TextField(blank=True, help_text="Highlights (EN)")

    url  = models.URLField(blank=True)
    logo = models.ImageField(upload_to="communities/", blank=True, null=True)

    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-start_date", "-created_at"]

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="images")
    image   = models.ImageField(upload_to="project_images/")
    caption = models.CharField(max_length=120, blank=True, default="")
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.project.title} image {self.id}"
