# Step1: Agent & Tool

import os
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages.ai import AIMessage
from tools import get_availability

load_dotenv()
memory = MemorySaver()

class JeffAgent():

    SUPPORTED_CONTENT_TYPES = ["text", 'text/plain']

    def __init__(self):

        self.model = ChatGroq(
            model="openai/gpt-oss-120b",
            api_key=os.getenv("GROQ_API_KEY"),
        )
        self.tools = [get_availability] if get_availability else []
        self.system_pmpt = "You are a scheduling personal assistant for Jeff Bezo's"
        self.graph = create_agent(
            self.model,
            tools = self.tools,
            system_prompt = self.system_pmpt,
            checkpointer = memory
        )

    async def get_response(self, query, context_id):

        inputs = {"messages": [("user", query)]}
        config = {"configurable": {"thread_id": context_id}}
        raw_response = await self.graph.ainvoke(inputs, config)
        messages = raw_response.get("messages", [])
        ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

        if not ai_messages:
            return {"content": "No response"}

        content = ai_messages[-1]
        if isinstance(content, list):
            text_parts = [part.get("text", "") if isinstance(part, dict) else str(part) for part in content]
            response = " ".join(text_parts)
        else:
            response = str(content)

        return {"content": response}

# agent = JeffAgent()
# import asyncio
# response = asyncio.run(agent.get_response(query="Is Jeff available on 8th Nov 2025?", context_id = 1234))
# print(response)