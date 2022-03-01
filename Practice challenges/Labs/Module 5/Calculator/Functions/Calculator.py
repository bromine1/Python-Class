def calculator():
    import decimal
    try:
        num1 = decimal(input("Please input the first number"))
        num2 = decimal(input("Please input the second number"))
    except:
        print("Something went wrong")
        calculator()
    