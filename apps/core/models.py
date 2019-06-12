from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.

class Icon(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Icon"
        verbose_name_plural = "Icons"

class Folder(models.Model):
    Icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    title = models.TextField()

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"

class Resource(models.Model):
    Folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)
    title = models.TextField()
    body = models.TextField()
    # body = MarkdownxField()

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

class Template(models.Model):
    title = models.TextField()
    Folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"
    
class Question(models.Model):
    Template = models.ForeignKey(Template, on_delete=models.CASCADE, null=True)
    question = models.TextField(null=True)
    description = models.TextField(null=True)
    text_type = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

