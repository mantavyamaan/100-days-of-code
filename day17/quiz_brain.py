class Quiz():
    def __init__(self,question_list):
        self.question_list = question_list
        self.score = 0
        self.question_number = 0

    def ask_question(self):
        for i in self.question_list:
            answer=input(f"Q{self.question_number+1}: {self.question_list[self.question_number].question} (True/False)?\n").lower()
            if answer==self.question_list[self.question_number].answer:
                self.score+=1
                print("You got it right!")
            else:
                print("Sorry, that's wrong.")
            print(f"The correct answer was: {self.question_list[self.question_number].answer}")
            print(f"Your current score is: {self.score}/{self.question_number+1}\n")
            self.question_number+=1