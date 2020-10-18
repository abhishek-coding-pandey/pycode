import random
a = 0
humanscore = list()
times = print(int(input("how many times you want to play")))
elements = ["rock", "paper", "scissors"]
while a <= 10:
    y = ("you won")
    l = ("you lose")
    t = ("tie")
    print("-------------------------")
    print("chosse one among rock,paper,scissors")
    print("-------------------------")
    user = input()
    computer = random.choice(elements)
    print("-------------------------")
    print("you took", user)
    print("computer took", computer)
    print("-------------------------")
    if computer == user:
        print("the match tie")
        a = a+1
        humanscore.append(t)
    if computer == "rock" and user == "scissors":
        print("you lose")
        a = a+1
        humanscore.append(l)

    if computer == "rock" and user == "paper":
        print("you win")
        a = a+1
        humanscore.append(y)
    if computer == "scissors" and user == "paper":
        print("you lose")
        a = a+1
        humanscore.append(l)
    if computer == "scissors" and user == "rock":
        print("you win")
        a = a+1
        humanscore.append(y)
    if computer == "paper" and user == "rock":
        print("you lose")
        a = a+1

        humanscore.append(l)
    if computer == "paper" and user == "scissors":
        print("you win")
        humanscore.append(y)

    if a >= 10:
        break

u= humanscore.count(y)
v=humanscore.count(l)
print("\n\n\n over all score ")
print("-----------------------")
print("your total score:",u)
print("computer total score:",v)
print("------------------------")
if u>v:
    print("you won this tournament")
    print("--------------------------")
else: print("you lose the tournament") 
print("-------------------------")   