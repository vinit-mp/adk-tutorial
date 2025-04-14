from google.ai import generativeai as genai
import requests
from bs4 import BeautifulSoup
import os



booking_agent = Agent(
    model="gemini-2.0-flash-001",
    name="booking_agent",
    description="Given an itinerary, complete the bookings of items by handling payment choices and processing.",
    instruction=prompt.BOOKING_AGENT_INSTR,
    tools=[
        AgentTool(agent=create_reservation),
        AgentTool(agent=payment_choice),
        AgentTool(agent=process_payment),
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.0, top_p=0.5
    )
)