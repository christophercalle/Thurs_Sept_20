def calculator(first_number, operator, second_number):
    correct_operator = False

    def divide(num1,num2):
    
        print(num1 / num2)
        
    def add(num1,num2):
        print(num1 + num2)
        
    def subtract(num1,num2):
       
        print(num1 - num2)

    def multiply(num1,num2):
     
        print(num1 * num2)
        
    if operator == "+":
        correct_operator = True
        add(first_number,second_number)

    
    if operator == "-":
        correct_operator = True
        subtract(first_number,second_number)

    if operator == "*":
        correct_operator = True
        multiply(first_number,second_number)

    
    if operator == "/":
        correct_operator = True
        divide(first_number,second_number)

    if correct_operator == False:
        newOperator = input("incorrect operator, please choose +, -, *, / ")
        calculator(first_number, newOperator, second_number)

    
while True:
    try:
        first_number = int(input("Give me a number: "))
        operator = input("Give me a math operator: choose +, -, *, / ")
        second_number = int(input("Give me another number: "))
        calculator(first_number, operator, second_number)
    except ValueError:
       print("That's not an int!")

