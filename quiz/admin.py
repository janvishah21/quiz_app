from django.contrib import admin

# Register your models here.
from .models import *

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	fields = ['index', 'question_text', 'choice_var', 'text_var']
	inlines = [ChoiceInLine]
	list_display = ('index', 'question_text', 'choice_var', 'text_var')

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('time', 'username', 'question', 'choice', 'answer_text')

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('time', 'username', 'rating', 'review_text', 'pika_exp')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Review, ReviewAdmin)