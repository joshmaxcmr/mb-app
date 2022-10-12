from django.db import models


# Create your models here.

class Post(models.Model):
    text = models.TextField()

    # méthode pour nommer le modèle dans l'espace admin
    def __str__(self):
        return self.text[:50]
