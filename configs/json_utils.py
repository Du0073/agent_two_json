import json
import os

#---------------------------------------------------------
#FOR AGENT: agent_json_project
#---------------------------------------------------------
def save_project_to_json(project_data, filename="proyecto_generado.json"):
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    with open(filepath, "w", encoding="utf-8") as json_file:
        json_str = json.dumps(project_data, ensure_ascii=False).replace("\\n", "").replace("\\", "")
        if json_str.startswith('"') and json_str.endswith('"'):
            json_str = json_str[1:-1]
        json_file.write(json_str)
    print(f"El proyecto ha sido guardado exitosamente en: {filepath}")

#---------------------------------------------------------
#FOR AGENT: agent_reviewer
#---------------------------------------------------------

def load_project_from_json(filepath="output/proyecto_generado.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as json_file:
            project_data = json.load(json_file)
        print(f"Proyecto cargado desde {filepath}")
        return project_data
    except FileNotFoundError:
        print(f"Archivo {filepath} no encontrado.")
        return None

def review_project(context_variables):
    # Listar archivos en la carpeta output
    output_dir = "output"
    files = [f for f in os.listdir(output_dir) if f.endswith(".json")]

    # Verificar si hay archivos en la carpeta output
    if not files:
        print("No se encontraron archivos JSON en la carpeta 'output'.")
        return None
    
    # Mostrar los archivos disponibles al usuario
    print("Archivos disponibles en la carpeta 'output':")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    
    # Solicitar al usuario que seleccione un archivo
    while True:
        try:
            choice = int(input("Seleccione el número del archivo que desea revisar: "))
            if 1 <= choice <= len(files):
                selected_file = files[choice - 1]
                break
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(files)}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    # Cargar el archivo JSON seleccionado
    project_file = os.path.join(output_dir, selected_file)
    project_data = load_project_from_json(project_file)
    
    # Almacenar el contenido del archivo en context_variables para acceso continuo
    context_variables["project_data"] = project_data

    # Generar un resumen del proyecto
    resumen = f"Resumen del Proyecto:\n"
    resumen += f"Título: {project_data.get('Titulo', 'No especificado')}\n"
    resumen += f"Objetivo: {project_data.get('Objetivo', 'No especificado')}\n"
    resumen += f"Recompensa: {project_data.get('Recompensa', 'No especificada')}\n"
    resumen += f"Fecha Límite: {project_data.get('Fecha', 'No especificada')}\n"
    resumen += f"Dificultad: {project_data.get('Dificultad', 'No especificada')}\n"
    
    # Resumir los retos y subtareas
    resumen += "Retos:\n"
    for idx, reto in enumerate(project_data.get("Retos", []), 1):
        # Verificar si "reto" es un diccionario
        if isinstance(reto, dict):
            resumen += f"  Reto {idx}: {reto.get('Tarea', 'No especificada')}\n"
            for subtarea in reto.get("Subtareas", []):
                resumen += f"    - {subtarea}\n"
        else:
            # En caso de que el reto no sea un diccionario
            resumen += f"  Reto {idx}: Información no especificada o en formato incorrecto\n"
    
    # Listar los participantes
    participantes = project_data.get("Participantes", [])
    resumen += "Participantes:\n" + "\n".join([f"  - {participante}" for participante in participantes]) + "\n"

    # Imprimir el resumen
    print(resumen)

    # Almacenar el resumen en context_variables para consultas futuras
    context_variables["project_summary"] = resumen

    return resumen

