def parse():
    print("$ Enter an amount")
    s = input("=>")
    d = ""
    c= ""
    n= len(s)
    x=0
    for i in range(n):
        if s[i] == " ":
            continue
        elif s[i]=="D":
            x=i+1
            break
        elif s[i].isdigit() or s[i]=="-":
            d+=s[i]
        else:
            print("Please enter valid input")
            return None,None
    for j in range(x,n):
        if s[j] == " ":
            continue
        elif s[j]=="C":
            break
        elif s[j]=="-":
            c+="-"
        elif s[j].isdigit() or s[j]=="-":
            c+=s[j]
        else :
            print("Please enter valid input")
            return None,None
    if c=="":
        c="0"
    if d=="" or "C" in d:
        d="0"
    c,d=int(c),int(d)
    if c > 99:
        d+=c//100
        c = c%100
    return c,d

def credit(balance):
    c,d = parse()
    if not c and not d:
        return
    tmpd = balance["d"]+d
    tmpc = balance["c"]+c
    if tmpc>balance["m"] or tmpd>balance["m"]:
        print("$ Max amount is " + str(balance["m"]) + "D" )
        return
    balance["d"]=tmpd
    balance["c"]=tmpc
    print("$ Done")

def debit(balance):
    c,d=parse()
    if not c and not d:
        return
    balance["d"]-=d
    balance["c"]-=c
    print("$ Done")

def check(balance):
    print("$ Current balance is "+str(balance["d"])+"D "+str(balance["c"])+"C")

def main():
    balance = {"d":0,"c":0,"m":10**9}
    while True:
        try:
            print("""
$ Select an option:
1. Credit
2. Debit
3. Check
4. Exit
            """)
            choice = int(input("=>"))
            if choice == 1:
                credit(balance)
            elif choice == 2:
                debit(balance)
            elif choice == 3:
                check(balance)
            elif choice == 4:
                print("$ Thank you!")
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print("Please enter valid input :" )


main()