calificacion = int(input("Ingresa tu calificación: "))

if calificacion > 90 and calificacion <= 100:
    print("Excelente")
elif calificacion >= 80 and calificacion < 90:
    print("Aprobado")
elif calificacion < 70 and calificacion >= 0:
    print("reprobaste")
else:
    print("Calificación inválida")