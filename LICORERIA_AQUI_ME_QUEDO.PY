#diccionario donde se guardan los usuarios registrados
usuarios_registrados={}
#diccionario donde se guardan los productos registrados
licores_registrados={}
name_licor=(input("·····INGRESE EL NOMBRE DE SU LICORERIA··········"))
#INVENTARIO
def inventario():
    print("INVENTARIO DE TU LICORERIA")
    cantidad=int(input("...INGRESE EL CODIGO DEL PRODUCTO....."))
    if 

def registro1():
    print("""......INGRESE UNA OPCION 
          1.REGISTRAR PRODUCTO.
          2.VOLVER""")
    opcional=int(input("......INGRESE UNA OPCION......"))
    if opcional==1:
        una()
    elif opcional==2:
         menu_tho()
    else:
         print(".....OPCION INVALIDA.........")
#REGISTRO DE PRODUCTOS DE VENTA
def una():
    print("......REGISTRO DE PRODUCTOS DE VENTA.......")
    name=(input(".....INGRESE EL NOMBRES DEL PRODUCTO A REGISTRAR...."))
    codigo=int(input(".....INGRESE EL CODIGO DEL PRODUCTO...."))
    precio=int(input("......INGRESE EL PRECIO DEL PRODUCTO........."))
    licores_registrados[codigo]={"nombre":name,"precio":precio}
    print("producto ",name,"con el codigo",codigo,"y el preciio",precio,
        "registrado con exito")
    print("""...SELECCIONE UNA OPCION.....
              1.SEGUIR REGISTRANDO 
              2.VOLVER AL MENU """)
    opcuna=int(input("...INGRESE UNA OPCION...."))
    if opcuna==1:
        una()
    elif opcuna==2:
        menu_tho()
    else:
         print("opcion invalida")
#VENTAS
def ventas():
    codigo=int(input(".....INGRESE EL CODIGO DEL PRODUCTO A VENDER..."))
    producto=licores_registrados[codigo]
    if codigo in licores_registrados:
         print(f"producto encontrado:{producto['nombre']}{producto['precio']}")
         num=int(input(".....ingrese cuntos productos va a vender......"))
         costo=num*producto['precio']
         print(".......EL COSTO TOTAL DEL PRODUCTO SERA DE :",costo,"BS") 
         print("....VENTA EXITOSA TENGA UN BUEN DIA:")          
#MENU2
def menu_tho():
    print("""INGRESE UNA OPCION
            1.VENTAS
            2.REGISTRO DE PRODUCTOS
            3.REGISTRO DE INVENTARIO""")
    elec=int(input("ingrese una opcion"))
    if elec==1:
        ventas()
    elif elec==2:
         registro1()
    elif elec==3:
        inventario()
    else:
        print("...OPCION INVALIDA....")
#REGISTRO DE USUARIO      
def registro():
    print("········BIENVENIDO AL SISTEMA ALCOLIC.INT······")
    name_licor=(input("·····INGRESE EL NOMBRE DE SU LICORERIA··········"))
    usu=(input("····INGRESE EL NOMBRE DEL USUARIO·········".strip()))
    print("···BIENVENIDO",usu.upper())
    con=1
    while con<=3:
        print(f"......intento" ,con, "de 3")   
        contraseña=input(".......INGRESE UNA CONTRASEÑA QUE TENGA 8 DIGITOS..........")
        b=(len(contraseña))
        if b>=8:
            print("contraseña correcta su cuenta fue guardada")
            usuarios_registrados[usu]=contraseña
            break
        else:
            print("contraseña insegura")
            con+=1
#incio_de_sesion
def inicio():
    print(".........INICIO DE SESIÓN DEL SISTEMA......")
    cont=1
    while cont<=3:
        t=input(".....INGRESE SU USUARIO.......")
        v=input(".........INGRESE SU CONTRASEÑA........")
        if t in usuarios_registrados and usuarios_registrados[t]==v:
            print("....INICIO DE SESIÓN CORRECTA,SEA BIENVENIDO",t.upper(),"A",name_licor.upper())
            menu_tho()

            break
        else:
            print("...USUARIO O CONTRASEÑA INCORRECTA .....")
            cont+=1
#menu_principal
while True:
    print(""".......BIENVENIDO A ALCHOLIC.INC........
            .....SELECCIONE UNA OPCION........
                1.registro
                2.inicio de sesion
                3.salir""")
    opc=int(input(".....INGRESE UNA OPCION....."))
    if opc==1:
        registro()
    elif opc==2:
        inicio()
    elif opc==3:
        print("SALIENDO DE SISTEMA ,GRACIAS POR USAR ALCOLICD.INT")
        break
    else:
        print("......OPCION INVALIDA VUELVA INTENTARLO.......")

