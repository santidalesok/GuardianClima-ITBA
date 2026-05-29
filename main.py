import login
import clima
import csv
import time
from clima import R, B, CY, GR, YE

def menu_principal():
    print(f"\n{GR}Bienvenido, {B}{login.usuario_ingresado}{R}{GR}!{R}")
    print(f"{B}{CY}=== MENÚ PRINCIPAL ==={R}")
    print(f"  {YE}1.{R} Consultar clima")
    print(f"  {YE}2.{R} Ver historial")
    print(f"  {YE}3.{R} Estadísticas globales")
    print(f"  {YE}4.{R} Consejo IA")
    print(f"  {YE}5.{R} Acerca de...")
    print(f"  {YE}6.{R} Cerrar sesión")
    seleccion = input("Seleccione una opción (1-6): ")
    return seleccion

def chequear_seleccion(seleccion):
    if seleccion == '1':
        consultar_clima()
    elif seleccion == '2':
        clima.solicitar_consultas(login.usuario_ingresado)
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
        decision = input("¿Desea consultar el clima nuevamente? (s/n): ").strip().lower()
        if decision == 's':
            consultar_clima()

def loop_principal():
    while True:
        seleccion = menu_principal()
        if not chequear_seleccion(seleccion):
            break

if __name__ == "__main__":
    loop_principal()