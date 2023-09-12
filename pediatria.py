variable_texto = "Agenda de Citas Medicas"
nueva_variable_texto_reemplazo = variable_texto.replace("Agenda de Citas Medicas"," Pediatria")
print(variable_texto)
print(nueva_variable_texto_reemplazo)

dato_ingresado = input("Ingrese su Usuario:")
variable_usuario = str(dato_ingresado)
if(variable_usuario <  "ygrivera"):
   print("Usuario incorrecto")
elif(variable_usuario == "ygrivera"):
   print("Usuario Correcto")
elif(variable_usuario > "ygrivera"and variable_usuario < "ygrivera"):
   print("usuario correcto")    
#else:
    #print("Bienvenido")
def comprobar_Contraseña(Password):
    largo = False
    mayus = False
    numer = False
    if len (Password) > 8:
        largo= True
    for i in range(len(Password)):
        if Password[i].isupper():
            mayus = True
        if Password[i].isnumeric():
            numer= True

    if largo and mayus and numer:
        return True
    else:
        return False
    
Password = input ("Ingrese Una Contraseña: ")
verificacion = comprobar_Contraseña (Password)
if verificacion:
    print ("la contraseña es segura")
else:
    print("La Contraseña no es Segura")