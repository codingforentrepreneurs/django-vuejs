from django.db import models

# Create your models here.
class Content(models.Model):
    # user = models.ForeignKey(User)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()