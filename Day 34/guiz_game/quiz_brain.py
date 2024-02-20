import html


class QuizBrain:
    def __init__(self, q_list):
        self.q_list = q_list
        self.q_number = 0
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.q_list[self.q_number]
        self.q_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.q_number}: {q_text}"

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
