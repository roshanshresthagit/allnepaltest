from django.shortcuts import render
from .models import Category, Subject

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def display_subjects(request, category_id):
    selected_category = Category.objects.get(pk=category_id)
    subjects = selected_category.subject.all()
    return render(request, 'category.html', {'category': selected_category, 'subjects': subjects})

def quiz_view(request, subject_id):
    quiz = Subject.objects.filter(id=subject_id).first()
    context ={"quiz":quiz}
    return render(request,'quiz.html',context)
