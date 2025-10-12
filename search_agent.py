from agents import Agent, ModelSettings, OpenAIChatCompletionsModel
from websearch_tool import OllamaWebSearchTool
from openai import AsyncOpenAI

ollama_client = AsyncOpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
llama_model = OpenAIChatCompletionsModel(model='mistral:7b', openai_client=ollama_client)

INSTRUCTIONS = (
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 150 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself."
)

# search_agent = Agent(
#     name="Search agent",
#     instructions=INSTRUCTIONS,
#     tools=[WebSearchTool(search_context_size="low")],
#     model=llama_model,
#     model_settings=ModelSettings(tool_choice="required"),
# )

search_agent = Agent(
    name="Search agent",
    instructions=INSTRUCTIONS,
    tools=[OllamaWebSearchTool()],
    model=llama_model,
    model_settings=ModelSettings(tool_choice="required"),
)
