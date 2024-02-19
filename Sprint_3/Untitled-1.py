import matplotlib.pyplot as plt

# Definimos los datos del diagrama
etiquetas = ["A", "B", "C", "D"]
valores = [25, 35, 30, 100]
colores = ["red", "green", "blue", "yellow"]

# Creamos la figura y los ejes
fig, ax = plt.subplots()

# Dibujamos el diagrama de sectores
ax.pie(valores, labels=etiquetas, colors=colores, autopct="%1.1f%%")

# Mostramos el gráfico
plt.show()
