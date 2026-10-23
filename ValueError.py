try:
    number = int(input("Enter a number:"))

    print(f"The Number entered = {number}")

except ValueError as ex:

    print(f"Exception: {ex}")