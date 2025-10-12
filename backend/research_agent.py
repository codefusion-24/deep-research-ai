import asyncio
from typing import Dict, Any, Callable
from query_decomposer import QueryDecomposer
from multi_agent_executor import MultiAgentExecutor
from synthesizer import ResearchSynthesizer
from citation_manager import CitationManager
import time


class DeepResearchAgent:
    """
    Main orchestrator for the Deep Research System
    Implements the complete workflow from the diagram
    """
    
    def __init__(self):
        self.decomposer = QueryDecomposer()
        self.executor = MultiAgentExecutor()
        self.synthesizer = ResearchSynthesizer()
        self.citation_manager = CitationManager()
        self.progress_callback = None
    
    def set_progress_callback(self, callback: Callable):
        """Set callback for progress updates"""
        self.progress_callback = callback
        self.executor.set_progress_callback(callback)
    
    async def run_research(self, query: str, max_tasks: int = 5) -> Dict[str, Any]:
        """
        Execute complete deep research workflow
        """
        start_time = time.time()
        
        print(f"\n" + "="*70)
        print(f"🚀 DEEP RESEARCH SYSTEM - Starting Research")
        print(f"="*70)
        print(f"Query: {query}")
        print(f"Max Tasks: {max_tasks}")
        
        try:
            # STEP 1: Query Analysis & Planning (Chain of Thought)
            self._update_progress("Planning", "Decomposing query with Chain of Thought", 10)
            decomposition = self.decomposer.decompose(query)
            dimensions = decomposition['decomposition']['dimensions']
            
            self._update_progress("Planning", f"Identified {len(dimensions)} research dimensions", 20)
            
            # STEP 2: Multi-Agent Execution
            self._update_progress("Execution", f"Launching {len(dimensions)} research agents", 30)
            agent_results = await self.executor.execute_research(dimensions)
            
            self._update_progress("Execution", "All agents completed", 50)
            
            # STEP 3: Aggregation & Synthesis
            self._update_progress("Synthesis", "Applying Self-Consistency aggregation", 60)
            aggregated = self.synthesizer.aggregate_results(agent_results)
            
            self._update_progress("Synthesis", "Extracting insights", 70)
            insights = self.synthesizer.extract_insights(aggregated)
            
            # STEP 4: Report Generation
            self._update_progress("Generation", "Generating comprehensive report with LLM", 80)
            report = self.synthesizer.generate_comprehensive_report(query, insights)
            
            # STEP 5: Citation Formatting
            self._update_progress("Finalization", "Formatting citations", 90)
            report['formatted_sources'] = self.citation_manager.format_sources(report['all_sources'])
            report['bibliography'] = self.citation_manager.generate_bibliography(report['formatted_sources'])
            
            # Add planning info
            report['planning'] = {
                'original_query': query,
                'decomposition_strategy': decomposition['strategy'],
                'dimensions': [
                    {
                        'aspect': d['aspect'],
                        'rationale': d['rationale'],
                        'queries': d['queries']
                    }
                    for d in dimensions
                ],
                'total_searches': decomposition['total_searches']
            }
            
            # Add execution summary
            report['execution_summary'] = {
                'agents_deployed': len(dimensions),
                'total_sources_found': sum(ar['result_count'] for ar in agent_results),
                'processing_time': round(time.time() - start_time, 2)
            }
            
            self._update_progress("Complete", "Research complete!", 100)
            
            print(f"\n" + "="*70)
            print(f"✅ RESEARCH COMPLETE")
            print(f"="*70)
            print(f"Time: {report['execution_summary']['processing_time']}s")
            print(f"Sources: {report['metadata']['total_sources']}")
            print(f"High Confidence: {report['metadata']['high_confidence_sources']}")
            
            return report
            
        except Exception as e:
            print(f"\n❌ Error during research: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def _update_progress(self, stage: str, message: str, progress: int):
        """Update progress if callback is set"""
        if self.progress_callback:
            self.progress_callback({
                'stage': stage,
                'message': message,
                'progress': progress
            })