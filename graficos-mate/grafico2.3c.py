import numpy as np
import matplotlib.pyplot as plt

# Datos
vida_media = 12.32  # años
N0 = 1000
porcentaje = 0.25
N = N0 * porcentaje

# Tiempo transcurrido
t = vida_media * np.log(N / N0) / np.log(0.5)

# Datos para la gráfica
tiempo = np.linspace(0, t * 1.4, 300)
actividad = N0 * (0.5) ** (tiempo / vida_media)

# Gráfica estilo GeoGebra
plt.figure()
plt.plot(tiempo, actividad)
plt.scatter([t], [N])
plt.axhline(N)
plt.axvline(t)

plt.xlabel("Tiempo (años)")
plt.ylabel("Actividad de Tritio (unidades)")
plt.title("Desintegración del Tritio (³H)")
plt.show()

