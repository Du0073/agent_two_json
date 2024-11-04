from swarm import Agent
from configs.json_utils import save_project_to_json
from configs.json_utils import review_project
from data.instructions import instructions_json_pj
from data.instructions import instructions_reviewer

def transfer_to_review():
    return agent_reviewer

agent_json_project = Agent(
    name="Project Generator Agent",
    instructions=instructions_json_pj,
    functions=[save_project_to_json,transfer_to_review],
    parallel_tool_calls=False
)

def transfer_to_json_project():
    return agent_json_project

agent_reviewer = Agent(
    name="Project Reviewer Agent",
    instructions=instructions_reviewer,
    functions=[review_project,transfer_to_json_project],
    parallel_tool_calls=False
)
