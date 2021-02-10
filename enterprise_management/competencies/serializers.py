from rest_framework import serializers

from .models import HardSkill, SoftSkill, SkillType


class HardSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardSkill
        fields = '__all__'


class SoftSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftSkill
        fields = '__all__'


class SkillTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillType
        fields = '__all__'
