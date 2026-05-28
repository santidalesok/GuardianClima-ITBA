import pathlib
import csv

while True:
    print("=== GUARDIÁNCLIMA ITBA ===")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir de la aplicación")

    opcion = input("Elegí una opción: ")

    # Login
    if opcion == "1":
        while True:
            usuario_ingresado = input("Usuario: ")
            password_ingresada = input("Contraseña: ")

            archivo = open("usuarios_simulados.csv", "r")
            lector = csv.reader(archivo)
            login_exitoso = False

            for fila in lector:
                if fila[0] == usuario_ingresado and fila[1] == password_ingresada:
                    login_exitoso = True

            archivo.close()

            if login_exitoso:
                break
            else:
                print("Usuario o contraseña incorrectos. Intentá de nuevo.\n")
        break

    # Sign up
    if opcion == "2":
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
        break
    
    #Salir
    if opcion == "3":
        exit()
        break

    else:
        print("Opción inválida. Intentá de nuevo.\n")