def credit():
    print("$ Enter money")
    s = input("=>")
    print(s)

def debit():
    pass

def check():
    pass

def main():
    turn =True
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
            credit()
        elif choice == 2:
            debit()
        elif choice == 3:
            check()
        elif choice == 4:
            break
        else:
            print("Invalid choice")


main()