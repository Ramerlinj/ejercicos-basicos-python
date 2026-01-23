import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
vida_media = 3.82  # días
N0 = 1000          # Bq/m^3 inicial
N = 125            # Bq/m^3 final

# Cálculo del tiempo transcurrido
t = vida_media * np.log(N / N0) / np.log(0.5)

# Rango para el gráfico
tiempo = np.linspace(0, t * 1.3, 300)
concentracion = N0 * (0.5) ** (tiempo / vida_media)

# Gráfico estilo GeoGebra
plt.figure()
plt.plot(tiempo, concentracion)
plt.scatter([t], [N])
plt.axhline(N)
plt.axvline(t)

plt.xlabel("Tiempo (días)")
plt.ylabel("Concentración de Radón-222 (Bq/m³)")
plt.title("Desintegración del Radón-222")
plt.show()

