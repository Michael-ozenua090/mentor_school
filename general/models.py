from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField( max_length=50)
    subject = models.CharField( max_length=50)
    message = models.TextField( max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']



