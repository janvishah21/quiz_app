from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
import random

from .models import *

# Create your views here.
def index(request):
	count = Question.objects.count()
	return render(request, 'quiz/index.html', {'count': count})

def question(request, index):
	question = Question.objects.get(index=index)
	count = Question.objects.count()
	image_id = index%8 + 1
	return render(request, 'quiz/question.html', {'index' : index, 'question' : question, 'count': count, 'image_id': str(image_id)})

def message(request):
	return render(request, 'quiz/message.html')

def update_answer(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		if question.choice_var:
			return render(request, 'quiz/question.html', {'index' : question.index, 'question' : question, 'error_message' : 'You didn\'t select any choice !'})
		pass
	try:
		answer_text = request.POST['answer_text']
	except:
		if question.text_var:
			return render(request, 'quiz/question.html', {'index' : question.index, 'question' : question, 'error_message' : 'You didn\'t write any answer !'})
		pass
	answer = Answer()
	answer.username = request.user
	answer.question = question
	answer.time = timezone.now()
	if question.choice_var:
		answer.choice = choice
	if question.text_var:
		answer.answer_text = answer_text
	answer.save()
	if question.index == Question.objects.count():
		return HttpResponseRedirect(reverse('quiz:message'))
	else:
		return HttpResponseRedirect(reverse('quiz:question', args = (question.index+1,)))

def reviews(request):
	if request.method == 'POST':
		review = Review()
		review.username = request.user
		review.time = timezone.now()
		review.rating = request.POST['rating']
		review.review_text = request.POST['review_text']
		review.pika_exp = request.POST['pika_exp']
		review.save()
		messages.success(request, 'Thank you for your reviews !', extra_tags='alert alert-success alert-dismissible fade show')
		return redirect('home')
	else:
		return render(request, 'quiz/reviews.html')