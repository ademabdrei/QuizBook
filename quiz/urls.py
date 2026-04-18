from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('api/quiz/<int:quiz_id>/', views.quiz_data, name='quiz_data'),
    
    path('admin/login/', views.login_view, name='login'),
    path('admin/', views.admin_page, name='admin_page'),
    path('admin/quiz/create/', views.create_quiz, name='create_quiz'),
    path('admin/quiz/edit/<int:quiz_id>/', views.edit_quiz, name='edit_quiz'),
    path('admin/quiz/delete/<int:quiz_id>/', views.delete_quiz, name='delete_quiz'),
    path('admin/question/save/', views.save_question, name='save_question'),
    path('admin/question/delete/<int:question_id>/', views.delete_question, name='delete_question'),
]