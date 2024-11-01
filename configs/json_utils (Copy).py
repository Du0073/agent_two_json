import json
import os

def save_project_to_json(project_data, filename="proyecto_generado.json"):
    # Crea el directorio si no existe
    os.makedirs("output", exist_ok=True)
    
    # Define la ruta completa del archivo
    filepath = os.path.join("output", filename)
    
    # Guarda los datos en formato JSON con codificación UTF-8 y tildes
    with open(filepath, "w", encoding="utf-8") as json_file:
        json.dump(project_data, json_file, ensure_ascii=False, indent=4)
    
    print(f"El proyecto ha sido guardado exitosamente en: {filepath}")
