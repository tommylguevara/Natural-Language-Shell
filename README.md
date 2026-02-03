# 🤖 AI-Powered OS Assistant (Python)

Un asistente de línea de comandos inteligente que permite interactuar con el sistema operativo utilizando lenguaje natural en español. El sistema utiliza el modelo **GPT-4o** de OpenAI para interpretar las intenciones del usuario y ejecutarlas de forma segura.



## 🚀 Características

* **Intérprete de Lenguaje Natural:** Traduce instrucciones como *"Crea una carpeta en el escritorio con mi IP"* en acciones reales de archivos y carpetas.
* **Acciones Soportadas:**
    * `crear_carpeta`: Crea directorios (incluyendo rutas anidadas).
    * `crear_archivo`: Genera archivos con contenido específico.
    * `leer_archivo`: Muestra el contenido de archivos existentes.
    * `listar_carpeta`: Lista los archivos y carpetas de una ruta.
    * `eliminar`: Borra archivos o carpetas (con confirmación de seguridad).
* **Placeholder de IP:** Capacidad de detectar la dirección IP local del host e insertarla dinámicamente si el usuario lo solicita.
* **Seguridad:** El sistema no ejecuta comandos de shell directos. Utiliza un enfoque de **Function Calling** mediante un esquema JSON estricto para prevenir inyecciones de código.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.10+
* **Modelos de IA:** OpenAI API (GPT-4o)
* **Librerías:** `openai`, `json`, `os`, `shutil`, `argparse`.

## 📦 Instalación y Configuración

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/nombre-de-tu-repo.git](https://github.com/tu-usuario/nombre-de-tu-repo.git)
   cd nombre-de-tu-repo

2. Crea y activa un entorno virtual:

Bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate


3. Instala las dependencias:

Bash
pip install -r requirements.txt


4. Configura tu API Key: El programa requiere una variable de entorno llamada OPENAI_API_KEY.

PowerShell
# En PowerShell (temporal):
$env:OPENAI_API_KEY = "tu-clave-aqui"

-----------------------------------------------------------------------
🎮 Uso

Para iniciar el asistente, simplemente ejecuta:

Bash
python prueba_tecnica.py
Ejemplos de comandos:
"Crea una carpeta llamada Proyectos en el escritorio."

"Haz un archivo de texto en la carpeta Proyectos que contenga mi IP actual."

"Dime qué archivos hay en mi carpeta de Documentos."

"Borra la carpeta temporal que creamos antes."

------------------------------------------------------------------------

🛡️ Seguridad y Diseño
Este proyecto fue diseñado bajo el principio de Privilegio Mínimo. Las acciones están restringidas a funciones predefinidas de Python, eliminando el riesgo de que la IA ejecute comandos maliciosos accidentalmente en la terminal.


---

### Siguientes pasos en PowerShell:
Una vez que hayas guardado este archivo, solo te faltan estos tres comandos para subirlo:

1.  `git add README.md`
2.  `git commit -m "docs: add professional README"`
3.  `git push origin main`
