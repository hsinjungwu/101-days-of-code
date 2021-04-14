class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        cur_quiz = self.question_list[self.question_number]
        user_answer = input(
            f"Q.{self.question_number+1}: {cur_quiz.text} (True/False)?: "
        ).lower()
        self.question_number += 1
        self.check_answer(user_answer, cur_quiz.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That is wrong")
        print(f"The right answer is {answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n\n")
