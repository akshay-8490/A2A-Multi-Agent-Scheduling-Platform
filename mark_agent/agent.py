# Step1: Agent & Tool

from crewai import LLM, Agent, Crew, Process, Task
from crewai.llms import cache as crewai_cache
from dotenv import load_dotenv
from tools import AvailabilityTool
import os

load_dotenv()


def _without_cache_breakpoint(message):
    return message


crewai_cache.mark_cache_breakpoint = _without_cache_breakpoint

class MarkAgent():

    SUPPORTED_CONTENT_TYPES = ["text", 'text/plain']

    def __init__(self):

        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment")
        
        # Use Groq provider via LiteLLM
        self.llm = LLM(
            model="groq/openai/gpt-oss-120b",
            api_key=self.api_key,
        )

        self.agent = Agent(
            role= "Scheduling Assistant",
            goal= "Answer questions about the Mark's availability using the calendar.",
            backstory= "You only answer scheduling questions and you always use the calendra tool.",
            tools= [AvailabilityTool()],
            llm= self.llm,
        )

    async def invoke(self, user_question):

        try:
            task = Task(
                description=f"Answer this question: '{user_question}'",
                expected_output="A clear answer about Mark's availability.",
                agent=self.agent
            )

            crew = Crew(
                    agents=[self.agent],
                    tasks=[task],
                    process=Process.sequential,
                )
            
            result = await crew.kickoff_async()
            return str(result) if result else "No response available"
        
        except Exception as e:
            print(f"[ERROR] mark_agent.invoke: {e}")
            return f"Sorry, I encountered an error: {str(e)}"


# mark_agent = MarkAgent()
# import asyncio
# print(asyncio.run(mark_agent.invoke("Hi, kya Mark available hai 14 Nov 2025 ko?")))