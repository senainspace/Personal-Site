from django.shortcuts import render
from .models import Project, Experience, Education, Competition



def _split_commas(s: str) -> list[str]:
    if not s:
        return []
    return [x.strip() for x in s.split(",") if x.strip()]


def _split_lines(s: str) -> list[str]:
    if not s:
        return []
    lines = []
    for line in s.splitlines():
        line = line.strip()
        if not line:
            continue
        # allow "- something" style bullets
        if line.startswith("- "):
            line = line[2:].strip()
        lines.append(line)
    return lines


def index(request):
    featured_projects = list(
        Project.objects.filter(is_featured=True).order_by("-start_date", "-created_at")
    )
    projects = list(
        Project.objects.filter(is_featured=False).order_by("-start_date", "-created_at")
    )

    experiences = list(Experience.objects.all())
    education_items = list(Education.objects.all())
    competitions = Competition.objects.all()   # 👈 EKLENDİ

    # Project tag split
    for p in featured_projects:
        p.tag_list = _split_commas(p.tech_stack)
    for p in projects:
        p.tag_list = _split_commas(p.tech_stack)

    # Experience highlights split
    for e in experiences:
        e.highlight_list = _split_lines(e.highlights)

    # Education description split
    for edu in education_items:
        edu.bullet_list = _split_lines(edu.description)

    return render(
        request,
        "portfolio/index.html",
        {
            "featured_projects": featured_projects,
            "projects": projects,
            "experiences": experiences,
            "education_items": education_items,
            "competitions": competitions,   # 👈 TEMPLATE’E GİDİYOR
        },
    )
