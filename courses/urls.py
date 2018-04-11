from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'teachers', views.TeacherViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
