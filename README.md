# GuardianClima ITBA

## Instalación de Dependencias
Instalar las librerías externas utilizadas en el proyecto con el comando:
```bash
pip install -r requirements.txt
```
Este instalará automáticamente las librerias utilizadas.

En caso de que no se disponga del archivo requirements.txt, se pueden instalar las librerias manualmente corriendo el siguiente comando:
```bash
pip install requests google-generativeai python-dotenv
```

## Configuración Segura de API Keys
Por motivos de seguridad, no se incluyen las credenciales y  API keys directamente en el código fuente ni están subidas a este repositorio, por lo que utilizamos python-dotenv para leer las API keys de forma externa.

### Instrucciones:
Primero se debe hacer una copia de env_EXAMPLE a un archivo .env:
```bash
cp env_EXAMPLE .env
```
Luego se deben editar los campos OPENWEATHER_API_KEY y GEMINI_API_KEY:
```bash
OPENWEATHER_API_KEY='tu-key-de-openweathermap'
GEMINI_API_KEY='tu-key-de-gemini'
```
Para conseguir las keys, uno debe acceder a openweathermap.org y a aistudio.google.com. Ambas son gratuitas.

## Guía de ejecución y flujo de menús
Para iniciar la aplicación basta con correr el python principal:
```bash
python main.py
```
//COMPLETAR LOGICA DE LOGIN//

Una vez iniciada la sesión de forma exitosa, se desplegará el panel central interactivo. A continuación se detalla la lógica de cada opción:

### Consultar clima
Una de las funcionalidades principales de la aplicacion es consultar el clima en cualquier ciudad del mundo a traves de la API de openweathermap. El usuario simplemente ingresa una ciudad, y la aplicacion devuelve multiples datos respecto al clima de dicha ciudad. Cada consulta queda grabada en historial_global.csv

### Ver historial
En cualquier momento, cualquier usuario puede consultar por consultas hechas por el mismo de cualquier ciudad.

### Estadísticas globales

### Consejo IA
Utilizando la API de gemini, la aplicación permite generar un consejo de vestimenta en funcion del clima.

### Acerca de...
