def add(a, b):
    return (a+b)

def sub(a, b):
    return (a-b)

def mul(a, b):
    return (a*b)

def div(a, b):
    return (a/b)

def taking_input():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your seconf number: "))
    return a,b


    

def perfoming_calculation():
    while True:
        want_to_play = input("Do you want to start calculation, Please type yes or no: ").lower()
        if want_to_play == 'yes':
            while True:
                print("Menu for the Calculator: ")
                print("1- Addition")
                print("2- Substraction")
                print("3- Multiplication")
                print("4- Division")
                print("5- Quit")

        
                choice = int(input("Enter your choice from 1 to 5: "))

                if choice == 1:
                    a,b = taking_input()
                    print(f"Addition of {a} and {b} is: {add(a,b)}")
     
                elif choice == 2:
                    a,b = taking_input()
                    print(f"Substraction of {a} and {b} is: {sub(a,b)}")
            
                elif choice == 3:
                    a,b = taking_input()
                    print(f"Multiplication of {a} and {b} is: {mul(a,b)}")
            
                elif choice == 4:
                    a,b = taking_input()
                    print(f"Division of {a} and {b} is: {div(a,b)}")

                elif choice == 5:
                    print("Ok BYE, Thank you for using this. ")
                    break

                else:
                    print("Please enter a valid oprion from 1 to 5: ")
        
        elif want_to_play == 'no':
            print("Ok bye bye, no problem! ")
            break
    
        else:
            print("please enter a valid option (yes/no): ")


name = input("Enter your name: ")
print(f"Hi! {name}, Welcome to the Simple Calculator. ")
perfoming_calculation()