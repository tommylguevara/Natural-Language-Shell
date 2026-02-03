# 🤖 AI-Powered OS Assistant (Python)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![OpenAI](https://img.shields.io/badge/AI-GPT--4o-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Un asistente de línea de comandos inteligente desarrollado en **Python** que permite interactuar con el sistema operativo utilizando lenguaje natural en español. El sistema utiliza el modelo **GPT-4o** de OpenAI para interpretar las intenciones del usuario y ejecutarlas de forma segura mediante un motor de acciones estructurado.



## 🚀 Características Principales

* **Intérprete de Lenguaje Natural:** Traduce instrucciones humanas como *"Crea una carpeta en el escritorio con mi IP"* en operaciones reales de archivos y directorios.
* **Gestión de Archivos y Carpetas:**
    * `crear_carpeta`: Generación de directorios (incluye creación de rutas anidadas).
    * `crear_archivo`: Escritura de archivos con contenido específico.
    * `leer_archivo` / `listar_carpeta`: Recuperación de información del sistema de forma segura.
    * `eliminar`: Borrado de archivos o carpetas con **confirmación manual obligatoria**.
* **Inyección Dinámica de Datos:** Capacidad de detectar la dirección IP local del host e insertarla automáticamente si el usuario lo solicita mediante lenguaje natural (placeholder `{IP}`).
* **Arquitectura Segura:** El sistema evita la ejecución directa de comandos de shell (`shell=True`). Utiliza un enfoque de **Function Calling** con validación de esquema JSON para prevenir inyecciones de código.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.10+
* **IA:** OpenAI API (GPT-4o)
* **Librerías:** `openai`, `json`, `os`, `shutil`, `socket`, `argparse`.

---

## 📦 Instalación y Configuración

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/AI-OS-Assistant.git](https://github.com/TU_USUARIO/AI-OS-Assistant.git)
   cd AI-OS-Assistant
Crea y activa un entorno virtual:

PowerShell
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
Instala las dependencias necesarias:

Bash
pip install openai python-dotenv
Configura tu API Key: El programa busca una variable de entorno llamada OPENAI_API_KEY.

PowerShell
# En PowerShell (sesión actual):
$env:OPENAI_API_KEY = "tu_api_key_aqui"
🎮 Guía de Uso
Para iniciar el asistente interactivo:

Bash
python prueba_tecnica.py
Ejemplos de comandos soportados:
"Crea una carpeta llamada 'Proyectos' en el escritorio."

"Escribe un archivo dentro de Proyectos llamado ip.txt que tenga mi dirección IP."

"Lista los archivos que hay en mi carpeta de Documentos."

"Elimina el archivo temporal.txt."

🛡️ Diseño y Seguridad
Este proyecto fue desarrollado bajo el principio de Privilegio Mínimo. A diferencia de otros asistentes que ejecutan comandos de terminal abiertos, este sistema actúa como un intermediario:

La IA genera un JSON de intención.

El script de Python valida los parámetros.

Se ejecutan funciones nativas y restringidas de Python.

Esto elimina el riesgo de ejecuciones maliciosas accidentales que podrían comprometer la integridad del sistema operativo.

Autor: Tommy Guevara

Desarrollado como proyecto de integración de LLMs y automatización de sistemas.


---

**¿Deseas que te ayude a crear el repositorio en GitHub y subirlo de una vez?** Solo tienes que decirme y te guío con los comandos finales.
