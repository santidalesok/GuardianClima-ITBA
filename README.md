# GuardianClima ITBA

##Instalación de Dependencias
Instala las librerías externas utilizadas en el proyecto con el comando:
pip install -r requirements.txt
Este instalrá automáticamente las librerias utilizadas.

En caso de que no se disponga del archivo requirements.txt, se pueden instalar las librerias manualmente corriendo el siguiente comando: pip install requests google-generativeai python-dotenv

##Configuración Segura de API Keys
Por motivos de seguridad, no se incluyen las credenciales y  API keys directamente en el código fuente ni están subidas a este repositorio, por lo que utilizamos python-dotenv para leer las API keys de forma externa.
###Instrucciones:
En primer lugar crea un archivo en la raiz del proyecto llamado .env
Abre el archivo .env con cualquier editor de notas y agrega tus propias credenciales en el siguiente formato:
OPENWEATHER_API_KEY=tu_token_de_openweather
GEMINI_API_KEY=tu_token_de_gemini

Para conseguir las llaves...

##Guía de ejecución y flujo de menús
Para iniciar la aplicación ejecuta desde tu consola el siguiente comando:
python main.py

//COMPLETAR LOGICA DE LOGIN//

Una vez iniciada la sesión de forma exitosa, se desplegará el panel central interactivo. A continuación se detalla la lógica de cada opción:

###Consultar clima

###Ver historial

###Estadísticas globales

###Consejo IA

###Acerca de...

###Cerrar sesión
