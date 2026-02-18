import gameclasses as gc
import gametasks as gt
try:
    mathInstructions = '''
В этой игре вам предлагается решить простую
арифметическую задачу.
За каждый правильный ответ вам начисляется одно очко.
За ошибочные ответы очки не вычитаются.
'''
    binaryInstructions = '''
В этой игре вы получаете десятичное число.
Ваша задача — преобразовать его в двоичную систему
счисления.
За каждый правильный ответ вам начисляется одно очко.
За ошибочные ответы очки не вычитаются.
'''
    bg, mg = gc.BinaryGame(), gc.MathGame()
    userName = 'Ilia'
    score = int(gt.getUserScore(userName))
    if score == -1:
        score = 0
        newUser = True
    else:
        newUser = False
    currScore = 0
    userChoice = ''
    while userChoice != '-1':
        game = input('Math Game (1) or Binary Game (2)? ')
        while game == '1' or game == '2':
            numPrompt = int(input('How many questions do you want per game (1 to 10)? '))
            if game == '1':
                mg.noOfQuestions = numPrompt
                gt.printInstructions(mathInstructions)
                currScore += mg.generateQuestions()
            else:
                bg.noOfQuestions = numPrompt
                gt.printInstructions(binaryInstructions)
                currScore += bg.generateQuestions()
            userChoice = input('If you want to quit enter -1: ')
            if userChoice == '-1': break
    gt.updateUserScore(newUser, userName, str(currScore))
except:
    print('Got some error')