i = 0
inventario =[]
def agregar_producto():
    nombre_de_producto = input("ingresar nombre del producto:")
    while True : 
        try:
             precio_producto = float(input("ingrese el precio del producto:"))
             if i > precio_producto:
                    print("ingrese un valor correcto")
                    continue
             break
        except ValueError:
            print("ingrese solo numeros")
    while True :
        try:
              cantidad_producto = int(input("ingrese la cantidad de su producto:"))
              if i > cantidad_producto:
                   print("ingrese un valor numerico")
                   continue
              break
        except ValueError:
             print("ingrese solo valores numericos")


    producto={
     "nombre" :nombre_de_producto,
     "precio" :precio_producto,
     "cantidad" : cantidad_producto, 
    }   
    
    inventario.append(producto)
    print("producto ingresado correctamente ")

def mostrar_inventario():
    print("---INVENTARIO---")
    if len(inventario) == 0 :
          print("el inventario esta vacio")
    else :
       for producto in inventario:
            print(f"producto:{producto['nombre']} | precio :{producto['precio']} | cantidad: {producto['cantidad']} ")

def estadistica_productos ():
     

             
               

          

        










