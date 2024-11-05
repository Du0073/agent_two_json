from fastapi import FastAPI, HTTPException
from configs.agents import agent_json_project, agent_reviewer
from configs.json_utils import save_project_to_json, load_project_from_json
from pydantic import BaseModel
import os

app = FastAPI()

class ProjectRequest(BaseModel):
    title: str
    description: str

@app.post("/generate-project")
async def generate_project(request: ProjectRequest):
    context_variables = {
        "project_title": request.title,
        "project_description": request.description,
    }
    # Ejecuta el agente para generar el proyecto y guarda en JSON
    project_data = agent_json_project.run(context_variables)
    
    # Guardar el proyecto en un archivo JSON
    save_project_to_json(project_data, filename="proyecto_generado.json")
    
    return {"message": "Project generated successfully", "data": project_data}

@app.get("/review-project/{project_name}")
async def review_project(project_name: str):
    filepath = f"output/{project_name}.json"
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Project file not found")

    # Cargar y revisar el proyecto
    project_data = load_project_from_json(filepath)
    review_summary = agent_reviewer.run({"project_data": project_data})
    return {"review": review_summary}
