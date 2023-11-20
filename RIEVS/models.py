from django.db import models

# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        """Devolve uma string do modelo"""
        return self.title


class Publication(models.Model):
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="img")
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma string do modelo"""
        return self.text[:50] + "..."
