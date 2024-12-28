from phi.agent import Agent
from phi.tools.github import GithubTools
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def get_project_ideas(technologies, level):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        api_key=api_key,
        markdown=True
    )
    
    response = agent.run(
        "Project ideas using {} for {} level".format(technologies, level)
    )
    
    return response.content