#tuplas
tupla1 = ()
print(tupla1)

tupla2 = ("una cadena",123,4.9,True)#una tupla heterogenea
print(tupla2)
print(tupla2[1])
print(tupla2[3])
print(tupla2[2])
#enlazar tuplas
tupla3 = (0,1,2,3)
tupla4 = ("a","b","c")
tupla5 = (tupla3,tupla4)
print(tupla5)

print(tupla5[1][1])#muestra de la tupla 2 el elemento en el indice 1
print(tupla5[0][3])#mestra de la tupla 3 el elemento en el indice 3

#operaciones con las tuplas
tupla6 = ("a","b","c","d","e")
tupla7 =(1,2,3,4,5)
tupla8=tupla6+tupla7 #concatenar

print(tupla8)
print(tupla8[8])

#repetir una tupla
tupla9 = (1,2,3,4,5)
tupla10 = tupla9*3
print(tupla10)

#comparar una tupla
tupla11 =  ("Rojas",)
tupla12 = (123,)
tupla13 = ("Rosas",)
tupla14 = ("rosas",)
print((tupla11,tupla12)<(tupla13,tupla14))
print((tupla13,tupla14)==(tupla11,tupla12))