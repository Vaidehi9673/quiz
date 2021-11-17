from django.db import models

# Create your models here.
class Contact(models.Model):
    Sr = models.AutoField(primary_key=True)
    email=models.CharField(max_length=50, default="")
    uname=models.CharField(max_length=100, default="")
    text=models.TextField()

    def __str__(self):
        return self.uname

class Question(models.Model):
    Sno=models.AutoField(primary_key=True)
    Ques=models.CharField(max_length=300, null=True)
    opt1=models.CharField(max_length=200, null=True)
    opt2=models.CharField(max_length=200, null=True)
    opt3=models.CharField(max_length=200, null=True)
    opt4=models.CharField(max_length=200, null=True)
    ans=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Ques