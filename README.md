# GuardianClima ITBA

## Instalación de Dependencias
Instala las librerías externas utilizadas en el proyecto con el comando:
pip install -r requirements.txt
Este instalrá automáticamente las librerias utilizadas.

En caso de que no se disponga del archivo requirements.txt, se pueden instalar las librerias manualmente corriendo el siguiente comando: pip install requests google-generativeai python-dotenv

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
Para iniciar la aplicación ejecuta desde tu consola el siguiente comando:
python main.py

//COMPLETAR LOGICA DE LOGIN//

Una vez iniciada la sesión de forma exitosa, se desplegará el panel central interactivo. A continuación se detalla la lógica de cada opción:

### Consultar clima

### Ver historial

### Estadísticas globales

### Consejo IA

### Acerca de...

### Cerrar sesión
