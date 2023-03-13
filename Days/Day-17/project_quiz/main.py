# Create a list of question objects..
from question_model import Question

from data import question_data
from quiz_brain import QuizBrain

question_bank =[]

# for dic in question_data:
#     question_bank.append(Question(text=dic['text'],answer=dic['answer']))


for dic in question_data:
    question_text = dic['text']
    answer_text = dic['answer']

    new_question = Question(text=question_text,answer=answer_text)

    question_bank.append(new_question)

# for ques in question_bank:
#     print(ques.question)
#     print(ques.answer)

quiz_class = QuizBrain(question_bank)

while quiz_class.still_has_questions():
    quiz_class.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_class.user_score}/{quiz_class.questions_number}")