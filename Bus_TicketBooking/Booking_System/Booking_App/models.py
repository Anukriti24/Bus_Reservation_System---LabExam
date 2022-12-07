from django.db import models

# Create your models here.

class BookingListItem(models.Model):
    content = models.TextField() 
    date = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=100)


class BookingDone(models.Model):
    done = models.Exists