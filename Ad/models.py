from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500, null=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.description}"


    class Meta:
        ordering = ("-created_at",)

    

