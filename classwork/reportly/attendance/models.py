from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    no_of_pages = models.IntegerField(default=10)
    
    author= models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField()
    isbn = models.CharField(max_length=42, null= True, blank = True)# here we are using null and blanck because if
#we dont, this database would not work. so null and blank means that if we dont fill those values, we could still summit things without filling ii

    def __str__(self):
        return self.title

class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=300)
    department = models.CharField(max_length=30)
    state = models.CharField(max_length=30)


    def __str__(self):
        return self.name



