import os
import requests
from dotenv import load_dotenv

load_dotenv()

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


def mostrar_clima(info):
    """Imprime el resumen del clima en consola."""
    print()
    print(f"━━━ Clima en {info['ciudad']}, {info['pais']} ━━━")
    print(f"  Condición   : {info['descripcion'].capitalize()} ({info['condicion']})")
    print(f"  Temperatura : {info['temperatura']}{info['simbolo_temp']}  (sensación {info['sensacion']}{info['simbolo_temp']})")
    print(f"  Mín / Máx   : {info['temp_min']}{info['simbolo_temp']} / {info['temp_max']}{info['simbolo_temp']}")
    print(f"  Humedad     : {info['humedad']}%")
    print(f"  Viento      : {info['viento']} {info['unidad_viento']}")
    print(f"  Nubosidad   : {info['nubosidad']}%")

def pedir_clima():
    """Pide la ciudad por input, consulta la API y muestra el resultado."""
    ciudad = input("Ingresá el nombre de la ciudad: ").strip()
    if not ciudad:
        print("No ingresaste ninguna ciudad.")
        return
    try:
        datos_crudos = obtener_clima(ciudad, API_KEY, IDIOMA, UNIDADES)
        info = parsear_datos(datos_crudos, UNIDADES)
        mostrar_clima(info)
    except Exception as e:
        return "Error al obtener el clima: " + str(e)

def clima():
    
    try:
        datos_crudos = obtener_clima(CIUDAD, API_KEY, IDIOMA, UNIDADES)
        info = parsear_datos(datos_crudos, UNIDADES)
        mostrar_clima(info)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    clima()