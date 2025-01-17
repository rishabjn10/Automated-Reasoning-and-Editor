import os
from dotenv import load_dotenv

load_dotenv(override = True)

LLM_CONFIGS = {
    "openai": {
        "model": "gpt-4o", # Change this to switch between LLMs
        "api_key": os.getenv('OPENAI_API_KEY')
    }
}

LLM_CONFIG = LLM_CONFIGS["openai"] # Change this to switch between LLMs

EDU_FLOW_INPUT_VARIABLES = {
    "audience_level": "intermediate",
    "topic": "How would you ensure compliance with relevant data privacy regulations (e.g., GDPR, CCPA) when developing an Agentic AI/RAG solution? How would you approach de-identification or anonymization of sensitive data used in an Agentic AI/RAG model? Explain with example use case and technical implementation"
} 