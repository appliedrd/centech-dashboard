from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tablebord.models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)