import os
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Setup Models
gemini = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key="YOUR_API_KEY")

# 2. Define Agents
finops_architect = Agent(
    role='FinOps Architect',
    goal='Ensure all infrastructure requests are cost-optimized and within budget',
    backstory='An expert in GCP cloud costs and architecture patterns.',
    llm=gemini,
    verbose=True
)

devops_engineer = Agent(
    role='DevOps Engineer',
    goal='Write valid Terraform code and test it in the E2B sandbox',
    backstory='A Terraform wizard with deep knowledge of GCS backends and HCL syntax.',
    llm=gemini, # Or Claude via Anthropic API
    verbose=True
)

# 3. Define Tasks
planning_task = Task(
    description='Analyze the request "{user_input}" and set a hard budget of {budget_limit}.',
    agent=finops_architect,
    expected_output='A technical spec including instance types and estimated monthly cost.'
)

coding_task = Task(
    description='Generate Terraform code based on the spec. Run "terraform validate" in E2B.',
    agent=devops_engineer,
    expected_output='Validated HCL code and successful Plan output.'
)

# 4. The Crew
sentinel_crew = Crew(
    agents=[finops_architect, devops_engineer],
    tasks=[planning_task, coding_task],
    process=Process.sequential
)

# Execute
# result = sentinel_crew.kickoff(inputs={'user_input': 'GKE Cluster', 'budget_limit': '$50'})
