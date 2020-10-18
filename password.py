print("enter your email")
email=input()
print("selct password")
passwd=input()
print("want to login")
yn=input()
if yn=="yes":
    print("enter your email")
    su1=input()
    print("enter your password")
    pu1=input()
    if email==su1 and passwd==pu1:
        print("sucessfully logined")
        print("you can enter your data")
        data=input()
    else : print("login failed check email or password")
elif yn=="no":
    print("thanks for sign in")
else :print("pls answer in yes or no")