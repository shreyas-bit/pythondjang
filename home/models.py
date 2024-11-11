from django.db import models

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    content=models.TextField()
    email=models.CharField(max_length=200)
    timeStamp=models.DateTimeField(auto_now_add="yes", blank=True)
    
    
    def __str__(self):
        return 'message from \n' + self.name
    
