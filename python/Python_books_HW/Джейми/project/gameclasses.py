class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions
    @property
    def noOfQuestions(self):
        return self._noOfQuestions
    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print('Minimum number of questions = 1')
            print('Hence, number of questions will be set to 1')
        elif value > 10:
            self._noOfQuestions = 10
            print('Maximum number of questions = 10')
            print('Hence, number of questions will be set to 10')
        else:
            self._noOfQuestions = value
class BinaryGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0
        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input(f'Please enter binary version of {base10}: ')
            while True:
                try:
                    answer = int(userResult, base = 2)
                    if answer == base10: 
                        score += 1
                    else:
                        print(f'Wrong answer. The correct answer is {base10:b}')
                    break
                except:
                    userResult = input('Wrong number was given. Please try again: ')
        return score
class MathGame(Game):
    def generateQuestions(self):
        from random import randint
        score, numberList, symbolList = 0, [0] * 5, [' '] * 4
        operatorDict = {1:'+', 2:'-', 3:'*', 4:'**'}
        for i in range(self.noOfQuestions):
            numberList = [randint(1, 9) for i in range(5)]
            for i in range(4):
                newop = operatorDict[randint(1, 4)]
                while newop == '**' and i > 0 and symbolList[i-1] == '**':
                    newop = operatorDict[randint(1, 4)]
                symbolList[i] = newop
        questionString = ''
        for i in range(5):
            if i < 5:
                questionString += str(numberList[i])
            if i < 4:
                questionString += symbolList[i]
        result = eval(questionString)
        questionString = questionString.replace('**', '^')
        userResult = input(f'Please solve this question {questionString}: ')
        while True:
                try:
                    answer = int(userResult)
                    if answer == result: 
                        score += 1
                    else:
                        print(f'Wrong answer. The correct answer is {result}')
                    break
                except:
                    userResult = input('Wrong number was given. Please try again: ')
        return score