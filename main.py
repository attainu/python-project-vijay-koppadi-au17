import random
import ladders
import game
import display
import sys


Target=100      #Target scrore
score=0
                #Ladder places declaration
ladder1=37
ladder2=10
ladder3=22
ladder4=21
ladder5=56
ladder6=16
ladder7=19
ladder8=19
                #snake places declartion
snake1=11
snake2=20
snake3=44
snake4=4
snake5=51
snake6=19
snake7=20
snake8=19

print("\n   *******THIS IS SNAKE AND LADDER GAME*******\n")
print("                 ##GAME RULLS\n")
print("1.TO PLAY PRESS 'D' AND PRESS ENTER TO ROLL THE DICE\n")
print('2.SCORE STARTS FROM',score ,"ENDS AT",Target,"\n")
print("3.PLACE OF HAVING LADDERS: 1 4 9 21 28 51 72 80\n")
print("4.PLACE OF HAVING SNAKES: 17 54 62 64 87 92 95 98 \n")
print("*****************GOOD LUCK******************")
count=0
while True:
    if score==Target:
        print("WOW GREATE JOB YOU WIN THE GAME")
        break
    x=input("PLAY ")
    if x=='D':
        dice = random.randint(1,6)
        if (score+dice)>Target:
            print('Over Input Dice')
            print('Dice:',dice)
            print('NOW SCORE:',score,"\n")
            print('Needed Dice: ',Target-score,"\n")
        else:
            print('Dice:',dice)
            score =score+dice
            print('NOW SCORE',score,"\n")
            if score==1:
                print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+ladder1, "\n")
                score=score+ladder1
                print('NOW SCORE:',score,"\n")
            elif score==4:
                print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+ladder2, "\n")
                score=score+ladder2
                print('NOW SCORE:',score,"\n")
            elif score==9:
                print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+ladder3, "\n")
                score=score+ladder3
                print('NOW SCORE:',score,"\n")
            elif score==21:
                print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+ladder4, "\n")
                score=score+ladder4
                print('NOW SCORE:',score,"\n")
            elif score==28:
                print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+ladder5, "\n")
                score=score+ladder5
                print('NOW SCORE:',score,"\n")
            elif score==51:
                print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+ladder6, "\n")
                score=score+ladder6
                print('NOW SCORE:',score,"\n")
            elif score==72:
                print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+ladder7, "\n")
                score=score+ladder7
                print('NOW SCORE:',score,"\n")
            elif score==80:
                print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+ladder8, "\n")
                score=score+ladder8
                print('NOW SCORE:',score,"\n")

                #snake cammends
            elif score==17:
                print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-snake1, "\n")
                score=score-snake1
                print('NOW SCORE:',score)
            elif score==54:
                print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-snake2, "\n")
                score=score-snake2
                print('NOW SCORE:',score)
            elif score==62:
                print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-snake3, "\n")
                score=score-snake3
                print('NOW SCORE:',score)
            elif score==64:
                print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-snake4, "\n")
                score=score-snake4
                print('NOW SCORE:',score)
            elif score==87:
                print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-snake5, "\n")
                score=score-snake5
                print('NOW SCORE:',score)
            elif score==93:
                print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-snake6, "\n")
                score=score-snake6
                print('NOW SCORE:',score)
            elif score==95:
                print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-snake7, "\n")
                score=score-snake7
                print('NOW SCORE:',score)
            elif score==98:
                print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-snake8, "\n")
                score=score-snake8
                print('NOW SCORE:',score)
    else:
            print("Wrong Input..Please Press 'D' \n")
    count+=1
print("NO.OF DICE ROLLED:",count,"\n")      
print("                            ##  THE GAME END  ##                        \n") 

x=input() #it will help  when run in idle to see winner messege