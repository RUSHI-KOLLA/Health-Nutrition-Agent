from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from agenthealth.agent import root_agent
import asyncio
import uuid

async def main():
    session_server = InMemorySessionService()
    
    initial_state = {
        "user_name": "dhanvantari",
        "user_id": "dhanvant123",
        "user_performance": """
           You are a helpful Health Nutritionist Agent.
           Your goal is to help users with food suggestions based on their health reports.
           """,
    }

    AGENT_NAME = "agents"
    USER_ID = "dhanvant123"
    SESSION_ID = str(uuid.uuid4())

    await session_server.create_session(
        app_name=AGENT_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state
)
    runner = Runner(
        agent=root_agent,
        app_name=AGENT_NAME,
        session_service= session_server
    )

    new_msg = types.Content(
        role='user',
        parts=[types.Part(text=input("Ask your diet question: "))]
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_msg,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"\n{event.content.parts[0].text}")

if __name__ == "__main__":
    asyncio.run(main())
