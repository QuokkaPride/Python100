class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        return user_answer

    def check_answer(self, user_answer):
        question = self.question_list[self.question_number-1]
        if user_answer == question.answer:
            self.score += 1
            print(f"Correct. Your score: {self.score}")
            
        else:
            self.score -= 1
            print(f"Wrong. Your score: {self.score}")

    def still_has_questions(self):
        return self.question_number <= len(self.question_list)
