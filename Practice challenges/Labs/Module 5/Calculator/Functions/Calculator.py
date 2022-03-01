def calculator():
    # Initialize data and modules
    import decimal
    try:
        a = decimal.Decimal(input("\nPlease input the first number: "))
        b = decimal.Decimal(input("\nPlease input the second number: "))
    except:
        print("Something went wrong")
        calculator()
    print("\nPlease choose an operation:\n")
    operations = {'add': a + b, 'subtract': a - b,'multiply': a * b, 'divide': a/b}
    for x in operations.keys():
        print (f"{x}\n")
    return(operations[input("\nType the given name of your operation: ")])

print(f"Your result is {calculator()}")