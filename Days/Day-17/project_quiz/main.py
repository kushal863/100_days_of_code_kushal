# Create a list of question objects..
from question_model import Question

from data import question_data

question_bank =[]

# for dic in question_data:
#     question_bank.append(Question(text=dic['text'],answer=dic['answer']))


for dic in question_data:
    question_text = dic['text']
    answer_text = dic['answer']

    new_question = Question(text=question_text,answer=answer_text)

    question_bank.append(new_question)

for ques in question_bank:
    print(ques.question)
    print(ques.answer)