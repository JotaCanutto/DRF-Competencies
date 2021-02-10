from django.db import models


class SkillType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return f'SkillType: {self.name}'


class HardSkill(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    definition = models.TextField(null=False, blank=False)
    skill_type = models.ManyToManyField(SkillType)

    def __str__(self):
        return f'HardSkill: {self.name}'


class SoftSkill(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    definition = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'SoftSkill: {self.name}'
