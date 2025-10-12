from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import traceback
from research_agent import DeepResearchAgent

app = FastAPI(
    title="Deep Research AI - Full System",
    version="4.0",
    description="Advanced multi-agent research system with Chain of Thought, Self-Consistency, and LLM synthesis"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    query: str
    max_tasks: Optional[int] = 5


class HealthResponse(BaseModel):
    status: str
    message: str
    version: str
    features: list


@app.get("/", response_model=HealthResponse)
def home():
    """Health check endpoint"""
    return {
        "status": "operational",
        "message": "Deep Research AI - Full System Running",
        "version": "4.0",
        "features": [
            "Chain of Thought Query Decomposition",
            "Multi-Agent Parallel Execution",
            "Self-Consistency Aggregation",
            "Sequential Revision Synthesis",
            "Tree of Thoughts Planning",
            "Advanced Citation Management"
        ]
    }


@app.get("/health")
def health_check():
    """Detailed health check"""
    from config import config
    
    return {
        "status": "healthy",
        "openrouter_configured": bool(config.OPENROUTER_API_KEY),
        "serpapi_configured": bool(config.SERPAPI_KEY),
        "model": config.MODEL_NAME,
        "max_parallel_agents": config.MAX_PARALLEL_AGENTS
    }


@app.post("/run")
async def run_research(request: ResearchRequest):
    """
    Execute deep research with full advanced features
    
    This endpoint implements:
    - Chain of Thought query decomposition
    - Multi-agent parallel search execution
    - Self-Consistency aggregation
    - Sequential Revision synthesis
    - Comprehensive citation management
    """
    
    if not request.query or not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    try:
        print(f"\n{'='*70}")
        print(f"📨 Received research request: {request.query}")
        print(f"{'='*70}")
        
        # Create agent and execute research (async)
        agent = DeepResearchAgent()
        result = await agent.run_research(request.query, request.max_tasks)
        
        return result
        
    except Exception as e:
        error_detail = f"Research failed: {str(e)}"
        print(f"\n❌ {error_detail}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=error_detail)


@app.get("/test")
def test_endpoint():
    """Quick test endpoint"""
    return {
        "message": "Backend is working!",
        "timestamp": __import__('datetime').datetime.now().isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    print("\n" + "="*70)
    print("🚀 Starting Deep Research AI Backend - Full System")
    print("="*70)
    print("Features:")
    print("  ✅ Chain of Thought Decomposition")
    print("  ✅ Multi-Agent Parallel Execution")
    print("  ✅ Self-Consistency Aggregation")
    print("  ✅ Sequential Revision Synthesis")
    print("  ✅ Advanced Citation Management")
    print("="*70 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)