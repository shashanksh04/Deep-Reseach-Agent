# Deep Research Agent
An AI-powered autonomous agent that performs in-depth research on any topic by planning searches, gathering information from the web, synthesizing findings into a coherent report, and optionally emailing the results. Built with modular components leveraging OpenAI and Ollama language models for powerful natural language understanding and generation.

### Features
- Asynchronous workflow for efficient, multitasking research processes
- Intelligent planning of search queries for comprehensive information coverage
- Web search execution to gather relevant data
- Report generation with well-structured summaries and insights
- Optional email delivery of research reports
- Interactive web UI with Gradio for ease of use and real-time progress display
- Traceability via unique trace IDs to monitor research workflow steps

### Repository Components
- research_manager.py: Core manager orchestrating the entire research process asynchronously.
- planner_agent.py: Plans search strategies and queries.
- search_agent.py: Executes web searches and collects results.
- writer_agent.py: Synthesizes search results into a readable report.
- email_agent.py: Sends the final report through email.
- deep_research.py: Entry-point script providing a Gradio-based user interface.
