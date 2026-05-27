usuarios_registrados={}
name_licor=(input("·····INGRESE EL NOMBRE DE SU LICORERIA··········"))
def registro():
#registro
    print("········BIENVENIDO AL SISTEMA ALCOLIC.INT······")
    name_licor=(input("·····INGRESE EL NOMBRE DE SU LICORERIA··········"))
    usu=(input("····INGRESE EL NOMBRE DEL USUARIO·········"))
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
