from django.db import models


class SkillType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class HardSkill(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    definition = models.TextField(null=False, blank=False)
    skill_type = models.ForeignKey(SkillType, related_name='hard_skills', on_delete=models.CASCADE)

    def __str__(self):
        return f'HardSkill: {self.name}'


class SoftSkill(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    definition = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'SoftSkill: {self.name}'
