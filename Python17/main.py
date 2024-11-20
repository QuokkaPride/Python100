from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# create quesiton bank containgin a list of question objects
question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    user_answer = quiz.next_question()
    quiz.check_answer(user_answer)
