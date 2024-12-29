from phi.agent import Agent
from phi.tools.github import GithubTools
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.wikipedia import WikipediaTools
import os

load_dotenv()

def get_project_ideas(technologies, level):
    api_key = os.getenv("GROQ_API_KEY")
    github_token = os.getenv("GITHUB_ACCESS_TOKEN")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    if not github_token:
        raise ValueError("GITHUB_ACCESS_TOKEN not found in environment variables")

    agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        instructions=[
            "Make a call to the github tool for information on repositories.",
            "Your goal is to find project ideas using the technologies and skill level provided by the user.",
            "First suggest some project ideas then suggest some repositories from github.",
            "Return the most famous repositories first along with number of forks and stars of each repository.",
            "Keep the response concise and clean and include urls for github repositories."
        ],
        tools=[
            GithubTools(
                    access_token=github_token,
                    search_repositories=True,
                    get_repository=True
                )
        ],
        api_key=api_key,
        # show_tool_calls=True,
        markdown=True
    )
    
    response = agent.run(
        "Project ideas using {} for {} level".format(technologies, level)
    )
    
    return response.content

def get_trending_technologies():
    api_key = os.getenv("GROQ_API_KEY")
    github_token = os.getenv("GITHUB_ACCESS_TOKEN")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    if not github_token:
        raise ValueError("GITHUB_ACCESS_TOKEN not found in environment variables")

    wiki_agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        instructions=[
            "Your goal is to find trending technologies from finding information on internet.",
            "You can use wikipedia tool to get the information."
            "Return the response in a concise and clean manner."
            "Give tables for the top 5 trending technologies and top 5 trending languages along with statitics in markdown.",
            "Also can you the provide the articles from which you got the information."
        ],
        tools=[WikipediaTools()],
        markdown=True
    )
    try:
        response = wiki_agent.run()
    except Exception as e:
        return "Error: " + str(e)
    return response.content