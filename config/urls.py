from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.pages import views

admin.site.site_header = "№105 мектеп — башкаруу панели"
admin.site.site_title = "№105 мектеп"
admin.site.index_title = "Мектептин маалыматтарын башкаруу"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teachers/', views.teachers, name='teachers'),
path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('news/', views.news, name='news'),
path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('events/', views.events, name='events'),
path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('achievements/', views.achievements, name='achievements'),
path('achievements/<int:pk>/', views.achievement_detail, name='achievement_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('contacts/', views.contacts, name='contacts'),
path('about/<slug:slug>/', views.education_detail, name='education_detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )