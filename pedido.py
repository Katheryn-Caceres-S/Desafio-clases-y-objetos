from te import Te

print("""
Elige el sabor de te 
      1 = te negro 
      2 = te verde 
      3 = agua de hierbas)
""")

sabor = int(input("elige un sabor: "))

print("""
Elige un formato (300 o 500)
""")
formato = int(input("elige formato: "))


nombre, tiempo, recomendacion = Te.receta(sabor)

precio = Te.obtener_precio(formato)

duracion = Te.duracion
print(f"""
a. Sabor del tipo de té: {nombre}
b. Formato: {formato}
c. Precio: {precio}
d. Tiempo: {tiempo}
e. Recomendación: {recomendacion}
f. duracion: {duracion}
""")