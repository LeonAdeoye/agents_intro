from transformers import pipeline

def transformer():
    # Load MiniLM
    qa_pipeline = pipeline(
        "question-answering",
        model="distilbert-base-uncased-distilled-squad"
    )

    # Provide context and ask a question
    context = "I have acquired nearly 30 years of broad hands-on experience in software development and delivery. I have been fortunate to lead many cultural and gender-diverse teams of various sizes in multiple locations.I have a track record of high-quality, on-schedule delivery and expediting system development due to my strong ownership mentality, triage and organizational skills, stakeholder management, and client-first philosophy. I am also known for my exceptional leadership skills and my ability to motivate and mentor my team to achieve success in their projects and individual careers. I enable business to grow while keeping their costs down. I deliver successful project outcomes because of my passion, energy, drive, and interest in the latest technologies. I enjoy transforming lagging teams into highly motivated stand-out groups of talented & motivated individuals. I lead by example at all times.My Technical and Product Expertise includes:In-depth understanding of distributed and enterprise architectures.Lengthy exposure to multiple technology stacks, frameworks, software best practices.Equity and derivatives financial instrument and product expertise.Front-office application development: order management systems, client relationship management systems, automated index, arbitrage, automated market making, index pricing, sales trading tools, automated hedging, derivatives pricing, position checking, transaction cost analysis client reporting, & proprietary reporting platforms.Blockchain development: asymmetric cryptography, wallets, blockchain mining, decentralized network handshaking, proof-of-work consensus algorithm, Merkle trees, Bloom filters, full client & simplified payment verification nodes."
    question = "what have I been fortunate with?"

    # Get the answer
    answer = qa_pipeline(question=question, context=context)
    print(answer)