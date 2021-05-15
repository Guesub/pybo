from django.contrib import admin

# Register your models here.

from .models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    search_fields=['content']