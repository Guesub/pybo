from django.contrib import admin

# Register your models here.

from .models import Question, Answer, Category

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    search_fields=['content']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields=['name']