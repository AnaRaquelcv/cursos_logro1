num1 = int(input("Ingrese un número: "))

menor_de_edad = not num1 >=18
print(f"Es menor de edad {menor_de_edad}")

mayor_de_edad = (num1 >=18  or num1 >=65 )
print(f"Es mayor de edad {mayor_de_edad}")