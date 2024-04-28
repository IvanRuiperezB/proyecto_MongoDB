#Iván Ruipérez Benítez
from pymongo import MongoClient
import sys
import pprint
def menu():
    print()
    print('''Menú
    1. Insertar receta.
    2. Borrar receta.
    3. Modificar nombre de receta.
    4. Mostrar el nombre de las recetas con más de 3 comensales.
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

def conexionMongo():
    try:
        client = MongoClient('localhost')
        db = client.Cocina
        col = db.recetas
    except :
        print("No hay conexión con Mongo.")
        sys.exit(1)    
    return col

def opciones(num,db):
    if int(num) == 1:
        Insertar(db)
    elif int(num) == 2:
        Eliminar(db)
    elif int(num) == 3:
        Modificar(db)
    elif int(num) == 4:
        NombreRecetas(db)
    elif int(num) == 5:
        PolloDesmenuzado(db)
    elif int(num) == 6:
        IngEnsaladaCesar(db)
    elif int(num) == 7:
        ContRecetasAutor(db)
        
def Insertar(db):
    print('1')

def Eliminar(db):
    print('2')
    
def Modificar(db):
    print('3')

def NombreRecetas(db):
    doc={"servings": {"$gt": 3} }
    resultado=db.find(doc, {"_id":0,"name":1})
    for documento in resultado:
        name=documento.get("name")
        print(name)