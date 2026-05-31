#Ejecutar en la consola: pip install -r requirements.txt
import login
import clima
import consejoia
import acercade
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
        print(f"\n{B}{CY}=== ESTADÍSTICAS GLOBALES DEL SISTEMA ==={R}")
        print("Procesando datos históricos de todos los usuarios...")
        stats = clima.calcular_estadisticas_globales()
        if stats is None:
            print("No hay datos disponibles para generar estadísticas globales.")
            return True
        print("\n-------------------------------------------------")
        print(f" Número total de consultas: {stats['total']}")
        print(f" Temperatura promedio registrada: {stats['promedio_temp']:.1f}°C")
        print(f" Ciudad más consultada por la comunidad: {stats['ciudad_top']} ({stats['ciudad_top_veces']} veces)")
        print("-------------------------------------------------")
        print(f"\n{GR} Nota: El archivo 'historial_global.csv' se encuentra actualizado")
        print(f"para ser exportado y analizado en Excel o Google Sheets.{R}")
        
        # Hacemos la pausa obligatoria para que el usuario pueda leer los números
        input(f"\n{YE}Presioná [ENTER] para volver al menú...{R}")
    elif seleccion == '4':
        registro = elegir_registro_consejo()
        if registro is None:
            print("No hay registros disponibles para generar un consejo de IA.")
            return True
        consejo = consejoia.obtener_consejo_ia(registro["Temperatura_C"], registro["Condicion_Clima"], registro["Viento_kmh"], registro["Humedad_Porcentaje"])
        print(f"\n{YE}Consejo:{R}")
        print(consejo)
        input(f"\n{YE}Presioná [ENTER] para continuar...{R}")
    elif seleccion == '5':
        acercade.acerca_de()
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

    registros = []
    try:
        with open(clima.HISTORIAL_CSV, newline="", encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                if fila["NombreDeUsuario"].lower() == login.usuario_ingresado.lower():
                    registros.append(fila)
    except FileNotFoundError:
        pass

    if not registros:
        print("No hay consultas previas disponibles. Consultá el clima primero.")
        return None

    print(f"\n{B}{CY}{'─'*60}{R}")
    print(f"  Tus consultas recientes:")
    print(f"{B}{CY}{'─'*60}{R}")
    for i, r in enumerate(registros, 1):
        print(f"  {YE}{i}.{R} {r['Ciudad']} — {r['Fecha_Hora']} — {GR}{r['Temperatura_C']}°C{R}")
    print(f"{CY}{'─'*60}{R}")

    try:
        seleccion_num = int(input(f"\nIngresá el número de consulta a usar (1-{len(registros)}), o 0 para volver: "))
        if seleccion_num == 0:
            return None
        if 1 <= seleccion_num <= len(registros):
            return registros[seleccion_num - 1]
        print("Número fuera de rango. Operación cancelada.")
        return None
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")
        return None

def loop_principal():
    while True:
        seleccion = menu_principal()
        if not chequear_seleccion(seleccion):
            break

if __name__ == "__main__":
    loop_principal()

