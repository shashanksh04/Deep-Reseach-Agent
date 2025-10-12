from pydantic import BaseModel, Field
from agents import Agent, OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI

ollama_client = AsyncOpenAI(base_url='http://localhost:11434/v1', api_key='ollama', timeout=7200)
llama_model = OpenAIChatCompletionsModel(model='gemma3:12b', openai_client=ollama_client)

INSTRUCTIONS = (
    "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 10-15 pages of content, at least 2500 words."
)


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")

    markdown_report: str = Field(description="The final report")

    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS,
    model=llama_model,
    output_type=ReportData,
)
