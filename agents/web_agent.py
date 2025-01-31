from phi.model.openai import OpenAIChat
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from tools.stock import get_company_symbol

web_agent = Agent(
    name="Web Agent",
    model=OpenAIChat(id="gpt-3.5-turbo"),
    tools=[DuckDuckGo(),  Newspaper4k(), get_company_symbol],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
