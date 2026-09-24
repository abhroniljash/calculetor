num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
operator = input("Enter the symbol: ")

if operator == "+":
    print(num1,"+",num2 ,"=", num1+num2)
if operator == "-":
    print(num1,"-",num2 ,"=", num1-num2)
if operator == "x" or "*":
    print(num1,"x",num2 ,"=", num1*num2)
if operator == "/":
    print(num1,"/",num2 ,"=", num1/num2)