nombre = 'Hola Mundo'

print(nombre.upper()) #todas mayusculas
print(nombre.lower()) #todas minusculas
print(nombre.capitalize()) #primera letra mayuscula
print(nombre.find('m')) #busca la letra m
nombre_nuevo = nombre.replace('Hola', 'Hola Mundo')
print(nombre_nuevo, nombre) #reemplaza Hola por Hola Mundo
print('Mundo' in nombre) #verifica si Mundo esta en la variable nombre