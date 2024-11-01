import os
from swarm import Agent
from configs.json_utils import load_project_from_json

# Función para revisar el proyecto y emitir una opinión
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
    
    # Criterios de evaluación flexibles
    opinion = "bueno"  # Valor por defecto
    reasons = []

    # Evaluación general de los campos principales
    required_fields = ["titulo", "objetivo"]
    for field in required_fields:
        if field not in project_data or not project_data[field]:
            opinion = "malo"
            reasons.append(f"El proyecto carece de un {field} claro.")

    # Evaluar campos adicionales si están presentes
    if "retos" in project_data:
        if len(project_data["retos"]) < 3:
            opinion = "regular" if opinion == "bueno" else opinion
            reasons.append("El proyecto tiene pocos retos. Se recomienda más variedad.")
    if "dificultad" in project_data:
        if project_data["dificultad"] < 2:
            reasons.append("El nivel de dificultad es bajo y podría no ser suficiente desafío.")
            opinion = "regular" if opinion != "malo" else opinion
        elif project_data["dificultad"] > 4:
            reasons.append("El nivel de dificultad es alto, lo que puede ser un desafío significativo para algunos estudiantes.")

    # Generar comentarios finales
    review_result = {
        "opinion": opinion,
        "reasons": reasons if reasons else ["El proyecto cumple con los criterios básicos."]
    }
    
    # Imprimir el resultado
    print(f"\nOpinión sobre el proyecto: {review_result['opinion'].capitalize()}")
    for reason in review_result["reasons"]:
        print(f"- {reason}")

    return review_result

# Definir el agente que realiza la revisión
project_reviewer_agent = Agent(
    name="Project Reviewer Agent",
    instructions="Al iniciar, este agente mostrará todos los archivos JSON en la carpeta 'output'. Luego, te pedirá que selecciones un archivo para revisar y emitirá una opinión sobre la calidad del proyecto.",
    functions=[review_project],
    parallel_tool_calls=False
)
