#This first function is a simple math to convert C to Farenheit
def celcius_to_fahrenheit(celcius):
    return (celcius*9/5) + 32
#This second one does the F to C conversion
def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit-32)*5/9
#This code fetches the user's input on which code(conversion) to run.
choice = input("Choose conversion type: 1 for C TO F, 2 for F TO C: ")
#if the user choice is 1 then the first function is executed in the if statement .
if choice == "1":
    celcius_value = float(input("Enter Temp in Celcius: "))
    result = celcius_to_fahrenheit(celcius_value)
    print(f"{celcius_value} Celcius is equal to {result} Fahrenheit")
#if the user choice is 2 then this function is executed
elif choice == "2":
    fahrenheit_value = float(input("Enter Temp in Fahrenheit: "))
    result = fahrenheit_to_celcius(fahrenheit_value)
    print(f"{fahrenheit_value} Fahrenheit is equal to {result} Celcius")
#if the user inputs an answe that is not part of the two options, this code is executed
else:
    print("Invalid choice. Please enter 1 or 2 for conversion type.")