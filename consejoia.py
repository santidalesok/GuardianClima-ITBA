import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY  = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_KEY)

def obtener_consejo_ia(temperatura, condicion_clima, viento, humedad):
    try:
        model = genai.GenerativeModel('models/gemini-2.5-flash')
        """
        Recibe las variables climáticas de la última consulta y le pide un consejo
        de vestimenta a la inteligencia artificial de Gemini.
        """
        # Usamos la técnica de prompt engineering vista en el módulo dos: Few shot prompting. Le damos a la IA ejemplos concretos de entrada y salida para que entienda el formato que queremos.
        prompt = f"""
        Actúa como un experto asesor de vestimenta.
        Tu objetivo es recibir variables climáticas y devolver un consejo muy breve, 
        directo y práctico sobre qué ropa usar hoy. Sigue estrictamente 
        el formato de los siguientes ejemplos:
        Ejemplo 1:
        ### EJEMPLO 1 (Clima Frío)
        Entrada Clima:
        - Temperatura: 8°C
        - Condición del cielo: Despejado
        - Velocidad del viento: 25 km/h
        - Humedad: 45%
        Consejo IA:
        Hace mucho frío y el viento aumentará la sensación térmica invernal. Te recomiendo vestirte en capas: una camiseta térmica, un abrigo o campera abrigada que corte el viento, bufanda y guantes. Ideal pantalones gruesos.

        CASO REAL A RESOLVER
        Basándote exactamente en la estructura y brevedad de los ejemplos anteriores, genera el consejo para este clima actual:
        Entrada Clima:
        - Temperatura: {temperatura}°C
        - Condición del cielo: {condicion_clima}
        - Velocidad del viento: {viento} km/h
        - Humedad: {humedad}%
        """
        print("Generando consejo de vestimenta con IA...")
        respuesta = model.generate_content(prompt)
        if respuesta.text: 
            return respuesta.text 
        else: 
            # A veces la API puede no devolver texto si hay problemas con el prompt o 

            # Investigar respuesta.prompt_feedback si hay problemas 
            print("La IA no pudo generar un consejo.", respuesta.prompt_feedback) 
        return "No se pudo generar un consejo en este momento."
    except Exception as e:
        print(f"Error al contactar la API de Gemini o procesar la respuesta: {e}") 
        return "Error al generar el consejo de IA."