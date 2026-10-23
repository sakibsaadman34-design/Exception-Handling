try:
    num1 = int(input("Enter Number 1: "))
    
    num2 = int(input("Enter Number 2: "))

    result = num1 / num2

    print(f"Result = {result}")

except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please Enter Valid Numbers.")
except:
    print("No Input")
else:
    print("No exception")
finally:
    print("This code will execute no matter what")