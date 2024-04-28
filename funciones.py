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
    nombre=input("Nombre de la receta: ")
    autor=input("Autor: ")
    desc=input("Descripción: ")
    cook=input("Tiempo de cocina: ")
    while cook.isnumeric() == False:
        print("La cadena solo puede contener números.")
        cook=input("Tiempo de cocina: ")
    etiqueta=input("Etiqueta: ")
    comensales=input("Comensales: ")
    while comensales.isnumeric() == False:
        print("La cadena solo puede contener números.")
        comensales=input("Comensales: ")
    
    doc={
        "author": autor,
        "name": nombre,
        "description": desc,
        "cook_time": int(cook),
        "servings": int(comensales),
        "tags": [etiqueta]
    }
    operacion=db.insert_one(doc)
    print("Se ha insertardo correctamente.")

def Eliminar(db):
    receta=input("Nombre de la receta: ")
    try:
        doc={"name": receta}
        print("Se eliminará este documento:")
        pprint.pprint(db.find_one(doc))
        operacion=db.delete_one(doc)
        print("Se ha eliminado con éxito.")
    except:
        print("No existe esa receta.")

def Modificar(db):
    receta=input("Nombre de la receta: ")
    nuevareceta=input("Nuevo nombre: ")
    try:
        doc={"name": receta}
        act={"$set":{"name": nuevareceta}}
        print("Se modificará este documento:")
        pprint.pprint(db.find_one(doc))
        operacion=db.update_one(doc,act)
        print("")
        print("Documento tras actualización")
        pprint.pprint(db.find_one({"name":nuevareceta}))
    except:
        print("No existe esa receta.")

def NombreRecetas(db):
    doc={"servings": {"$gt": 3} }
    operacion=db.find(doc, {"_id":0,"name":1})
    for documento in operacion:
        name=documento.get("name")
        print(name)
        
def PolloDesmenuzado(db):
    doc={"tags":"Pollo desmenuzado"}
    operacion=db.find(doc, {"_id":0,"name":1})
    for documento in operacion:
        name=documento.get("name")
        print(name)
