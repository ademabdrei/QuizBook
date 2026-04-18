from django.core.management.base import BaseCommand
from quiz.models import Quiz, Question


class Command(BaseCommand):
    help = 'Loads sample quiz data'

    def handle(self, *args, **options):
        quiz, created = Quiz.objects.get_or_create(
            topic="Anthropology Chapter 1: Introducing Anthropology Multiple Choice Questions (MCQs)- Part 3",
            defaults={
                'name': 'Anthropology Quiz',
                'description': 'MCQs about anthropology fundamentals'
            }
        )

        if created:
            questions_data = [
                {
                    "question": "1. What is the etymology of the term 'anthropology'?",
                    "answers": ["A. The study of human cultures and histories", "B. The study of human beings and their interactions", "C. The study of human beings and reason", "D. The study of the biological and psychological nature of humans"],
                    "correct": "C. The study of human beings and reason"
                },
                {
                    "question": "2. What distinguishes anthropology from other disciplines like sociology and biology?",
                    "answers": ["A. Its focus on the biological characteristics of humans", "B. Its exclusive study of material culture", "C. Its comprehensive examination of both biological and cultural characteristics of humans", "D. Its primary concern with economic structures"],
                    "correct": "C. Its comprehensive examination of both biological and cultural characteristics of humans"
                },
                {
                    "question": "3. What is the primary focus of anthropology as a scientific discipline?",
                    "answers": ["A. To study humans only through their biological aspects", "B. To study human social groups and their strategies for living", "C. To analyze the political systems of societies", "D. To categorize different human races and physical traits"],
                    "correct": "B. To study human social groups and their strategies for living"
                },
                {
                    "question": "4. How does anthropology seek to understand human diversity?",
                    "answers": ["A. By focusing exclusively on genetics and heredity", "B. By comparing material objects and religious beliefs", "C. Through a combination of biological and cultural perspectives", "D. By focusing only on the social aspects of human societies"],
                    "correct": "C. Through a combination of biological and cultural perspectives"
                },
                {
                    "question": "5. Which of the following best describes the scope of anthropology?",
                    "answers": ["A. Limited to the study of human genetics", "B. Narrowly focused on the development of human language", "C. Broad, covering all aspects of human existence, from origins to contemporary variations", "D. Focused solely on the development of agriculture and its impact"],
                    "correct": "C. Broad, covering all aspects of human existence, from origins to contemporary variations"
                },
                {
                    "question": "6. In what way does anthropology contribute to understanding human societies?",
                    "answers": ["A. By offering speculative theories about human nature", "B. By examining human societies only through a political lens", "C. By using comparative study to analyze the diverse ways humans live", "D. By exclusively studying historical events"],
                    "correct": "C. By using comparative study to analyze the diverse ways humans live"
                },
                {
                    "question": "7. Which of the following is a key misconception about anthropology?",
                    "answers": ["A. It only studies biological evolution", "B. It is irrelevant to understanding contemporary social issues", "C. It studies only primitive societies", "D. It is not concerned with human culture"],
                    "correct": "B. It is irrelevant to understanding contemporary social issues"
                },
                {
                    "question": "8. What does anthropology aim to explain about human beings?",
                    "answers": ["A. Why humans are physically different from other species", "B. The exact role of human language in society", "C. How and why humans are both similar and different across cultures and environments", "D. The specific causes of human conflict"],
                    "correct": "C. How and why humans are both similar and different across cultures and environments"
                },
                {
                    "question": "9. Which of the following is NOT considered a product of social groups analyzed by anthropology?",
                    "answers": ["A. Material objects (material cultures)", "B. Non-material creations (beliefs, social values)", "C. Biological inheritance", "D. Social institutions and practices"],
                    "correct": "C. Biological inheritance"
                },
                {
                    "question": "10. How does anthropology primarily differ from disciplines like political science and economics?",
                    "answers": ["A. Anthropology exclusively focuses on cultural aspects", "B. Anthropology examines human existence from both a biological and cultural perspective", "C. Anthropology only studies primitive human societies", "D. Anthropology is less concerned with human behavior"],
                    "correct": "B. Anthropology examines human existence from both a biological and cultural perspective"
                },
            ]

            for i, q in enumerate(questions_data):
                Question.objects.create(
                    quiz=quiz,
                    question_text=q['question'],
                    answers=q['answers'],
                    correct_answer=q['correct'],
                    order=i
                )

            self.stdout.write(self.style.SUCCESS(f'Successfully loaded quiz with {len(questions_data)} questions'))
        else:
            self.stdout.write('Quiz already exists')