nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
print(nombre, edad)
print(type(edad))

numero = int(edad)
print( numero * 3 )

string = str(numero)
print(string)

float_num = float(edad)
print(float_num + 0.5)

bool_val = bool(edad)
#? este envalua falso los string vacios, NOne, 0 y float 0.0
print(bool_val)