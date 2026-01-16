from django.db import models

class Card(models.Model):
    name = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name