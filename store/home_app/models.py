from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    subject = models.CharField(max_length=30)
    comment = models.TextField()
    
    def __str__(self):
        return self.subject

