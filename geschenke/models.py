from django.db import models

class Geschenk(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to = 'geschenke/bilder/', blank=True)
   #we can add blank to anything to make it optional
