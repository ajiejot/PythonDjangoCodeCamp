from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)