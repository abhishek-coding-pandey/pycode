
print("what is our name")
na=input()
print("your age")
ag=int(input())
print("gender")
ge=input()
print("email")
date= input()
print("Do you want your information")
final= input()
if final=="yes":
    print("name =",na)
    print("age =",ag)
    print("gender=",ge)
    print("email=",date)
    print("thanks")
elif final=="no":
    print("thanks your data is safe with us")
else :
    print("please input yes or no")


