from django.shortcuts import render, get_object_or_404

from apps.news.models import News
from apps.events.models import Event
from apps.achievements.models import Achievement
from apps.gallery.models import Gallery
from apps.pages.models import SchoolStatistic, EducationDetail
from apps.teachers.models import Teacher
from django.contrib import messages
from django.shortcuts import redirect
from .models import ContactMessage


def home(request):
    latest_news = News.objects.filter(is_published=True)[:3]
    latest_achievements = Achievement.objects.filter(is_published=True)[:3]
    school_stats = SchoolStatistic.objects.first()

    return render(request, 'home.html', {
        'latest_news': latest_news,
        'latest_achievements': latest_achievements,
        'school_stats': school_stats,
    })


def section(request, title, subtitle, cards):
    return render(request, 'pages/section.html', {
        'title': title,
        'subtitle': subtitle,
        'cards': cards,
    })


def about(request):
    return render(request, 'pages/about.html')


def education_detail(request, slug):
    item = EducationDetail.objects.filter(
        slug=slug,
        is_published=True
    ).first()

    if not item:
        return render(request, 'pages/education_empty.html', {
            'slug': slug
        })

    return render(request, 'pages/education_detail.html', {
        'item': item
    })


def teachers(request):
    items = Teacher.objects.filter(is_published=True)

    return render(request, 'pages/teachers.html', {
        'teachers': items
    })

def teacher_detail(request, pk):
    item = get_object_or_404(
        Teacher,
        pk=pk,
        is_published=True
    )
    return render(request, 'pages/teacher_detail.html', {
        'item': item
    })

def news(request):
    items = News.objects.filter(is_published=True)
    return render(request, 'pages/news.html', {'items': items})


def news_detail(request, pk):
    item = get_object_or_404(
        News,
        pk=pk,
        is_published=True
    )
    return render(request, 'pages/news_detail.html', {
        'item': item
    })


def events(request):
    items = Event.objects.filter(is_published=True)

    return render(request, 'pages/events.html', {
        'items': items,
    })

def event_detail(request, pk):
    item = get_object_or_404(
        Event,
        pk=pk,
        is_published=True
    )
    return render(request, 'pages/event_detail.html', {
        'item': item
    })

def achievements(request):
    items = Achievement.objects.filter(is_published=True)

    return render(request, 'pages/achievements.html', {
        'items': items,
    })

def achievement_detail(request, pk):
    item = get_object_or_404(
        Achievement,
        pk=pk,
        is_published=True
    )
    return render(request, 'pages/achievement_detail.html', {
        'item': item
    })


def gallery(request):
    items = Gallery.objects.filter(is_published=True)

    return render(request, 'pages/gallery.html', {
        'items': items,
    })

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not message:
            messages.error(
                request,
                "Аты-жөнүңүздү жана билдирүүңүздү толтуруңуз."
            )
        else:
            ContactMessage.objects.create(
                name=name,
                phone=phone,
                email=email,
                message=message
            )

            messages.success(
                request,
                "Билдирүүңүз ийгиликтүү жөнөтүлдү!"
            )

            return redirect("contacts")

    return render(request, "pages/contacts.html")