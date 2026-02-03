import json
from types import SimpleNamespace
import pytest
import prueba_tecnica


def fake_response(content):
    return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=content))])


def test_procesar_instruccion_crear_carpeta(monkeypatch, tmp_path):
    # Mockear la respuesta del cliente OpenAI
    fake_content = json.dumps({"accion": "crear_carpeta", "ruta": str(tmp_path / "carpeta")})
    monkeypatch.setattr(prueba_tecnica, 'client', SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=lambda *a, **k: fake_response(fake_content)))))

    res = prueba_tecnica.procesar_instruccion("crear carpeta")
    assert res["accion"] == "crear_carpeta"
    assert res["ruta"] == str(tmp_path / "carpeta")


def test_ejecutar_accion_crear_carpeta(tmp_path):
    datos = {"accion": "crear_carpeta", "ruta": str(tmp_path / "nueva")}
    out = prueba_tecnica.ejecutar_accion(datos)
    assert (tmp_path / "nueva").exists()
    assert "Carpeta creada en" in out


def test_ejecutar_accion_crear_archivo_with_ip(tmp_path, monkeypatch):
    # Forzamos obtener_ip para que sea determinista
    monkeypatch.setattr(prueba_tecnica, 'obtener_ip', lambda: '1.2.3.4')
    ruta = tmp_path / "archivo.txt"

    datos = {"accion": "crear_archivo", "ruta": str(ruta), "contenido": "Mi IP es {IP}"}
    out = prueba_tecnica.ejecutar_accion(datos)

    assert ruta.exists()
    assert ruta.read_text(encoding="utf-8") == "Mi IP es 1.2.3.4"
    assert "Archivo creado en" in out


def test_ejecutar_accion_leer_archivo(tmp_path):
    ruta = tmp_path / "archivo.txt"
    ruta.write_text("hola", encoding="utf-8")
    datos = {"accion": "leer_archivo", "ruta": str(ruta)}

    out = prueba_tecnica.ejecutar_accion(datos)
    assert "hola" in out


def test_procesar_instruccion_invalid_json(monkeypatch):
    monkeypatch.setattr(prueba_tecnica, 'client', SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=lambda *a, **k: fake_response('No es JSON')))))
    with pytest.raises(json.JSONDecodeError):
        prueba_tecnica.procesar_instruccion("generar no-json")
