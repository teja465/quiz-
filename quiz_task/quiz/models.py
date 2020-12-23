from django.db import models

# Create your models here.
class questions(models.Model):
    quiz_name=models.CharField(max_length=100)
    question=models.CharField(max_length=300)
    a=models.CharField(max_length=200)
    b=models.CharField(max_length=200)
    c=models.CharField(max_length=200)
    d=models.CharField(max_length=200)
    answer=models.CharField(max_length=5)

    def __str__(self):
        return self.question