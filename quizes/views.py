from django.shortcuts import redirect, render
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
    # quiz = Subject.objects.filter(id=subject_id).first()
    questions = Question.objects.filter(subject_id=subject_id)
    selected_questions = random.sample(list(questions),20) #here to change the number of question to show 
    context ={"quiz":selected_questions}
    return render(request,'quiz.html',context)

def submit_quiz(request):
    if request.method == 'POST':
        # Process the submitted quiz answers
        # Retrieve the user's answers from the form
        user_answers = []
        for question in Question.objects.all():
            selected_option = request.POST.get(str(question.id), None)
            if selected_option is not None:
                user_answers.append({
                    'question_id': question.id,
                    'selected_option': selected_option
                })

        # Store the user's answers in the session
        request.session['user_answers'] = user_answers

        # Redirect to the quiz results page
        return redirect('quiz_results')
    else:
        # Handle invalid request method (GET or other methods)
        # Redirect to an appropriate page or show an error message
        pass

def quiz_results(request):
    # Retrieve the user's answers from the session
    user_answers = request.session.get('user_answers', [])
    
    # Calculate the total marks obtained by the user
    total_marks = 0
    for answer in user_answers:
        question = Question.objects.get(pk=answer['question_id'])
        if question.correct_answer == answer['selected_option']:
            total_marks += question.marks
    
    # Clear the user's answers from the session
    request.session['user_answers'] = []

    # Render the quiz results page with the total marks
    return render(request, 'quiz_results.html', {'total_marks': total_marks})


