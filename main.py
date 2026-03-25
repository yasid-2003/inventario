from src.inventario import agregar_producto,mostrar_inventario,estadistica_productos

while True:
    print("---MENU---")
    print("1)agregar producto")
    print("2)mostrar inventario")
    print("3)mostrar estadistica")
    print("4)salir")
    opcion = input("ingrese una opcion:")

    if opcion == "1":
        agregar_producto()
    
    if opcion == "2":
        mostrar_inventario()

    if opcion == "3":
        estadistica_productos()
    


    

        

