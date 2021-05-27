from django.db import models

class DogImage(models.Model):
    image = models.ImageField(upload_to="uploads/", null=True, blank = False)
