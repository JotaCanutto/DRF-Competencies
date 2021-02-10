from rest_framework import viewsets

from .serializers import HardSkillSerializer, SoftSkillSerializer, SkillTypeSerializer
from .models import HardSkill, SoftSkill, SkillType


class HardSkillViewSet(viewsets.ModelViewSet):
    queryset = HardSkill.objects.all().order_by('name')
    serializer_class = HardSkillSerializer


class SoftSkillViewSet(viewsets.ModelViewSet):
    queryset = SoftSkill.objects.all().order_by('name')
    serializer_class = SoftSkillSerializer


class SkillTypeViewSet(viewsets.ModelViewSet):
    queryset = SkillType.objects.all().order_by('name')
    serializer_class = SkillTypeSerializer
