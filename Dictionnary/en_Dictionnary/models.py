from django.db import models

class Word(models.Model):
    word = models.CharField(max_length = 250, unique = True)
    definition = models.TextField


    def __str__(self):
        return self.word

# Create your models here.

