# TODO :Asking the question
# TODO : checking if the answer was correct
# TODO : checking if we're the end of the quiz


class QuizBrain:

    def __init__(self,questions_list):
        self.questions_list = questions_list
        self.questions_number =0

    def still_has_questions(self):
        question_num = self.questions_number
        total_questions = len(self.questions_list)
        if (question_num>=total_questions):
            return False
        return True
            


    def next_question(self):

        current_question =self.questions_list[self.questions_number].question
        self.questions_number+=1
        
        question = f"Q.{self.questions_number}: {current_question} (True/False)?:"
        # item = self.questions_list[self.questions_number]
        user_input=input(question)
        