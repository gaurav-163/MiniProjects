import random

print ("Welcome to SNAKE WATER GUN Game")
# loop = int(input("Enter number of rounds: "))

Human_score = 0
pc_score = 0
loop = 0

while(loop<9):

    Human = input("Enter You're choice from below\n s\n w\n g\n")
    pc = random.choice(['snake', 'water', 'gun'])
    
    if (Human == 's' and pc == 'water'):
        print (f"Human wins this turn as it selects {Human} and pc selects {pc}")
        print (f"Human has Earn a point {Human_score}")
        Human_score +=1
        loop +=1

    elif (Human == 's' and pc == 'gun'):
        print (f"Human wins this turn as it selects {Human} and pc selects {pc}")
        print (f"Human has Earn a point {Human_score}")
        Human_score +=1
        loop +=1

    elif (Human == 'g' and pc == 'snake'):
        print (f"Human wins this turn as it selects {Human} and pc selects {pc}")
        print (f"Human has Earn a point {Human_score}")
        Human_score += 1
        loop +=1

    elif (Human == 'g' and pc == 'water'):
        print (f"Computer wins this turn as it selects {pc} and human selects {Human}")
        print (f"Computer has Earn a point {pc_score}")
        pc_score += 1
        loop +=1

    elif (Human == 'w' and pc == 'gun'):
        print (f"Human wins this turn as it selects {Human} and pc selects {pc}")
        print (f"Human has Earn a point {Human_score}")
        Human_score +=1
        loop +=1

    elif (pc == 'snake' and Human == 'w'):
        print (f"Computer wins this turn as it selects {pc} and human selects {Human}")
        print (f"Computer has Earn a point {pc_score}")
        pc_score += 1
        loop +=1

    elif (pc == 'gun' and Human == 's'):
        print (f"Computer wins this turn as it selects {pc} and human selects {Human}")
        print (f"Computer has Earn a point {pc_score}")
        pc_score += 1
        loop +=1

    elif (pc == Human or Human == pc):
        print (f"Tie as it selects {pc} and human selects {Human}")
        loop +=1

print (f"\nThe Score are\n Human Score is {Human_score}\n Computer Score is {pc_score}\n")
if (Human_score<pc_score):
    print ("Computer Win")

elif (Human_score>pc_score):
    print("Human Win")

else:
    print("Tie")