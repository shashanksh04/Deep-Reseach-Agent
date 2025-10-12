# websearch_tool.py

import asyncio
from typing import Any, Dict, List
from agents.tool import FunctionTool
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

class OllamaWebSearchTool(FunctionTool):
    def __init__(
        self,
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "ollama",
        model_name: str = "mistral:7b",
        num_results: int = 5,
    ):
        # Build the JSON schema for the 'query' parameter
        params_schema = {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search terms"}
            },
            "required": ["query"],
        }

        # Call the parent constructor correctly
        super().__init__(
            name="ollama_web_search",
            description="Search the web using Ollama LLM and return a concise summary.",
            params_json_schema=params_schema,
            on_invoke_tool=self._run  # internal handler
        )

        # Setup the LLM client and model
        self.client = AsyncOpenAI(base_url=base_url, api_key=api_key)
        self.model = OpenAIChatCompletionsModel(model=model_name, openai_client=self.client)
        self.num_results = num_results

    async def _run(self, tool_input: Dict[str, Any]) -> str:
        query = tool_input["query"]
        # Stub: replace with real HTTP fetch logic
        snippets = [f"Snippet {i+1} for '{query}'" for i in range(self.num_results)]

        prompt = (
            f"Summarize these web snippets for: {query}\n\n"
            + "\n\n".join(snippets)
            + "\n\nWrite 2–3 paragraphs (<300 words)."
        )
        response = await self.model.generate([{"role": "user", "content": prompt}])
        return response.choices[0].message.content
