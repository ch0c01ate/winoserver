from django.db import models


class Image(models.Model):
    img = models.ImageField(upload_to='images/')