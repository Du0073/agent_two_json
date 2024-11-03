# Project Review Agent

Este proyecto contiene un agente en Python diseñado para revisar proyectos almacenados en formato JSON, proporcionando un resumen y una opinión sobre la calidad de cada proyecto en función de sus principales características. La estructura se adapta para ser usada con GitHub y es fácil de ejecutar y mantener.

## Estructura del Proyecto
project_directory/

├── main.py

├── .env

├── output/
│   ├── proyecto1.json
│   └── proyecto2.json

└── configs/
    ├── agent_review.py  
    ├── json_utils.py
    └── tools.py



## Descripción de Archivos

### `main.py`
Archivo principal para ejecutar el agente `Project Reviewer Agent`. Este archivo importa el agente y lo ejecuta para interactuar con los archivos JSON del proyecto.

### `.env`
Archivo opcional para almacenar la clave de la API de OpenAI (si es necesaria), manteniendo las credenciales seguras fuera del código fuente.

### `output/`
Carpeta donde se almacenan los archivos JSON de proyectos. Cada archivo JSON debe incluir información clave como `Titulo`, `Objetivo`, `Recompensa`, `Retos`, `Fecha`, `Participantes`, y `Dificultad`.

### `configs/`
Contiene los archivos de configuración y funciones auxiliares para el agente.

- **`agent_review.py`**: Define el agente `Project Reviewer Agent`, que permite:
  - Listar y seleccionar un archivo JSON de la carpeta `output`.
  - Cargar y almacenar los datos del archivo en `context_variables` para consultas futuras.
  - Generar un resumen estructurado del proyecto, que incluye el título, objetivo, recompensa, lista de retos, fecha límite, participantes, y dificultad.

  Principales funciones:
  - `review_project(context_variables)`: Lista los archivos JSON, permite seleccionar uno y genera un resumen del contenido.
  - `project_reviewer_instructions(context_variables)`: Define las instrucciones de funcionamiento del agente, explicando cómo interactuar con los archivos JSON.

- **`json_utils.py`**: Contiene funciones de utilidad para cargar y guardar archivos JSON.
  - `load_project_from_json(file_path)`: Carga el archivo JSON en un diccionario Python para su posterior análisis por el agente.

- **`tools.py`**: Este archivo puede contener funciones adicionales para manipulación de datos u otras tareas de soporte según las necesidades del proyecto.

## Uso

1. **Clonar el repositorio** y asegurarse de que los archivos JSON estén en la carpeta `output/`.
2. **Ejecutar `main.py`** para iniciar el agente.
3. **Seguir las instrucciones en pantalla** para seleccionar un proyecto, generar el resumen y obtener la evaluación del proyecto.

## Cosas que faltan por hacer

Este proyecto aún requiere desarrollo adicional para mejorar su funcionalidad y alcance. Las próximas mejoras incluyen:

- **Modelado de escenarios de análisis**: Definir dos situaciones principales para el análisis: una para generar nuevos proyectos y otra para agrupar estudiantes.
- **Comunicación entre agentes**: Establecer un sistema de interacción entre los agentes para optimizar el procesamiento de los proyectos.
- **Conexión con una API externa**: Integrar el sistema con una API en desarrollo para facilitar el análisis y gestión de los proyectos.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un problema o tienes una sugerencia, no dudes en abrir una **issue** o crear un **pull request**.


