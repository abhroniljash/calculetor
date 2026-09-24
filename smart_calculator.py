# Calcutetor creat by function method

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divided(a,b):
    return a/b

print("=== WELLCOME TO CALCULATOR ===")

#Creat a loop
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter Your Choise: ")  # user inter your choise

    
    
    if choice == "1":
        add_first = int(input("Enter Your First Digit: "))
        add_second = int(input("Enter Your Second Digit: "))
        result_add = add(add_first,add_second)  #function call
        print("Your Result: ",result_add)
        

    elif choice == "2":
        subtract_first = int(input("Enter Your First Digit: "))
        subtract_second = int(input("Enter Your Second Digit: "))
        result_subtract = subtract(subtract_first,subtract_second) #function call
        print("Your Result: ",result_subtract)


    elif choice  == "3":
        multiply_first = int(input("Enter Your First Digit: "))
        multiply_second = int(input("Enter Your Second Digit: "))
        result_multiply = multiply(multiply_first,multiply_second)  #function call
        print("Your Result: ",result_multiply)


    elif choice == "4":
        divided_first = int(input("Enter Your First Digit: "))
        divided_second = int(input("Enter Your Second Digit: "))
        #if-else condition
        if divided_first == 0: #check user inter zero
            print("Cannot divided by zero.")
        else:
            if divided_second == 0:  #check user inter zero
                print("Cannot divided by zero.")
            else:
                result_divided = divided(divided_first,divided_second)  #function call
                print("Your Result: ",result_divided)


    elif choice == "5":
        print("THANK YOU for Calculation")
        break #inter exit and breck the loop