from django.db import models
from django.utils import timezone


# Create your models here.
class question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published(self):
        return self.pub_date <= timezone.now()




class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
