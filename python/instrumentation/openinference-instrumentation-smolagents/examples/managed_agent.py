import os

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    ManagedAgent,
    OpenAIServerModel,
    ToolCallingAgent,
)

from openinference.instrumentation.smolagents import SmolagentsInstrumentor

endpoint = "http://0.0.0.0:6006/v1/traces"
trace_provider = TracerProvider()
trace_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint)))

SmolagentsInstrumentor().instrument(tracer_provider=trace_provider, skip_dep_check=True)


model = OpenAIServerModel(
    model_id="gpt-4o",
    api_base="https://api.openai.com/v1",
    api_key=os.environ["OPENAI_API_KEY"],
)
agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    max_steps=3,
)
managed_agent = ManagedAgent(
    agent=agent,
    name="managed_agent",
    description=(
        "This is an agent that can do web search. "
        "When solving a task, ask him directly first, he gives good answers. "
        "Then you can double check."
    ),
)
manager_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    managed_agents=[managed_agent],
)
manager_agent.run(
    "How many seconds would it take for a leopard at full speed to run through Pont des Arts? "
    "ASK YOUR MANAGED AGENT FOR LEOPARD SPEED FIRST"
)
