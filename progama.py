#Iván Ruipérez Benítez
from funciones import conexionMongo,menu,opciones

db=conexionMongo()
num=0
while num != 8:
    num=menu()
    opciones(num,db)