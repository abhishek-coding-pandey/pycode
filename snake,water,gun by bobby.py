import random
print("this is a snake water gun vs computer")
i=0
ll=int(input("type the number of rounds u want:"))
ele= ["snake","water","gun"]
lst=[]
list1=list(lst)

while(i<=ll):
    t="tie"
    c="computer won"
    y="you won"
    mymove=input("type snake or water or gun\n")
    computermove=random.choice(ele)
    print("-------------------------")
    print("your move:"+mymove)
    print("computer's move:"+computermove)
    print("-------------------------")

        
    if computermove=="snake":
        
        if mymove.lower()==ele[0]:
            print(t)
            list1.append(t)
            i=i+1
        elif mymove.lower()==ele[1]:
            print(c)
            list1.append(c)
            i=i+1
        elif mymove.lower()==ele[2]:
            print(y)
            list1.append(y)
            i=i+1
        else:
            print("pls type snake or water or gun")
            
    elif computermove=="water":
        
        if mymove.lower()==ele[1]:
            print(t)
            list1.append(t)
            i=i+1
        elif mymove.lower()==ele[0]:
            print(y)
            list1.append(y)
            i=i+1
        elif mymove.lower()==ele[2]:
            print(c)
            list1.append(c)
            i=i+1
        else:
            print("pls type snake or water or gun")
            
    else:
        
        if mymove.lower()==ele[2]:
            print(t)
            list1.append(t)
            i=i+1
        elif mymove.lower()==ele[1]:
            print(y)
            list1.append(y)
            i=i+1
        elif  mymove.lower()==ele[0]:
            print(c)
            list1.append(c)
            i=i+1
        else:
            print("pls type snake or water or gun")
            
            
    if i>=ll:
        print("tournament over")
        break
    

    

print(list1)
v=list1.count(y)
print("number of times u won is",v)
u=list1.count(c)
print("number of times computer won is",u)
a=list1.count(t)
print("number of times it was a tie",a)

if v>u:
    print("you won the tournament")
elif v<u:
    print("computer won the tournament")
else:
    print("the tournament is tie")