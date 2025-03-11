num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))

positivo = num1 >0 and num2 >0
print(f"los dos numeros son positivos {positivo}")

solo_uno = (num1 >0 and num2 <0) or (num1 <0 and num2 >0)
print(f"solo 1 de los numeros es positivos {solo_uno}")

negativo = not num1 >0 
print(f" el primero es negativos {negativo}")