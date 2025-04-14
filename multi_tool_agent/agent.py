from google.adk.agents import Agent
from multi_tool_agent.Utlis.const import ROOT_AGENT_INSTR




root_agent = Agent(
    model = "gemini-2.0-flash-001",
    instructions =ROOT_AGENT_INSTR,
    sub_agents = []

)