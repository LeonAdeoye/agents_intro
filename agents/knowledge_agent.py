from phi.knowledge.text import TextKnowledgeBase
from phi.model.openai import OpenAIChat
from phi.agent import Agent
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.embedder.openai import OpenAIEmbedder
from phi.model.base import Model
from tools.pdf_processor import extract_text_from_pdf_using_pymupdf, delete_temporary_file, \
    create_temporary_file_from_text, extract_text_from_pdf_using_pdfminer


class KnowledgeBaseManager:
    def __init__(self, source: str, debug_mode: bool = False, model: Model = OpenAIChat(id="gpt-3.5-turbo")):
        """Initialize the knowledge base manager."""
        self.source = source
        self.knowledge_base = None
        self.vector_db = self._initialize_vector_db()
        self._create_knowledge_base()
        self.debug_mode = debug_mode
        self.model = model

    @staticmethod
    def _initialize_vector_db() -> LanceDb:
        """Initialize LanceDB as the vector database."""
        return LanceDb(
            table_name="documents",
            uri="./lance.db",
            search_type=SearchType.vector,
            embedder=OpenAIEmbedder(model="text-embedding-3-small"),
        )

    def _create_knowledge_base(self):
        """Create the appropriate knowledge base depending on the `use_url` flag."""

        file_name = create_temporary_file_from_text(extract_text_from_pdf_using_pdfminer(self.source))
        self.knowledge_base = TextKnowledgeBase(
            name="Knowledge Base", path=file_name, vector_db=self.vector_db
        )
        self.knowledge_base.load()  # Load PDF content into the vector DB
        delete_temporary_file(file_name)

    def get_agent(self) -> Agent:
        """Create and return the knowledge agent."""
        return Agent(
            name="Knowledge Agent",
            model=self.model,
            knowledge=self.knowledge_base,
            add_context=True,
            search_knowledge=True,
            debug_mode=self.debug_mode,
        )




