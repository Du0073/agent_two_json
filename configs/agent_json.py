#from configs.tools_DEL import generate_project
from swarm import Agent
from configs.json_utils import save_project_to_json
from configs.instructions import project_agent_instructions

#project creatorproject_agent_json
project_agent_json = Agent(
    name="Project Generator Agent",
    instructions=project_agent_instructions,
    functions=[save_project_to_json],
    parallel_tool_calls=False
)
