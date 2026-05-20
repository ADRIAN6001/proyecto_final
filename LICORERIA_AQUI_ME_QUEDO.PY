print("········BIENVENIDO AL SISTEMA ALCOLIC.INT······")
b=print(input("·····INGRESE EL NOMBRE DE SU LICORERIA··········"))
usu=print(input("····INGRESE EL NOMBRE DEL USUARIO·········"))
contraseña=print(input("·····INGRESE UNA CONTRASEÑA········"))
b=(len(contraseña))

if b==8:
    print("contraseña segura")
else:
    print("contraseña insegura")