#Example #4 Ciso NetAcad 2.7.1.5 (raise)
def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")
