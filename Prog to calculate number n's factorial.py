
def calculate_factorial(number):
    if number < 0:
        return "Factorial is not defined for any negative numbers"
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

user_input = int(input("Enter a number to calculate the factorial: "))
result = calculate_factorial(user_input)
print(f"The factorial of {user_input} is: {result}")
