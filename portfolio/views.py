from django.shortcuts import render
from .models import Project, Experience


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
    projects = list(Project.objects.all())
    experiences = list(Experience.objects.all())

    # Prepare template-friendly lists (templates can't call split()).
    for p in projects:
        p.tag_list = _split_commas(p.tech_stack)

    for e in experiences:
        e.highlight_list = _split_lines(e.highlights)

    return render(
        request,
        "portfolio/index.html",
        {"projects": projects, "experiences": experiences},
    )
