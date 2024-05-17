from django.shortcuts import get_object_or_404, redirect, render
import random
from .models import Category, Subject,Question

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def display_subjects(request, category_id):
    selected_category = get_object_or_404(Category, pk=category_id)
    subjects = selected_category.subject.all()
    return render(request, 'subjects.html', {'category': selected_category, 'subjects': subjects})

def quiz_view(request, subject_id):
    questions = Question.objects.filter(subject_id=subject_id)
    selected_questions = random.sample(list(questions),20) #here to change the number of question to show 
    context ={"quiz":selected_questions}
    return render(request,'quiz.html',context)

def submit_quiz(request):
    if request.method == 'POST':
        user_answers = []
        for question_id in request.POST:
            if question_id.isdigit():  # Check if the form field represents a question ID
                selected_option = request.POST.get(question_id)
                user_answers.append({
                    'question_id': int(question_id),
                    'selected_option': selected_option
                })

        request.session['user_answers'] = user_answers
        return redirect('quiz_results')
    else:
        # Handle invalid request method
        pass

def quiz_results(request):
    user_answers = request.session.get('user_answers', [])
    question_ids = [answer['question_id'] for answer in user_answers]
    questions = Question.objects.filter(pk__in=question_ids)
    
    total_marks = sum(question.marks for question in questions if question.correct_answer == user_answers[question_ids.index(question.id)]['selected_option'])
    
    request.session['user_answers'] = []  # Clear the user's answers

    return render(request, 'quiz_results.html', {'total_marks': total_marks})

