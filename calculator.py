#Creating a calculator programm

print("------------------------------------------------------------------------------")

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("-------------------------------------------------------------------------------")
print("Choose the operation to perform")
print("Addition\t:+")
print("Subtraction\t:-")
print("Multiplacation\t:*")
print("Division\t:/")
print("Modulous\t:%")
print("--------------------------------------------------------------------------------")

operation = (input("Enter the operation to perform:"))

# def calculator_program(operation):
match operation:
        case "+":
            sum = num1 + num2
            print("The sum of two numbers is: " + str(sum))
        case "-":
            result = num1 - num2
            print("The operation of subtracting 2 numbers is: " + str(result))
        case "*":
            result = num1 * num2
            print("The result of multiplying the two numbers is: " + str(result))
        case "/":
            result = num1/num2
            print("The result of dividing two numbers is: " + str(result))
        case "%":
            result = num1%num2
            print("The modulous of the two numbers is: " + str(result))
        case _:
            print("Enter a valid operation to perform")




