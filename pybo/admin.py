from django.contrib import admin

# Register your models here.

from .models import Question, Answer, Category
from common.models import CustomUser

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    search_fields=['content']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields=['name']

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display =(
        'username',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
        'last_login',
        'date_joined',

    )