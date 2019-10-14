
listado_personal = []
diccionario={}
     
filas = int(input("Cantidad de filas: "))



for fila in range(filas):
    fila1 = int(input("Numero: "))
    fila2 = input("Nombre: ")
    fila3 = input("Apellido: ")
    fila4 = input("Area: ")
    fila5 = input("Cargo: ")
    fila6 = input("Estado: ")
    fila1 = 'Nombre: ',fila1
    fila2 = 'Apellido: ',fila2
    fila3 = 'Area: ',fila3
    fila4 = 'Cargo: ',fila4
    fila5 = 'Cargo: ',fila5
    fila6 = 'Estado: ',fila6
    listado_personal.append(fila1   )
    listado_personal.append(fila2)
    listado_personal.append(fila3)
    listado_personal.append(fila4)
    listado_personal.append(fila5)
    listado_personal.append(fila6)
diccionario[''] = listado_personal
print(diccionario)
            