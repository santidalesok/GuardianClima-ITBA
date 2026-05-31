#Ejecutar en la consola: pip install -r requirements.txt
import login
import clima
import consejoia
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
        clima.solicitar_consultas()
    elif seleccion == '3':
        print("Funcionalidad de estadísticas globales aún no implementada.")
    elif seleccion == '4':
        registro = elegir_registro_consejo()
        if not registro:
            print("No hay registros disponibles para generar un consejo de IA.")
        consejo = consejoia.obtener_consejo_ia(registro["Temperatura_C"], registro["Condicion_Clima"], registro["Viento_kmh"], registro["Humedad_Porcentaje"])
        print(f"\n{YE}Consejo:{R}")
        print(consejo)
        input(f"\n{YE}Presioná [ENTER] para continuar...{R}")
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

def elegir_registro_consejo():
    print(f"\n{B}{CY}=== OBTENER CONSEJO DE IA ==={R}")
    print("Para darte un consejo de vestimenta personalizado, necesitamos datos climáticos.")
    print("¿Qué deseas hacer?")
    print(f"  {YE}1.{R} Buscar el historial de una ciudad y elegir una consulta pasada")
    print(f"  {YE}2.{R} Volver al menú principal")

    opcion = input("Selecciona una opción (1-2): ").strip()
    
    if opcion == "1":
        consultas_disponibles = clima.solicitar_consultas(login.usuario_ingresado)
        
        # Si la función de clima devolvió None o una lista vacía, avisamos y salimos
        if not consultas_disponibles:
            print("⚠️ No se pudieron recuperar registros de esa ciudad.")
            return None
            
        # Si llegó acá, significa que consultas_disponibles SÍ tiene los datos
        try:
            seleccion_num = int(input(f"\nIngresá el número de consulta que querés usar (1-{len(consultas_disponibles)}): "))
                
            if 1 <= seleccion_num <= len(consultas_disponibles):
                registro_elegido = consultas_disponibles[seleccion_num - 1]
                return registro_elegido
            else:
                print(" Número fuera de rango. Operación cancelada.")
                return None
        except ValueError:
            print(" Entrada inválida. Debes ingresar un número entero.")
            return None
        
    elif opcion == "2":
        return None
    else: 
        print(" Opción inválida. Operación cancelada.")
        return None

def loop_principal():
    while True:
        seleccion = menu_principal()
        if not chequear_seleccion(seleccion):
            break

if __name__ == "__main__":
    loop_principal()

