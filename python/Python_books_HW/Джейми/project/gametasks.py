'''
Ver-1
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'userScores.txt')
def printInstructions(instructions):
    print(instructions)
def getUserScore(userName):
    for line in open(file_path, 'r'):
        lineName, lineScore = line.strip().split(', ')
        if lineName == userName:
            return lineScore
    return -1
print(getUserScore('Carol'))
def updateUserScore(newUser, userName, score):
    if newUser == True:
        file = open(file_path, 'a')
        file.write('{}, {}'.format(userName, score))
        file.close()
    else:
        tmpfile_path = file_path.replace('txt', 'tmp')
        tmpfile = open(tmpfile_path, 'w')
        for line in open(file_path, 'r'):
            lineName, lineScore = line.strip().split(', ')  
            if lineName == userName:
                lineScore = score
                tmpfile.write('{}, {}\n'.format(lineName, lineScore))
            else:
                tmpfile.write('{}, {}\n'.format(lineName, lineScore))
        os.remove(file_path)
        tmpfile.close()
        tmpfile_path2 = file_path.replace('tmp', 'txt')
        os.rename(tmpfile_path, tmpfile_path2)
updateUserScore(False, 'Benny', 158)
'''
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'userScores.txt')
def printInstructions(instructions):
    print(instructions)
def getUserScore(userName):
    for line in open(file_path, 'r'):
        lineName, lineScore = line.strip().split(', ')
        if lineName == userName:
            return lineScore
    return -1
def updateUserScore(newUser, userName, score):
    if newUser == True:
        with open(file_path, 'a') as f:
            print(f'\n{userName}, {score}', file=f)
    else:
        tmpfile_path = file_path.replace('txt', 'tmp')
        with open(tmpfile_path, 'w') as tmp, open(file_path, 'r') as orig:
            for line in orig:
                lineName, lineScore = line.strip().split(', ')  
                if lineName == userName:
                    lineScore = score
                    print(f'{lineName}, {lineScore}', file=tmp)
                else:
                    print(f'{lineName}, {lineScore}', file=tmp)
        os.remove(file_path)
        tmpfile_path2 = file_path.replace('tmp', 'txt')
        os.rename(tmpfile_path, tmpfile_path2)