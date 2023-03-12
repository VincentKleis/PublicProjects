from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True)
    pub_date = models.DateField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.title}, {self.author}, {self.pub_date}, {self.price}"