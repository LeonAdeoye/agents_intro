from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.text import TextKnowledgeBase
from phi.model.openai import OpenAIChat
from phi.agent import Agent
from phi.vectordb.lancedb import LanceDb
from phi.vectordb.search import SearchType
from agents.knowledge_agent import KnowledgeBaseManager

if __name__ == '__main__':
    knowledge_base_manager = KnowledgeBaseManager(source="./pdfs/Leon Adeoye Resume.pdf", debug_mode=True)
    agent_team = Agent(
        name="Agent Team",
        model=OpenAIChat(id="gpt-3.5-turbo"),
        team=[knowledge_base_manager.get_agent()],
    )
    agent_team.print_response("Extract details from the text knowledge base and use it to summarize what is in the knowledge base", stream=True)

    knowledge_base = TextKnowledgeBase(
        path="./text_files/leon.txt",
        vector_db=LanceDb(
            table_name="documents",
            uri="./lance.db",
            search_type=SearchType.keyword,
            embedder=OpenAIEmbedder(model="text-embedding-3-small"),
        ),
    )

    knowledge_base.load(recreate=True)

    agent = Agent(
        name="My Agent",
        model=OpenAIChat(id="gpt-3.5-turbo"),
        knowledge_base=knowledge_base,
        search_knowledge=True,
        debug_mode=True,
    )

    agent.print_response("Tell something about Leon Adeoye using the Knowledge base")





