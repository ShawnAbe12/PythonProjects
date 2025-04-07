from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random


question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
for i in question_bank:
    print(f"Question: {i.text}\nAnswer: {i.answer}")

random.shuffle(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"Your final score is {quiz.score}")