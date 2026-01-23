import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
vida_media = 5730  # años
N0 = 1000          # cantidad inicial
porcentaje_restante = 0.375

# Cálculo del tiempo
t = vida_media * np.log(porcentaje_restante) / np.log(0.5)

# Rango de tiempo para la gráfica
tiempo = np.linspace(0, t * 1.2, 300)
N = N0 * (0.5) ** (tiempo / vida_media)

# Gráfica estilo GeoGebra (simple, limpio)
plt.figure()
plt.plot(tiempo, N)
plt.scatter([t], [N0 * porcentaje_restante])
plt.axhline(N0 * porcentaje_restante)
plt.axvline(t)

plt.xlabel("Tiempo (años)")
plt.ylabel("Cantidad de Carbono-14")
plt.title("Desintegración del Carbono-14")
plt.show()
