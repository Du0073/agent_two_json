import os
from configs.json_utils import load_project_from_json
from swarm import Agent

# Función para revisar el proyecto, emitir una opinión y generar un resumen
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


def project_reviewer_instructions(context_variables):
    return """
    Al iniciar, este agente mostrará todos los archivos JSON en la carpeta 'output'. 
    
    Te pedirá que selecciones un archivo para revisar, generará un resumen del contenido del proyecto, y además podrás hacer preguntas específicas sobre los campos del proyecto, como el título, objetivo, recompensa, retos, fecha, participantes y dificultad.
    """


# Definir el agente que realiza la revisión
project_reviewer_agent = Agent(
    name="Project Reviewer Agent",
    instructions=project_reviewer_instructions,
    functions=[review_project],
    parallel_tool_calls=False
)
