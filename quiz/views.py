from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question
import json


def quiz_list(request):
    quizzes = Quiz.objects.all().order_by('-created_at')
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all().order_by('order')
    questions_json = json.dumps([
        {
            'question': q.question_text,
            'answers': q.answers,
            'correct': q.correct_answer
        }
        for q in questions
    ])
    return render(request, 'quiz/quiz_detail.html', {
        'quiz': quiz,
        'questions_json': questions_json
    })


def quiz_data(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all().order_by('order')
    data = {
        'topic': quiz.topic,
        'questions': [
            {
                'question': q.question_text,
                'answers': q.answers,
                'correct': q.correct_answer
            }
            for q in questions
        ]
    }
    return JsonResponse(data)


@login_required
def admin_page(request):
    quizzes = Quiz.objects.all().order_by('-created_at')
    return render(request, 'quiz/admin.html', {'quizzes': quizzes})


def login_view(request):
    error = None
    if request.method == 'POST':
        from django.contrib.auth import authenticate, login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            error = 'Invalid username or password'
    return render(request, 'quiz/login.html', {'error': error})


@login_required
def create_quiz(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        description = request.POST.get('description', '')
        quiz = Quiz.objects.create(topic=topic, description=description, name=topic.split()[0])
        return redirect('/admin/quiz/edit/' + str(quiz.id) + '/')
    return redirect('/admin/')


@login_required
def edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all().order_by('order')
    return render(request, 'quiz/edit_quiz.html', {'quiz': quiz, 'questions': questions})


@login_required
@require_http_methods(["POST"])
def save_question(request):
    data = json.loads(request.body)
    quiz = get_object_or_404(Quiz, id=data['quiz_id'])
    
    if 'question_id' in data and data['question_id']:
        question = Question.objects.get(id=data['question_id'])
        question.question_text = data['question_text']
        question.answers = data['answers']
        question.correct_answer = data['correct_answer']
        question.save()
    else:
        order = quiz.questions.count()
        Question.objects.create(
            quiz=quiz,
            question_text=data['question_text'],
            answers=data['answers'],
            correct_answer=data['correct_answer'],
            order=order
        )
    return JsonResponse({'status': 'success'})


@login_required
def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    return redirect('/admin/')


@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    quiz_id = question.quiz.id
    question.delete()
    return redirect('/admin/quiz/edit/' + str(quiz_id) + '/')