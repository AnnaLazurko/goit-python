a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c
x1 = (-b + D**0.5) / 2**a
x2 = (-b - D**0.5) / 2**a

print(f"x = {float(x1)}; x2 = {float(x2)}")