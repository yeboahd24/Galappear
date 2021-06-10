from django.db import models


class Abstract(models.Model):
    image = models.ImageField(upload_to='images')

    def __ster__(self):
        return self.id


class Gaming(models.Model):
    image = models.ImageField(upload_to='images')

    def __ster__(self):
        return self.id


class Logo(models.Model):
    image = models.ImageField(upload_to='images')

    def __ster__(self):
        return self.id
