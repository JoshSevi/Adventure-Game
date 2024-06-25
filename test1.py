class Question:

    def __init__(self):
        self._text = ""
        self._answer = ""

    def setText(self, questionText):
        self._text = questionText

    def setAnswer(self, correctResponse):
        self._answer = correctResponse

    def checkAnswer(self, response):
        return response == self._answer

    def display(self):
        print(self._text)


class ChoiceQuestion(Question)

    def __init__(self):
    super().__init__()
    self._choices=[]

    def addChoice(self, choice, correct)
        self._choices.append(choice)
        if correct:
            choiceString=str(len(self._choices))
            self.setAnswer(choiceString)

    def display(self)
        super().display()

    for i in range(len(self._choices)):
        choiceNumber=i + 1
        print("%d: %s" %(choiceNumber, self._choices[i]))

def main():
    first.ChoiceQuestion()
    first.setText("1x1")
    first.addChoice("1", True)
    first.addChoice("0", False)
    first.addChoice("-1", False)
    first.addChoice("11", False)

    second = ChoiceQuestion()
    second.setText("3x3")
    second.addChoice("6", False)
    second.addChoice("9", True)
    second.addChoice("12", False)
    second.addChoice("18", False)

    third = ChoiceQuestion()
    third.setText("5x5")
    third.addChoice("50", False)
    third.addChoice("10", False)
    third.addChoice("55", False)
    third.addChoice("25", True)

    fourth = ChoiceQuestion()
    fourth.setText("9x2")
    fourth.addChoice("12", False)
    fourth.addChoice("16", False)
    fourth.addChoice("18", True)
    fourth.addChoice("9", False)

    fifth = ChoiceQuestion()
    fifth.setText("7x7")
    fifth.addChoice("-49", False)
    fifth.addChoice("49", True)
    fifth.addChoice("14", False)
    fifth.addChoice("77", False)

    presentQuestion(first)
    presentQuestion(second)
    presentQuestion(third)
    presentQuestion(fourth)
    presentQuestion(fifth)

    def presentQuestion(q):
        q.display()
    response=input("Your Answer: ")
    if q.checkAnswer(response) == False:
        print(q.checkAnswer(response))
    presentQuestion(q)
    elif q.checkAnswer(response) == True:
        print(q.checkAnswer(response))

    main()
