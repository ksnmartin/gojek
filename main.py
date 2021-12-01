class user:
    def __init__(self, name, uid,dollar=0,cents=0,max_balance=10**9):
        self.name = name
        self.uid = uid
        self.balance = {"d": dollar, "m": max_balance,"c":cents}

    def __str__(self):
        return f"{self.name} is {self.uid}"
    
    def deposit(self, amount):
        print(f"{self.name} is depositing {amount}")

    def withdraw(self, amount):
        print(f"{self.name} is withdrawing {amount}")
    
    def getBalance(self):
        print(f"{self.name}'s balance is {self.balance}")

    def __del__(self):
        print("User object destroyed")

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

def credit(customer,amount=None):
    if not amount:
        c,d = parse()
    else:
        c,d = amount
    if not c and not d:
        return
    tmpd = customer.balance["d"]+d
    tmpc = customer.balance["c"]+c
    if tmpc < 0:
        tmpd-=1
        tmpc+=100
    if tmpc>customer.balance["m"] or tmpd>customer.balance["m"]:
        print("$ Max amount is " + str(customer.balance["m"]) + "D" )
        return
    customer.balance["d"]=tmpd
    customer.balance["c"]=tmpc
    print("$ Done")

def debit(customer,amount=None):
    if not amount:
        c,d = parse()
    else:
        c,d = amount
    if not c and not d:
        return
    tmpd = customer.balance["d"]-d
    tmpc = customer.balance["c"]-c
    if tmpc < 0:
        tmpd-=1
        tmpc+=100
    if tmpc>customer.balance["m"] or tmpd>customer.balance["m"]:
        print("$ Max amount is " + str(customer.balance["m"]) + "D" )
        return
    customer.balance["d"]=tmpd
    customer.balance["c"]=tmpc
    print("$ Done")

def check(customer):
    customer.getBalance()

def transfer(sender,receiver,amount):
    debit(sender,amount)
    credit(receiver,amount)


def run():
    bank =[user("John",1),user("Jane",2),user("Jack",3)]
    while True:
        try:
            uid = int(input("$ Enter your uid: "))
            u = bank[uid-1]
            print("""
$ Select an option:
1. Credit
2. Debit
3. Check
4. Transfer
5. Exit
            """)
            choice = int(input("=>"))
            if choice == 1:
                credit(u)
            elif choice == 2:
                debit(u)
            elif choice == 3:
                check(u)
            elif choice == 4:
                reciver_uid = int(input("$ Enter receiver's UID: "))
                reciver = bank[reciver_uid-1]
                amount = parse()
                if amount == (None,None):
                    continue
                transfer(u,reciver,amount)
            elif choice == 5:
                print("$ Thank you!")
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print("Please enter valid input :" )


if __name__ == "__main__":
    run()

