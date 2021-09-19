#Welcome
print('Welcome to my computer Quiz!')

#Want to play?
playing = input('Do you want to play? ')
if playing.lower != 'yes':
    quit()
print("Okay! Let's play")

#Score is 0 at first
score = 0

#Question 1
answer1 = input('What is 1+1? ')
if answer1 == '2':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

#Question 2
answer2 = input('What is 2+2? ')
if answer2 == '4':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

#Question 3
answer3 = input('What is 3+3? ')
if answer3 == '6':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

#Question 4
answer4 = input('What is 4+4? ')
if answer4 == '8':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

#Question 5
answer5 = input('What is 5+5? ')
if answer5 == '10':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
