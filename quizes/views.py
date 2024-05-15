from django.shortcuts import render
import random
from .models import Category, Subject,Question

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def display_subjects(request, category_id):
    selected_category = Category.objects.get(pk=category_id)
    subjects = selected_category.subject.all()
    return render(request, 'subjects.html', {'category': selected_category, 'subjects': subjects})

def quiz_view(request, subject_id):
    quiz = Subject.objects.filter(id=subject_id).first()
    questions = Question.objects.filter(subject_id=subject_id)
    selected_questions = random.sample(list(questions),20) 
    context ={"quiz":selected_questions}
    return render(request,'quiz.html',context)



