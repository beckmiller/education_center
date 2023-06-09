from django.urls import path, include
from rest_framework import routers

from .views import CourseViewSet

router = routers.DefaultRouter()
router.register("courses", CourseViewSet, "courses")

urlpatterns = [
    path('', include(router.urls))
]
