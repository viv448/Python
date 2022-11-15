
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_attempted = 0
        self.user_continue = True
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def still_continue(self):
        return self.user_continue

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
        if input(f"\nDo you want to continue playing. Type 'yes' or 'no': ") == "no":
            self.user_continue = False

    def check_answer(self, user_answer, correct_answer):
        self.questions_attempted += 1
        if user_answer.lower() == correct_answer.lower():
            print(f"You got it right!")
            self.score += 1
        else:
            print(f"That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is {self.score}/{self.questions_attempted}")


