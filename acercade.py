from clima import R, B, CY, GR, YE

def acerca_de():
    sep = f"{B}{CY}{'━'*62}{R}"
    print(f"\n{sep}")
    print(f"{B}{CY}  GuardiánClima ITBA  |  Grupo: Apple inc.{R}")
    print(sep)

    print(f"\n{B}{YE}DESCRIPCIÓN{R}")
    print("""
  GuardiánClima ITBA es una aplicación de consola para la consulta
  de clima en tiempo real, el registro de un historial de consultas,
  la generación de estadísticas y la obtención de consejos
  personalizados con inteligencia artificial.
  El proyecto es un ejercicio académico para el ITBA.""")

    print(f"\n{B}{YE}MENÚ DE ACCESO{R}")
    print(f"""
  Al iniciar la aplicación, el usuario tiene tres opciones:

  {YE}1. Iniciar sesión:{R}
     El usuario ingresa su nombre de usuario y contraseña. El sistema
     los verifica contra un archivo CSV. Si los datos son correctos,
     el acceso al menú principal es inmediato.

  {YE}2. Registrarse:{R}
     El usuario elige un nombre de usuario único y una contraseña.
     La contraseña debe superar los 8 caracteres, incluir al menos
     un número y una combinación de letras mayúsculas y minúsculas.
     Una vez validada, el nuevo usuario queda registrado en el CSV.

  {YE}3. Salir:{R}
     Cierra la aplicación.""")

    print(f"\n{B}{YE}MENÚ PRINCIPAL{R}")
    print(f"""
  {YE}1. Consultar clima:{R}
     El usuario ingresa el nombre de una ciudad. La aplicación
     devuelve los datos climáticos en tiempo real: temperatura,
     humedad, viento, nubosidad y condición. La consulta queda
     registrada de forma automática en el historial global.

  {YE}2. Ver historial:{R}
     El usuario ingresa el nombre de una ciudad y la aplicación
     muestra todas sus consultas previas para esa ciudad, con
     fecha, hora y datos climáticos completos.

  {YE}3. Estadísticas globales:{R}
     La aplicación genera un resumen estadístico de todas las
     consultas del historial global: promedios de temperatura,
     ciudades más consultadas y más. El CSV resultante es
     compatible con Excel, Google Sheets o librerías de Python
     como matplotlib y pandas para la creación de gráficos.

  {YE}4. Consejo IA:{R}
     La aplicación muestra el historial de consultas del usuario.
     Al elegir una, un modelo de inteligencia artificial genera
     un consejo de vestimenta y actividades adaptado a las
     condiciones climáticas de ese registro.

  {YE}5. Acerca de...:{R}
     Esta sección.

  {YE}6. Cerrar sesión:{R}
     Cierra la sesión actual y vuelve al menú de acceso.""")

    print(f"\n{B}{YE}FUNCIONAMIENTO INTERNO{R}")
    print(f"""
  {B}Gestión de usuarios:{R}
  Los usuarios tienen su lugar en un archivo CSV llamado
  usuarios_simulados.csv. La validación de contraseñas exige
  longitud mínima, uso de números y combinación de mayúsculas y
  minúsculas. Para un entorno real, es recomendable el uso de bases
  de datos con autenticación segura como OAuth o JWT.

  {B}⚠  Advertencia de seguridad:{R}
  Las contraseñas tienen su lugar en el CSV en texto plano. Este
  enfoque es exclusivo del ejercicio académico y no es apto para
  producción. En aplicaciones reales, las contraseñas deben pasar
  por algoritmos de hashing seguros como bcrypt o Argon2, de modo
  que el valor original nunca tenga su lugar en el almacenamiento.

  {B}Consulta de clima e historial:{R}
  Los datos climáticos provienen de la API de OpenWeatherMap.
  Cada consulta exitosa tiene su registro en historial_global.csv
  con el nombre de usuario, ciudad, fecha y hora, temperatura en °C,
  condición climática, humedad y velocidad del viento en km/h.

  {B}Estadísticas globales:{R}
  La función de estadísticas toma los datos de historial_global.csv
  y calcula métricas agregadas sobre todas las consultas. El archivo
  es compatible con herramientas de visualización como Excel o pandas.

  {B}Consejos de IA:{R}
  El sistema toma los datos de una consulta del historial del usuario
  y los envía a un modelo de lenguaje. La respuesta es un consejo en
  lenguaje natural, adaptado a las condiciones climáticas del momento
  elegido.""")

    print(f"\n{B}{YE}EQUIPO{R}")
    print(f"""
  Grupo: {B}Apple inc.{R}

  · Santiago D'alessandro
  · Santiago Lopez Cozza
  · Manuel Chab
  · Tomas Nieponice""")

    print(f"\n{sep}\n")
    input(f"  {YE}Presioná [ENTER] para volver al menú principal...{R}")
