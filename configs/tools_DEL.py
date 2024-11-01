import random
import pandas as pd

def load_courses_and_projects(excel_file):
    df_courses = pd.read_excel(excel_file, sheet_name='Sheet1')
    df_projects = pd.read_excel(excel_file, sheet_name='Temas de Proyectos')
    return df_courses, df_projects

def generate_project(context_variables):
    excel_file = context_variables.get("excel_file")
    df_courses, df_projects = load_courses_and_projects(excel_file)
    
    # Solicitar información de participantes, dificultad y tema
    participants = int(input("How many participants? (2-6): "))
    difficulty = int(input("What is the difficulty level? (1-5): "))
    project_topic = input("What is the project topic? Or type 'random' to let the agent choose: ")
    
    # Si el tema es 'random', seleccionar uno aleatorio
    if project_topic.lower() == 'random':
        project_topic = random.choice(df_projects['Tema del Proyecto'].tolist())

    # Seleccionar cursos aleatorios para los participantes
    selected_courses = df_courses.sample(participants)['Curso'].tolist()

    # Crear el proyecto
    project = {
        "title": f"Project on {project_topic}",
        "objective": "Develop a comprehensive solution based on the knowledge acquired in the course.",
        "rewards": "Learning",
        "challenges": [],
        "deadline": "30 days from now",
        "participants": selected_courses,
        "difficulty": difficulty
    }
    
    # Generar los retos personalizados
    for i, course in enumerate(selected_courses):
        task = {
            "task": f"Task for participant {i + 1}",
            "subtasks": [f"Subtask based on {course} - 1", f"Subtask based on {course} - 2"]
        }
        project["challenges"].append(task)

    return project
