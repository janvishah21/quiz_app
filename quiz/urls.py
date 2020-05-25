from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('message/', views.message, name='message'),
	path('<int:index>/', views.question, name='question'),
	path('<int:question_id>/update_answer/', views.update_answer, name='update_answer'),
	path('reviews/', views.reviews, name='reviews'),
]