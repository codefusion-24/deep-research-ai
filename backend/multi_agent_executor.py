import asyncio
import aiohttp
import requests
from typing import List, Dict, Any
from config import config
import time


class MultiAgentExecutor:
    """
    Implements parallel multi-agent search execution with progress tracking.
    Each agent is responsible for one research dimension.
    """
    
    def __init__(self):
        self.config = config
        self.progress_callback = None
    
    def set_progress_callback(self, callback):
        """Set callback for progress updates"""
        self.progress_callback = callback
    
    async def execute_research(self, dimensions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Execute parallel research across all dimensions using multi-agent approach
        """
        print(f"\n🤖 Launching {len(dimensions)} parallel research agents...")
        
        # Create tasks for parallel execution
        tasks = []
        for idx, dimension in enumerate(dimensions):
            task = self._agent_research(idx + 1, dimension)
            tasks.append(task)
        
        # Execute all agents in parallel
        results = await asyncio.gather(*tasks)
        
        print(f"✅ All {len(dimensions)} agents completed")
        return results
    
    async def _agent_research(self, agent_id: int, dimension: Dict[str, Any]) -> Dict[str, Any]:
        """
        Single agent executing searches for one dimension
        """
        aspect = dimension.get('aspect', f'Dimension {agent_id}')
        queries = dimension.get('queries', [])
        
        print(f"  Agent {agent_id} ({aspect}): Starting {len(queries)} searches...")
        
        if self.progress_callback:
            self.progress_callback({
                'agent_id': agent_id,
                'aspect': aspect,
                'status': 'searching',
                'progress': 0
            })
        
        all_results = []
        
        for idx, query in enumerate(queries):
            try:
                # Perform search
                results = await self._search_serpapi(query)
                all_results.extend(results)
                
                progress = int(((idx + 1) / len(queries)) * 100)
                print(f"  Agent {agent_id}: Query {idx + 1}/{len(queries)} - Found {len(results)} results")
                
                if self.progress_callback:
                    self.progress_callback({
                        'agent_id': agent_id,
                        'aspect': aspect,
                        'status': 'searching',
                        'progress': progress,
                        'current_query': query,
                        'results_found': len(results)
                    })
                
                # Rate limiting
                await asyncio.sleep(0.5)
                
            except Exception as e:
                print(f"  Agent {agent_id}: Error on query '{query}': {e}")
                continue
        
        if self.progress_callback:
            self.progress_callback({
                'agent_id': agent_id,
                'aspect': aspect,
                'status': 'complete',
                'progress': 100,
                'total_results': len(all_results)
            })
        
        print(f"  Agent {agent_id} ({aspect}): Complete - {len(all_results)} total results")
        
        return {
            'agent_id': agent_id,
            'aspect': aspect,
            'rationale': dimension.get('rationale', ''),
            'queries_executed': queries,
            'results': all_results,
            'result_count': len(all_results)
        }
    
    async def _search_serpapi(self, query: str) -> List[Dict[str, Any]]:
        """
        Perform async web search using SerpAPI
        """
        params = {
            "q": query,
            "api_key": self.config.SERPAPI_KEY,
            "num": 10,
            "engine": "google",
            "gl": "us",
            "hl": "en"
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.config.SERPAPI_BASE_URL, params=params, timeout=aiohttp.ClientTimeout(total=15)) as response:
                    if response.status == 200:
                        data = await response.json()
                        organic_results = data.get('organic_results', [])
                        
                        return [
                            {
                                'title': result.get('title', ''),
                                'url': result.get('link', ''),
                                'snippet': result.get('snippet', ''),
                                'position': result.get('position', 0),
                                'source_query': query
                            }
                            for result in organic_results
                        ]
                    else:
                        print(f"SerpAPI error: {response.status}")
                        return []
        except Exception as e:
            print(f"Search error: {e}")
            return []
