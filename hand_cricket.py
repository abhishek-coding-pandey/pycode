import random
import math
i=0
a=0
runs=[1,2,3,4,5,6]
score=list()
computerscore=list()
totalhuman=(0)

print("welcome to hand cricket game")
print("---------------")
print ("how many overs match you want to play")
overs=int(input())
print("---------------")
while i<=overs*6:
        print("your hit")
        hit=int(input())
        cbowl=random.choice(runs)
        print ("computer threw=",cbowl,"your hit",hit)
        if hit is not cbowl:
            score.append(hit)
            i=i+1
            print(score)
        if hit==cbowl:
            print("you are out ")
            break
            print ("computer batting")
        if i>=overs*6:
            break
print("----------------------------------")
print("computer bating")     
while i<=overs*6: 
    print(" your throw")
    ball=(int(input())) 
    computerhits=(random.choice(runs))
    if computerhits==ball:
        print("you threw",ball,"computer hits",computerhits)
        print("computer out")
        break
    if computerhits is not ball:
        print("you threw",ball,"computer hits",computerhits)
        computerscore.append(computerhits)
        a=a+1
        print (computerscore)
    if a>=overs*6:
        break
print("match over")
print("-------------------------------------------")
