from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.text import TextKnowledgeBase
from phi.model.openai import OpenAIChat
from phi.agent import Agent
from phi.vectordb.lancedb import LanceDb
from phi.vectordb.search import SearchType
from agents.knowledge_agent import KnowledgeBaseManager
from tools.get_info import get_info
from tools.transformer import transformer

if __name__ == '__main__':
    get_info()
    transformer()

    knowledge_base_manager = KnowledgeBaseManager(source="./pdfs/resume.pdf", debug_mode=False)
    agent_team = Agent(
        name="Agent Team",
        model=OpenAIChat(id="gpt-3.5-turbo"),
        team=[knowledge_base_manager.get_agent()],
    )
    agent_team.print_response("I have uploaded a resume of a candidate into a knowledge base. Extract details from the knowledge base and tell me as much as possible about the candidate", stream=True)

    knowledge_base = TextKnowledgeBase(
        path="./text_files/leon.txt",
        vector_db=LanceDb(
            table_name="documents",
            uri="./lance.db",
            search_type=SearchType.keyword,
            embedder=OpenAIEmbedder(model="text-embedding-3-small"),
        ),
    )

    knowledge_base.load()

    agent = Agent(
        name="My Agent",
        model=OpenAIChat(id="gpt-3.5-turbo"),
        knowledge_base=knowledge_base,
        search_knowledge=True,
        debug_mode=False
    )

    agent.print_response("I have uploaded Leon Adeoye's resume which has information about Leon's technical skills, previous workplaces, etc. Tell me as much as you can about Leon Adeoye has using the Knowledge base")





