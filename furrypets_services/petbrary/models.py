from django.db import models


class PetsModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=255)

    objects = models.Manager()


class CareAndHealthModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=255)

    objects = models.Manager()


