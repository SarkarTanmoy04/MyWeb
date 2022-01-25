from django.db import models

class Contact(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email= models.EmailField()
    Desc= models.TextField()
    Date=models.DateField()

    def __str__(self):
        return self.First_Name + " " +self.Last_Name
