from rest_framework import routers
from django.urls import path, include

from .views import HardSkillViewSet, SoftSkillViewSet, SkillTypeViewSet

router = routers.DefaultRouter()

router.register(r'hard_skill', HardSkillViewSet, basename="hard_skill")
router.register(r'soft_skill', SoftSkillViewSet, basename="soft_skill")
router.register(r'skill_type', SkillTypeViewSet, basename="skill_type")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]