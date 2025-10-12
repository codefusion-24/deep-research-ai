import requests
from typing import List, Dict, Any
from config import config


class QueryDecomposer:
    """
    Implements Chain of Thought reasoning to decompose complex queries
    into structured research dimensions with targeted sub-queries.
    """
    
    def __init__(self):
        self.config = config
    
    def decompose(self, query: str) -> Dict[str, Any]:
        """
        Chain of Thought: Break down query into research dimensions
        """
        print(f"\n🧠 Chain of Thought: Analyzing query...")
        
        # Use LLM to intelligently decompose the query
        decomposition_prompt = f"""You are a research planning expert. Analyze this research query and break it down into 3 distinct research dimensions.

Query: "{query}"

For each dimension, provide:
1. Aspect name (what area of research)
2. 3 specific search queries that would gather relevant data

Respond in this exact JSON format:
{{
    "dimensions": [
        {{
            "aspect": "Dimension name",
            "rationale": "Why this dimension is important",
            "queries": ["query 1", "query 2", "query 3"]
        }}
    ]
}}

Focus on:
- Market/Industry analysis (if applicable)
- Key players/Competition (if applicable)
- Technical/Innovation aspects (if applicable)
- Or other relevant dimensions based on the query

Be specific and actionable."""

        try:
            response = self._call_llm(decomposition_prompt)
            
            # Parse LLM response
            import json
            # Extract JSON from response
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1
            if start_idx != -1 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                decomposition = json.loads(json_str)
            else:
                # Fallback to rule-based decomposition
                decomposition = self._fallback_decomposition(query)
            
        except Exception as e:
            print(f"⚠️  LLM decomposition failed, using rule-based: {e}")
            decomposition = self._fallback_decomposition(query)
        
        # Add metadata
        result = {
            "original_query": query,
            "decomposition": decomposition,
            "total_searches": sum(len(d.get("queries", [])) for d in decomposition.get("dimensions", [])),
            "strategy": "Chain of Thought + Tree of Thoughts"
        }
        
        print(f"✅ Decomposed into {len(decomposition.get('dimensions', []))} dimensions")
        return result
    
    def _fallback_decomposition(self, query: str) -> Dict[str, List[Dict[str, Any]]]:
        """Rule-based fallback decomposition"""
        query_lower = query.lower()
        
        dimensions = []
        
        # Competitive/Market queries
        if any(kw in query_lower for kw in ['competitive', 'landscape', 'market', 'analysis', 'compare', 'trends']):
            dimensions = [
                {
                    "aspect": "Market Overview & Trends",
                    "rationale": "Understanding market size, growth, and current trends",
                    "queries": [
                        f"{query} market size 2024",
                        f"{query} industry trends 2024",
                        f"{query} market analysis report"
                    ]
                },
                {
                    "aspect": "Key Players & Competition",
                    "rationale": "Identifying major companies and competitive dynamics",
                    "queries": [
                        f"leading companies {query}",
                        f"top competitors {query} 2024",
                        f"market leaders {query}"
                    ]
                },
                {
                    "aspect": "Technology & Innovation",
                    "rationale": "Latest technological developments and innovations",
                    "queries": [
                        f"latest technology {query}",
                        f"innovations {query} 2024",
                        f"technical advancements {query}"
                    ]
                }
            ]
        else:
            # General research
            dimensions = [
                {
                    "aspect": "Overview & Fundamentals",
                    "rationale": "Core concepts and background information",
                    "queries": [
                        query,
                        f"{query} overview 2024",
                        f"what is {query}"
                    ]
                },
                {
                    "aspect": "Current Developments",
                    "rationale": "Latest news and recent developments",
                    "queries": [
                        f"{query} 2024 latest",
                        f"{query} recent developments",
                        f"{query} news 2024"
                    ]
                },
                {
                    "aspect": "Expert Analysis",
                    "rationale": "Professional insights and analysis",
                    "queries": [
                        f"{query} expert opinion",
                        f"{query} analysis report",
                        f"{query} industry insights"
                    ]
                }
            ]
        
        return {"dimensions": dimensions}
    
    def _call_llm(self, prompt: str) -> str:
        """Call OpenRouter LLM"""
        headers = {
            "Authorization": f"Bearer {self.config.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://deep-research.app",
            "X-Title": "Deep Research System"
        }
        
        data = {
            "model": self.config.MODEL_NAME,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 1500
        }
        
        response = requests.post(self.config.OPENROUTER_BASE_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
