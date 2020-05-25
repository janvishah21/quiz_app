from django.db import models
from django.utils import timezone

# Create your models here
class Question(models.Model):
	index = models.IntegerField(default=1)
	question_text = models.CharField(max_length = 200)
	choice_var = models.BooleanField()
	text_var = models.BooleanField()

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 100)
	is_answer = models.BooleanField(default=False)

	def __str__(self):
		return self.choice_text

class Answer(models.Model):
	username = models.CharField(max_length = 20, default='')
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
	answer_text = models.TextField(max_length = 5000, null=True)
	time = models.DateTimeField('time answered')

class Review(models.Model):
	username = models.CharField(max_length = 20, default='')
	rating = models.IntegerField(default=5)
	review_text = models.CharField(max_length=2000)
	pika_exp = models.CharField(max_length=2000)
	remarks = models.CharField(max_length=2000)
	time = models.DateTimeField('response time')