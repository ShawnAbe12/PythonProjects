class QuizBrain():
    def __init__(self, questions_lists):
        self.question_number = 0
        self.questions_lists = questions_lists
        self.score = 0

    def check_answer(self, choice, correct_choice):
        return choice == correct_choice

    def still_has_questions(self):
        return self.question_number < len(self.questions_lists)

    def next_question(self):
        question_num = self.question_number + 1
        question_text = self.questions_lists[self.question_number].text
        question_answer = self.questions_lists[self.question_number].answer
        choice = input(f"Q.{question_num}: {question_text} (True/False)?:").lower()
        if choice == "off":
            self.question_number = len(self.questions_lists)
        elif self.check_answer(choice[0].lower(), question_answer[0].lower()) and self.still_has_questions():
            print("You Got it Right!!")
            self.question_number += 1
            self.score += 1
        else:
            self.question_number += 1
            print(f"You failed. The correct answer is {question_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
