import os
import csv
import requests
from datetime import datetime
from dotenv import load_dotenv

# Colores para menus mas faciles de ver:

R  = "\033[0m"   # resetear
B  = "\033[1m"   # negrita
CY = "\033[96m"  # cian
GR = "\033[92m"  # verde
YE = "\033[93m"  # amarillo

load_dotenv()

HISTORIAL_CSV = "historial_global.csv"
API_KEY  = os.environ["OPENWEATHER_API_KEY"]
CIUDAD   = "Buenos Aires"
IDIOMA   = "es"
UNIDADES = "metric"
URL_BASE = "https://api.openweathermap.org/data/2.5/weather"


def obtener_clima(ciudad, api_key, idioma="es", unidades="metric"):
    """Llama a la API y devuelve el JSON crudo, o lanza una excepción con mensaje claro."""
    parametros = {
        "q":     ciudad,
        "appid": api_key,
        "lang":  idioma,
        "units": unidades,
    }
    respuesta = requests.get(URL_BASE, params=parametros)

    if respuesta.status_code == 401:
        raise PermissionError("API key inválida o no activada aún.")
    elif respuesta.status_code == 404:
        raise ValueError(f"Ciudad '{ciudad}' no encontrada.")
    elif respuesta.status_code == 429:
        raise ConnectionError("Límite de requests superado. Esperá un momento e intentá de nuevo.")
    elif respuesta.status_code != 200:
        raise RuntimeError(f"Error inesperado. Código HTTP: {respuesta.status_code}")

    return respuesta.json()


def parsear_datos(datos, unidades="metric"):
    """Extrae los campos relevantes del JSON y devuelve un dict estructurado."""
    simbolo_temp  = "°C" if unidades == "metric" else ("°F" if unidades == "imperial" else "K")
    unidad_viento = "m/s" if unidades in ("metric", "standard") else "mph"

    return {
        "ciudad":       datos["name"],
        "pais":         datos["sys"]["country"],
        "condicion":    datos["weather"][0]["main"],
        "descripcion":  datos["weather"][0]["description"],
        "temperatura":  datos["main"]["temp"],
        "sensacion":    datos["main"]["feels_like"],
        "humedad":      datos["main"]["humidity"],
        "temp_min":     datos["main"]["temp_min"],
        "temp_max":     datos["main"]["temp_max"],
        "viento":       datos["wind"]["speed"],
        "nubosidad":    datos["clouds"]["all"],
        "simbolo_temp": simbolo_temp,
        "unidad_viento": unidad_viento,
    }

def solicitar_consultas(usuario):
    ciudad = input("Ingresá el nombre de la ciudad a buscar: ").strip()
    if not ciudad:
        print("No ingresaste ninguna ciudad.")
        return

    resultados = []
    try:
        with open(HISTORIAL_CSV, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                if (fila["NombreDeUsuario"].lower() == usuario.lower()
                        and fila["Ciudad"].lower() == ciudad.lower()):
                    resultados.append(fila)
    except FileNotFoundError:
        print("Todavía no hay historial de consultas.")
        return

    if not resultados:
        print(f"\nNo se encontraron consultas de '{usuario}' para '{ciudad}'.")
        return

    print(f"\n{B}{CY}{'─'*60}{R}")
    print(f"{B}{CY}  Consultas de {usuario} para {resultados[0]['Ciudad']}{R}")
    print(f"{B}{CY}{'─'*60}{R}")
    for i, r in enumerate(resultados, 1):
        print(f"  {B}Consulta #{i}{R}")
        print(f"    {YE}Fecha/Hora   :{R} {r['Fecha_Hora']}")
        print(f"    {YE}Temperatura  :{R} {GR}{r['Temperatura_C']} °C{R}")
        print(f"    {YE}Condición    :{R} {r['Condicion_Clima']}")
        print(f"    {YE}Humedad      :{R} {r['Humedad_Porcentaje']}%")
        print(f"    {YE}Viento       :{R} {r['Viento_kmh']} km/h")
        if i < len(resultados):
            print()
    print(f"{CY}{'─'*60}{R}")


def mostrar_clima(info):
    """Imprime el resumen del clima en consola."""
    print()
    print(f"{B}{CY}━━━ Clima en {info['ciudad']}, {info['pais']} ━━━{R}")
    print(f"  {YE}Condición   :{R} {info['descripcion'].capitalize()} ({info['condicion']})")
    print(f"  {YE}Temperatura :{R} {GR}{info['temperatura']}{info['simbolo_temp']}{R}  (sensación {info['sensacion']}{info['simbolo_temp']})")
    print(f"  {YE}Mín / Máx   :{R} {info['temp_min']}{info['simbolo_temp']} / {info['temp_max']}{info['simbolo_temp']}")
    print(f"  {YE}Humedad     :{R} {info['humedad']}%")
    print(f"  {YE}Viento      :{R} {info['viento']} {info['unidad_viento']}")
    print(f"  {YE}Nubosidad   :{R} {info['nubosidad']}%")

def guardar_historial(usuario, info):
    """Agrega una fila al historial global CSV con los datos de la consulta."""
    archivo_vacio = not os.path.isfile(HISTORIAL_CSV) or os.path.getsize(HISTORIAL_CSV) == 0
    with open(HISTORIAL_CSV, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        if archivo_vacio:
            escritor.writerow([
                "NombreDeUsuario", "Ciudad", "Fecha_Hora",
                "Temperatura_C", "Condicion_Clima",
                "Humedad_Porcentaje", "Viento_kmh"
            ])
        escritor.writerow([
            usuario,
            info["ciudad"],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            info["temperatura"],
            info["condicion"],
            info["humedad"],
            round(info["viento"] * 3.6, 2),
        ])


def pedir_clima(usuario="desconocido"):
    """Pide la ciudad por input, consulta la API, muestra el resultado y guarda el historial."""
    ciudad = input("Ingresá el nombre de la ciudad: ").strip()
    if not ciudad:
        return "Error: No ingresaste ninguna ciudad."
    try:
        datos_crudos = obtener_clima(ciudad, API_KEY, IDIOMA, UNIDADES)
        info = parsear_datos(datos_crudos, UNIDADES)
        mostrar_clima(info)
        guardar_historial(usuario, info)
    except Exception as e:
        return "Error al obtener el clima: " + str(e)
    return "Clima consultado exitosamente."

def clima():
    
    try:
        datos_crudos = obtener_clima(CIUDAD, API_KEY, IDIOMA, UNIDADES)
        info = parsear_datos(datos_crudos, UNIDADES)
        mostrar_clima(info)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    clima()
