import json
import os

#FOR AGENT: project_agent_json
def save_project_to_json(project_data, filename="proyecto_generado.json"):
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    with open(filepath, "w", encoding="utf-8") as json_file:
        json_str = json.dumps(project_data, ensure_ascii=False).replace("\\n", "").replace("\\", "")
        if json_str.startswith('"') and json_str.endswith('"'):
            json_str = json_str[1:-1]
        json_file.write(json_str)
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

#FOR AGENT: project_agent_json