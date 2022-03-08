def calculator():
    # Initialize data and modules
    import decimal
    # gather user input
    try:
        a = decimal.Decimal(input("\nPlease input the first number: "))
        b = decimal.Decimal(input("\nPlease input the second number: "))
    except:
        print("Something went wrong")
        calculator()
    # select operator
    print("\nPlease choose an operation:\n")
    operations = {'add': a + b, 'subtract': a - b,'multiply': a * b, 'divide': a/b}
    # print operator options
    for x in operations.keys():
        print (f"{x}\n")
    # return operator output value
    return(operations[input("\nType the given name of your operation: ")])

print(f"Your result is {calculator()}")