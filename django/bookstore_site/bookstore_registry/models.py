from django.db import models

# Create your models here.
class Book(models.Model):
    title =  models.CharField(max_length = 50, null=True)
    #author = models.CharField(max_length = 50)
    #pub_date = models.DateField(blank=True)
    #price = models.IntegerField(null=True)

    def __str__(self):
        return self.title, 
        #self.author, self.pub_date, self.price