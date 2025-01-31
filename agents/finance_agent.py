from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from tools.stock import get_company_symbol

finance_agent = Agent(
    name="My Agent",
    model=OpenAIChat(id="gpt-3.5-turbo"),
    instructions=["Use table to display data.",
                  "If you don't know the company symbol, use get_company_symbol(company_name) tool to get it."],
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    show_tool_calls=True,
    markdown=True,
)
