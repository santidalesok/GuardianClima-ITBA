import pathlib
import csv

# Login
def login():    
    while True:
        print("\n1. Volver al menú")
        print("2. Ir al Sign Up")
        usuario_ingresado = input("Usuario: ")

        if usuario_ingresado == "1":
            return None
        if usuario_ingresado == "2":
            return "signup"

        password_ingresada = input("Contraseña: ")

        archivo = open("usuarios_simulados.csv", "r")
        lector = csv.reader(archivo)
        login_exitoso = False

        for fila in lector:
            if fila[0] == usuario_ingresado and fila[1] == password_ingresada:
                login_exitoso = True

        archivo.close()

        if login_exitoso:
            return usuario_ingresado
        else:
            print("Usuario o contraseña incorrectos. Intentá de nuevo.\n")

# Sign up
def signup():
    while True:
        usuario_nuevo = input("Elegí un nombre de usuario: ")

        archivo = open("usuarios_simulados.csv", "r")
        lector = csv.reader(archivo)
        usuario_existe = False

        for fila in lector:
            if fila[0] == usuario_nuevo:
                usuario_existe = True

        archivo.close()

        if usuario_existe:
            print("Ese nombre de usuario ya existe. Elegí otro.\n")
        else:
            break

    while True:
        password_nueva = input("Elegí una contraseña: ")

        suficiente_largo = len(password_nueva) > 8

        tiene_numero = False
        for caracter in password_nueva:
            if caracter.isdigit():
                tiene_numero = True

        tiene_mayuscula = False
        tiene_minuscula = False
        for caracter in password_nueva:
            if caracter.isupper():
                tiene_mayuscula = True
            if caracter.islower():
                tiene_minuscula = True

        errores = []
        soluciones = []

        if not suficiente_largo:
            errores.append("mínimo de caracteres")
            soluciones.append("más de 8 caracteres")
        if not tiene_numero:
            errores.append("incluir un número")
            soluciones.append("al menos un número")
        if not tiene_mayuscula or not tiene_minuscula:
            errores.append("mezcla de mayúsculas y minúsculas")
            soluciones.append("al menos una letra mayúscula y una minúscula")

        if len(errores) > 0:
            print("Tu contraseña no cumple con " + ", ".join(errores) + ". Para una contraseña más segura, considera usar " + ", ".join(soluciones) + ".")
        
        if suficiente_largo and tiene_numero and (tiene_mayuscula and tiene_minuscula):
            break

    archivo = open("usuarios_simulados.csv", "a", newline="")
    escritor = csv.writer(archivo)
    escritor.writerow([usuario_nuevo, password_nueva])
    archivo.close()

    print(f"Usuario '{usuario_nuevo}' registrado con éxito!")
    usuario_ingresado = usuario_nuevo  

while True:
    print("=== GUARDIÁNCLIMA ITBA ===")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir de la aplicación")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        resultado = login()
        if resultado == "signup":
            usuario_ingresado = signup()
            break
        elif resultado is not None:
            usuario_ingresado = resultado
            break

    elif opcion == "2":
        usuario_ingresado = signup()
        break

    elif opcion == "3":
        exit()

    else:
        print("Opción inválida. Intentá de nuevo.\n")