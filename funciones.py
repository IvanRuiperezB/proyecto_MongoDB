#Iván Ruipérez Benítez
import pymongo

def menu():
    print()
    print('''Menú
    1. Insertar receta.
    2. Borrar receta.
    3. Modificar nombre de receta.
    4. Mostrar nombre de las recetas.
    5. Mostrar recetas con etiqueta Pollo desmenuzado.
    6. Mostrar los ingredientes de la receta Ensalada César.
    7. Mostrar el número de recetas de cada autor.
    8. Salir.''')
    num=input("Elija una opción: ")
    print()
    while num.isnumeric() == False or int(num) > 8 or int(num) < 1:
        print("Esa opción no existe.")
        num=input("Elija una opción: ")
    return int(num)