def newGame():
    
    guesses=[]
    correct_guesses=0
    Question_num=1

    for key in Question:
        print('---------------------')
        print(key)
        for i in options[Question_num-1]:
            print(i)
        guess=input('enter (A,B,C or D) :')
        guess=guess.upper()
        guesses.append(guess)

        correct_guesses+= check_answer(Question.get(key),guess)
        Question_num+=1    

    display_score(correct_guesses,guesses)
#!--------------------------------
def check_answer(answer,guess):
    if answer==guess:
        print('CORRECT')
        return 1
    else:
        print('wrong!!')
        return 0
 #!--------------------------------
def display_score(correct_guesses,guesses):
    print('--------------------------------')
    print('RESULTS')
    print('--------------------------------')
    print("Answers: ",end="")
    for i in Question:
        print(Question.get(i),end=' ')
    print()

    print("Guesses: ",end="")
    for i in guesses:
        print(i,end=' ')
    print()  

    score=int((correct_guesses/len(Question))*100)
    print('Your score is : '+str(score)+'%')
#!--------------------------------
def play_again():
    reponse=input('do you you want play again :')
    reponse=reponse.upper()

    if reponse=='YES':
        return True
    else:
        return False
#!--------------------------------


Question ={
    'who created Python?: ':'A',
    'what year was Python created?: ':'B',
    'Python is tributed to which comedy group?: ':'C',
    'is the Earth round?: ':'A',
}

options = [
    ['A. Guido van Rossum', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark Zuckerberg'],
    ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
    ['A. Lonely Islands', 'B. Smosh', 'C. Monty Python', 'D. SNL'],
    ['A. true', 'B. False', 'C. something', "D. what's Earth"]
]


newGame()

while play_again():
    newGame()

print('Byyeee!')