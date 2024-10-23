from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Articles(models.Model):
    Title = models.CharField(max_length=30)
    Content = models.CharField(max_length=30)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Edition_Date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Title: {self.Title}, Content: {self.Content}, Author: {self.Author.username}, Edition Date: {self.Edition_Date}"
