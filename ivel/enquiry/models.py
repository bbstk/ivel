from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=128)
    description = models.TextField()
    category = models.CharField(max_length=128)

    def __str__(self):
        return self.name + "-" + self.location + "-" + self.category
    
