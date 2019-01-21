from django.db import models

# Create your models here.
class Sections(models.Model):
    section_id = models.CharField(max_length=127, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

class Ratings(models.Model):
    rating_level = models.TextField(null=True,blank=True)
