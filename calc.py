#imports

#global vars

#fucntions
def print_menu():
    print('*******')
    print("Welcome - PyCalc")
    print('*******')

    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')

    print('[5] Calculate Age')

    print('[x] Exit')

def clear():
    print('\n' * 50)
    # HW: Python clear console
    # HW2: for option 5, ask user for birth year & display age under the elif

#instructions
opc = ''

while(opc != 'x'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1' or opc == '2' or opc == '3' or opc == '4'):
        num1 = float(input("Input your first number "))
        num2 = float(input("Input your second number "))
        if(opc == '4' and num2 == 0):
            while(num2 == 0):
                print("Error, do not divide by 0")
                num2 = float(input("Input your second number "))
    elif(opc == '5'):
        num3 = int(input("Input your birth year "))

    if(opc == '1'):
        print(num1 + num2)
    elif(opc == '2'):
        print(num1 - num2)
    elif(opc == '3'):
        print(num1 * num2)
    elif(opc == '4'):
        print(num1 / num2)
    elif(opc == '5'):
        print(2020 - num3)

    if(opc !='x'):
        input("Press Enter to return to the Main Menu")





print("Good Bye!")