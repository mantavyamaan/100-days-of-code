from quiz_brain import Quiz
from question_model import Questions
from data import question_data

question_bank=[]
for i in range(len(question_data)):
    question_bank.append(Questions(question_data[i]["question"],question_data[i]["answer"]))

print("Welcome to the Quiz")
quiz=Quiz(question_bank)
quiz.ask_question()

print("Thank you for playing!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}\n")