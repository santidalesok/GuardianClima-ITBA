import login
import clima
import time

def menu_principal():
    print(f"\nBienvenido, {login.usuario_ingresado}!")
    print("=== MENÚ PRINCIPAL ===")
    print("1. Consultar clima")
    print("2. Ver historial")
    print("3. Estadísticas globales")
    print("4. Consejo IA")
    print("5. Acerca de...")
    print("6. Cerrar sesión")
    seleccion = input("Seleccione una opción (1-6): ")
    return seleccion

def chequear_seleccion(seleccion):
    if seleccion == '1':
        consultar_clima()
    elif seleccion == '2':
        print("Funcionalidad de ver historial aún no implementada.")
    elif seleccion == '3':
        print("Funcionalidad de estadísticas globales aún no implementada.")
    elif seleccion == '4':
        print("Funcionalidad de consejo IA aún no implementada.")
    elif seleccion == '5':
        print("Funcionalidad de acerca de... aún no implementada.")
    elif seleccion == '6':
        print("Cerrando sesión...")
        return False
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 6.")
    return True

def consultar_clima():
    clima_nuevo = clima.pedir_clima(login.usuario_ingresado)
    if "Error" in clima_nuevo:
        print(f"{clima_nuevo}")
        decision = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()
        if decision == 's':
            consultar_clima()
        else:
            print("Regresando al menú principal...\n")
            time.sleep(1)
            loop_principal()
    else:
        decision = input("¿Desea consultar el clima nuevamente? (s/n): ").strip().lower()
        if decision == 's':
            consultar_clima()
        else:
            print("Regresando al menú principal...\n")
            time.sleep(1)
            loop_principal()

def loop_principal():
    while True:
        seleccion = menu_principal()
        if not chequear_seleccion(seleccion):
            break

if __name__ == "__main__":
    loop_principal()