from rest_framework import viewsets

from .serializers import HardSkillSerializer, SoftSkillSerializer, SkillTypeSerializer
from .models import HardSkill, SoftSkill, SkillType


class HardSkillViewSet(viewsets.ModelViewSet):
    query_set = HardSkill.objects.all().order_by('name')
    serializer_class = HardSkillSerializer


class SoftSkillViewSet(viewsets.ModelViewSet):
    query_set = SoftSkill.objects.all().order_by('name')
    serializer_class = SoftSkillSerializer


class SkillTypeViewSet(viewsets.ModelViewSet):
    query_set = SkillType.objects.all().order_by('name')
    serializer_class = SkillTypeSerializer
