"""Quiz game with OOP"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    """Make a bank of questions"""
    question = Question(question["question"], question["correct_answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while not quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.q_number}")
