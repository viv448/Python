from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in range(0, len(question_data)):
    q = question_data[item]
    text = q['question']
    answer = q['correct_answer']

    new_q = Question(q_text=text, q_answer=answer)
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)

while quiz.still_continue() and quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.questions_attempted}")

# print(question_bank)
# print(question_bank[0].text)