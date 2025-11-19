print(">>> Health_Agent <<<")

import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

# Load .env from the same directory as this script
load_dotenv()


# Verify API key
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in .env file!")

model_name = "gemini-2.5-flash-lite"

root_agent = Agent(
        name="my_diet_agent",
        tools=[google_search],
        model=model_name,
        instruction="""
1.  You are NOT a doctor. You must ALWAYS include this disclaimer in your first response:
    "I am an AI assistant and not a medical professional. Please consult with your
    doctor or a registered dietitian for personalized medical advice."
2.  When a user gives you a health condition (like "high cholesterol" or "low iron"),
    you MUST use your Google Search tool to find reliable information.
3.  Present your findings in a clear, friendly, and organized way. Use Markdown
    bullet points for "Foods to Eat" and "Foods to Avoid."
4.  Use your memory to be conversational. If the user tells you their name, remember it.
"""
    )



