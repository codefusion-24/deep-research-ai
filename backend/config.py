import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    SERPAPI_KEY = os.getenv("SERPAPI_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "openai/gpt-4o-mini")
    
    # API Endpoints
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
    SERPAPI_BASE_URL = "https://serpapi.com/search.json"
    
    # Research Configuration
    MAX_PARALLEL_AGENTS = 3
    SEARCHES_PER_AGENT = 3
    MAX_SOURCES_PER_DIMENSION = 15
    CONFIDENCE_THRESHOLD = 2  # Sources mentioned 2+ times = high confidence
    
    # LLM Parameters
    TEMPERATURE = 0.4
    MAX_TOKENS = 2000

config = Config()