from django.shortcuts import render
from .models import Project, Experience, Education, Competition, Community


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

    for p in featured_projects + projects:
        p.tag_list = _split_commas(p.tech_stack)

    experiences = list(Experience.objects.all())
    for e in experiences:
        e.highlight_list    = _split_lines(e.highlights)
        e.highlight_list_en = _split_lines(e.highlights_en) if e.highlights_en else e.highlight_list

    education_items = list(Education.objects.all())
    for edu in education_items:
        edu.bullet_list    = _split_lines(edu.description)
        edu.bullet_list_en = _split_lines(edu.description_en) if edu.description_en else edu.bullet_list

    competitions = list(Competition.objects.all())
    for c in competitions:
        c.highlight_list    = _split_lines(c.highlights)
        c.highlight_list_en = _split_lines(c.highlights_en) if c.highlights_en else c.highlight_list
        c.member_list       = _split_lines(c.team_members)

    communities = list(Community.objects.all())
    for com in communities:
        com.highlight_list    = _split_lines(com.highlights)
        com.highlight_list_en = _split_lines(com.highlights_en) if com.highlights_en else com.highlight_list

    return render(
        request,
        "portfolio/index.html",
        {
            "featured_projects": featured_projects,
            "projects": projects,
            "experiences": experiences,
            "education_items": education_items,
            "competitions": competitions,
            "communities": communities,
        },
    )
