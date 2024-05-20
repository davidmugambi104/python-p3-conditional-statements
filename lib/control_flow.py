#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
        
def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif temperature >= 40 and temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    
    # Manually capitalize the first letter
    response = response.capitalize()
    
    return f"It's {response} out there!"

    
def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        num="FizzBuzz"

    elif num % 3 == 0:
        num="Fizz"

    elif num % 5 == 0:
        num="Buzz"
    else:
        print(num)

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Cannot divide by zero!")
            return None
    else:
        print("Invalid operation!")
        return None

        
