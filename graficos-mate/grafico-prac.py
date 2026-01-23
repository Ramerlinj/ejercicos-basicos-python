import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
P0 = 1200
r = 0.18
ano_inicial = 2024
ano_final = 2040

# Generar datos
anos = np.arange(ano_inicial, ano_final + 1)
t = anos - ano_inicial
poblacion = P0 * (1 + r)**t

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(anos, poblacion, marker='o', linestyle='-', color='green', label='Crecimiento de Leucaena')

# Línea de referencia de 10,000 plantas
plt.axhline(y=10000, color='red', linestyle='--', label='Umbral 10,000 plantas')

# Marcar el punto inicial
plt.scatter([2024], [1200], color='blue', zorder=5)
plt.text(2024.5, 1200, 'Inicio (2024): 1,200', va='bottom')

# Marcar el punto donde supera las 10,000 (aprox 2037)
# Calculamos el valor exacto para 2037
p_2037 = P0 * (1 + r)**(2037 - 2024)
plt.scatter([2037], [p_2037], color='orange', zorder=5)
plt.text(2035, p_2037 + 500, f'~2037: {int(p_2037)} plantas', va='bottom')

plt.title('Crecimiento Poblacional de Leucaena leucocephala en Montecristi')
plt.xlabel('Año')
plt.ylabel('Cantidad de Plantas')
plt.grid(True, alpha=0.3)
plt.legend()

# Guardar el gráfico
plt.savefig('leucaena_crecimiento.png')