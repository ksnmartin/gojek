def parse():
    print("$ Enter money")
    s = input("=>")
    d = ""
    c= ""
    n= len(s)
    x=0
    for i in range(n):
        if s[i]=="D":
            x=i+1
            break
        else:
            d+=s[i]
    for j in range(x,n):
        if s[j]=="C":
            break
        else:
            c+=s[j]
    if c=="":
        c="0"
    if d=="" or "C" in d:
        d="0"
    return int(c),int(d)

def credit(balance):
    c,d = parse()
    balance["d"]+=d
    balance["c"]+=c
    print("$",d,"Dollars and",c,"Cents")

def debit(balance):
    c,d=parse()
    balance["d"]-=d
    balance["c"]-=c
    print("$",d,"Dollars and",c,"Cents")

def check(balance):
    print("$ Current balance is ",balance["d"],"D",balance["c"],"C")

def main():
    turn =True
    balance = {"d":0,"c":0}
    while turn:
        print("""
$ Select an option:
1. Credit
2. Debit
3. Check
4. Exit
        """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            credit(balance)
        elif choice == 2:
            debit(balance)
        elif choice == 3:
            check(balance)
        elif choice == 4:
            break
        else:
            print("Invalid choice")


main()