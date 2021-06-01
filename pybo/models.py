from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Category model 추가
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Question(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    category = models.CharField(max_length=255, default='문의글', blank=True)

    def __str__(self):
        return str(self.id)

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date=models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        resultText = str(self.question) + '/' + self.content 
        return resultText 

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)



