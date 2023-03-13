# TODO :Asking the question
# TODO : checking if the answer was correct
# TODO : checking if we're the end of the quiz


class QuizBrain:

    def __init__(self,questions_list):
        self.questions_list = questions_list
        self.questions_number =0
        self.user_score =0

    def still_has_questions(self):
        question_num = self.questions_number
        total_questions = len(self.questions_list)
        if (question_num>=total_questions):
            return False
        return True
            


    def next_question(self):

        current_question =self.questions_list[self.questions_number]
        self.questions_number+=1
        
        question = f"Q.{self.questions_number}: {current_question.question} (True/False)?:"
        # item = self.questions_list[self.questions_number]
        user_answer=user_input=input(question)
        self.check_answer(user_answer,current_question.answer)


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.user_score +=1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.user_score}/{self.questions_number}")
        print("\n")
            
        