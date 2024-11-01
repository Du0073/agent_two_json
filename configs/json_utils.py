import json
import os

def save_project_to_json(project_data, filename="proyecto_generado.json"):
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    with open(filepath, "w", encoding="utf-8") as json_file:
        json.dump(project_data, json_file, ensure_ascii=False, indent=4)
    print(f"El proyecto ha sido guardado exitosamente en: {filepath}")

def load_project_from_json(filepath="output/proyecto_generado.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as json_file:
            project_data = json.load(json_file)
        print(f"Proyecto cargado desde {filepath}")
        return project_data
    except FileNotFoundError:
        print(f"Archivo {filepath} no encontrado.")
        return None
