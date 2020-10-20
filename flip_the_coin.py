import random
while(True):
    coin = ["head", "tails"]
    print("you chosse to heads or tails")
    choice = input()
    print("---------------------------------------")
    print("you chioice",choice)
    flip=print("coin flips to", random.choice(coin))
    print("------------------------------------------")
    if choice==flip:
        print("you won")
    else:print("you lose")
    print("-----------------------------------")
