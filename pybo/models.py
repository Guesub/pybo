from django.db import models
from common.models import CustomUser

# Create your models here.

# Category model 추가
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

class Question(models.Model):
    author=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_question')
    subject=models.CharField(max_length=200)
    content=models.TextField()
    content_summary=models.TextField()
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(CustomUser, related_name='voter_question')
    category = models.CharField(max_length=255, default='문의글', blank=True)
    viewCount = models.IntegerField(default=0, blank=True)
    avatar = models.CharField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.id)

class Answer(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date=models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(CustomUser, related_name='voter_answer')
    avatar = models.CharField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        resultText = str(self.question) + '/' + self.content 
        return resultText 

class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


class Citycode(models.Model):
    code=models.IntegerField()
    provins= models.TextField()
    city=models.TextField()

    def __str__(self):
        return str(self.code)
