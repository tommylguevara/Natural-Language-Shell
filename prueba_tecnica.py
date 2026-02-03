import os
import json
import re
import socket
import logging
import argparse
import shutil
from typing import Any, Dict
from openai import OpenAI

# Configuración de Logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

client = None

def get_client():
    global client
    if client is not None:
        return client
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("La variable de entorno OPENAI_API_KEY no está definida")
    client = OpenAI(api_key=api_key)
    return client

def obtener_ip() -> str:
    """Obtiene la IP local del host."""
    try:
        # Intento conectar a un servidor externo para obtener la IP real en la red
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return socket.gethostbyname(socket.gethostname())

def ejecutar_accion(datos: Dict[str, Any]) -> str:
    """Ejecuta acciones en el sistema de archivos según el JSON recibido."""
    accion = datos.get("accion")
    ruta = os.path.expanduser(datos.get("ruta", ""))
    contenido = datos.get("contenido", "")

    try:
        if accion == "crear_carpeta":
            os.makedirs(ruta, exist_ok=True)
            return f"Carpeta creada en: {ruta}"

        elif accion == "crear_archivo":
            if "{IP}" in contenido:
                contenido = contenido.replace("{IP}", obtener_ip())
            
            parent = os.path.dirname(ruta)
            if parent:
                os.makedirs(parent, exist_ok=True)
            
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido)
            return f"Archivo creado en: {ruta}"

        elif accion == "leer_archivo":
            if not os.path.exists(ruta):
                return f"Error: El archivo {ruta} no existe."
            with open(ruta, "r", encoding="utf-8") as f:
                return f"Contenido de {ruta}:\n{f.read()}"

        elif accion == "listar_carpeta":
            if not os.path.exists(ruta):
                return f"Error: La carpeta {ruta} no existe."
            entries = os.listdir(ruta)
            return f"Contenido de {ruta}:\n" + "\n".join(entries)

        elif accion == "eliminar":
            if os.path.isdir(ruta):
                shutil.rmtree(ruta)
                return f"Carpeta eliminada: {ruta}"
            elif os.path.isfile(ruta):
                os.remove(ruta)
                return f"Archivo eliminado: {ruta}"
            else:
                return f"No existe el elemento: {ruta}"

        return f"Acción desconocida: {accion}"

    except Exception as e:
        logger.error(f"Error en ejecución: {e}")
        return f"Error al ejecutar la acción: {e}"

def procesar_instruccion(instruccion_usuario: str) -> Dict[str, Any]:
    """Usa GPT-4o para interpretar la instrucción y devolver un JSON."""
    prompt_sistema = (
        "Eres un experto en automatización de sistemas. Tu tarea es convertir instrucciones en español "
        "a un objeto JSON estricto para ejecutar acciones de sistema operativo.\n\n"
        "Acciones soportadas:\n"
        "- crear_carpeta: {'accion':'crear_carpeta', 'ruta':'...'}\n"
        "- crear_archivo: {'accion':'crear_archivo', 'ruta':'...', 'contenido':'...'}\n"
        "- leer_archivo: {'accion':'leer_archivo', 'ruta':'...'}\n"
        "- listar_carpeta: {'accion':'listar_carpeta', 'ruta':'...'}\n"
        "- eliminar: {'accion':'eliminar', 'ruta':'...'}\n\n"
        "Regla especial: Si el contenido requiere la dirección IP, escribe exactamente '{IP}'.\n"
        "Responde EXCLUSIVAMENTE con el objeto JSON."
    )

    client = get_client()
    # Usamos response_format={"type": "json_object"} para mayor seguridad
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": instruccion_usuario}
        ],
        response_format={"type": "json_object"}
    )

    raw_content = response.choices[0].message.content
    return json.loads(raw_content)

def interactive_loop():
    print("\n" + "="*40)
    print("ASISTENTE DE SISTEMA OPERATIVO (IA)")
    print("="*40)
    print("Ejemplo: 'Crea un archivo en el escritorio con mi IP'")
    print("Escribe 'salir' para finalizar.")

    while True:
        user_input = input('\n> ')
        if user_input.strip().lower() in ["salir", "exit", "quit"]:
            break

        try:
            print("Interpretando instrucción...", end="\r")
            comando_json = procesar_instruccion(user_input)
            
            # Confirmación de seguridad
            if comando_json.get("accion") == "eliminar":
                confirm = input(f"¿Estás seguro de eliminar {comando_json.get('ruta')}? (s/n): ")
                if confirm.lower() != 's':
                    print("Operación cancelada.")
                    continue

            resultado = ejecutar_accion(comando_json)
            print(f"Resultado: {resultado}")

        except Exception as e:
            print(f"Ocurrió un error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Asistente de consola OS via LLM.")
    # Podrías expandir la lógica de --safe aquí si lo deseas
    parser.add_argument("--safe", action="store_true", help="Habilita modo de ejecución segura.")
    args = parser.parse_args()

    try:
        interactive_loop()
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario.")

if __name__ == "__main__":
    main()