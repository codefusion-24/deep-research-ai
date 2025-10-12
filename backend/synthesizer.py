import requests
from typing import List, Dict, Any
from collections import Counter
from config import config


class ResearchSynthesizer:
    """
    Implements Self-Consistency aggregation and Sequential Revision
    for synthesizing research findings into comprehensive reports.
    """
    
    def __init__(self):
        self.config = config
    
    def aggregate_results(self, agent_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Self-Consistency: Aggregate and deduplicate results across agents
        Cross-validate sources that appear multiple times
        """
        print(f"\n🔄 Self-Consistency: Aggregating results from {len(agent_results)} agents...")
        
        aggregated = []
        
        for agent_result in agent_results:
            aspect = agent_result['aspect']
            results = agent_result['results']
            
            # Deduplicate by URL and track confidence
            url_map = {}
            
            for result in results:
                url = result['url']
                if url in url_map:
                    # Source appeared in multiple queries - increase confidence
                    url_map[url]['confidence'] += 1
                    # Merge snippets if different
                    if result['snippet'] and result['snippet'] not in url_map[url]['snippet']:
                        url_map[url]['snippet'] += " " + result['snippet']
                else:
                    url_map[url] = {
                        **result,
                        'confidence': 1
                    }
            
            # Sort by confidence (cross-validation) and position
            sorted_results = sorted(
                url_map.values(),
                key=lambda x: (x['confidence'], -x['position']),
                reverse=True
            )
            
            # Take top results
            top_results = sorted_results[:self.config.MAX_SOURCES_PER_DIMENSION]
            
            high_confidence = sum(1 for r in top_results if r['confidence'] >= self.config.CONFIDENCE_THRESHOLD)
            
            print(f"  {aspect}: {len(top_results)} sources ({high_confidence} high-confidence)")
            
            aggregated.append({
                'aspect': agent_result['aspect'],
                'rationale': agent_result['rationale'],
                'agent_id': agent_result['agent_id'],
                'sources': top_results,
                'total_sources': len(top_results),
                'high_confidence_sources': high_confidence
            })
        
        return aggregated
    
    def extract_insights(self, aggregated_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Extract key insights from each research dimension
        """
        print(f"\n💡 Extracting insights from {len(aggregated_data)} dimensions...")
        
        insights = []
        
        for dimension in aggregated_data:
            key_points = []
            
            for source in dimension['sources'][:8]:  # Top 8 sources
                if source.get('snippet') and len(source['snippet']) > 50:
                    snippet = source['snippet'].strip()
                    if len(snippet) > 300:
                        snippet = snippet[:297] + "..."
                    
                    key_points.append({
                        'text': snippet,
                        'source': {
                            'title': source['title'],
                            'url': source['url']
                        },
                        'confidence': source['confidence'],
                        'is_high_confidence': source['confidence'] >= self.config.CONFIDENCE_THRESHOLD
                    })
            
            insights.append({
                'aspect': dimension['aspect'],
                'rationale': dimension['rationale'],
                'key_points': key_points,
                'sources': dimension['sources'],
                'metadata': {
                    'total_sources': dimension['total_sources'],
                    'high_confidence_sources': dimension['high_confidence_sources']
                }
            })
            
            print(f"  {dimension['aspect']}: {len(key_points)} key insights")
        
        return insights
    
    def generate_comprehensive_report(self, query: str, insights: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Sequential Revision: Generate comprehensive report using LLM
        """
        print(f"\n📝 Generating comprehensive report with LLM...")
        
        # Prepare context
        context = self._prepare_context(query, insights)
        
        # Generate executive summary
        print("  Generating executive summary...")
        executive_summary = self._generate_executive_summary(query, context)
        
        # Generate detailed sections
        print("  Generating detailed sections...")
        sections = []
        for insight in insights:
            section = self._generate_section(insight)
            sections.append(section)
        
        # Collect all sources
        all_sources = []
        seen_urls = set()
        for insight in insights:
            for source in insight['sources']:
                if source['url'] not in seen_urls:
                    all_sources.append({
                        'title': source['title'],
                        'url': source['url'],
                        'snippet': source.get('snippet', ''),
                        'confidence': source['confidence']
                    })
                    seen_urls.add(source['url'])
        
        # Sort by confidence
        all_sources.sort(key=lambda x: x['confidence'], reverse=True)
        
        # Generate verification
        verification = self._generate_verification(insights)
        
        report = {
            'query': query,
            'executive_summary': executive_summary,
            'sections': sections,
            'all_sources': all_sources,
            'verification': verification,
            'metadata': {
                'total_sources': len(all_sources),
                'high_confidence_sources': sum(1 for s in all_sources if s['confidence'] >= self.config.CONFIDENCE_THRESHOLD),
                'dimensions': len(sections),
                'techniques_used': [
                    'Chain of Thought',
                    'Multi-Agent Execution',
                    'Self-Consistency',
                    'Sequential Revision',
                    'Tree of Thoughts'
                ]
            }
        }
        
        print(f"✅ Report complete: {len(sections)} sections, {len(all_sources)} sources")
        
        return report
    
    def _prepare_context(self, query: str, insights: List[Dict[str, Any]]) -> str:
        """Prepare context for LLM"""
        context = f"Research Query: {query}\n\n"
        context += "=== RESEARCH FINDINGS ===\n\n"
        
        for insight in insights:
            context += f"## {insight['aspect']}\n"
            context += f"Rationale: {insight['rationale']}\n\n"
            context += "Key Findings:\n"
            
            for idx, point in enumerate(insight['key_points'][:5], 1):
                confidence_marker = "⭐⭐" if point['is_high_confidence'] else "⭐"
                context += f"{idx}. {confidence_marker} {point['text']}\n"
                context += f"   Source: {point['source']['title']}\n\n"
        
        return context
    
    def _generate_executive_summary(self, query: str, context: str) -> str:
        """Generate executive summary using LLM"""
        prompt = f"""You are a research analyst. Write a comprehensive executive summary (4-5 paragraphs) based on the research findings below.

{context}

Requirements:
- Synthesize key insights across all dimensions
- Highlight the most important findings
- Mention that this used advanced multi-agent research with cross-validation
- Be specific and data-driven
- Professional tone

Executive Summary:"""
        
        try:
            return self._call_llm(prompt, max_tokens=1500)
        except Exception as e:
            return f"Executive summary generation encountered an error: {e}"
    
    def _generate_section(self, insight: Dict[str, Any]) -> Dict[str, Any]:
        """Generate detailed section for one dimension"""
        context = f"Research Dimension: {insight['aspect']}\n"
        context += f"Rationale: {insight['rationale']}\n\n"
        context += "Findings:\n"
        
        for idx, point in enumerate(insight['key_points'][:6], 1):
            conf = "High Confidence" if point['is_high_confidence'] else "Standard"
            context += f"{idx}. [{conf}] {point['text']}\n"
        
        prompt = f"""Based on these research findings, write a comprehensive analysis (3-4 paragraphs) for "{insight['aspect']}":

{context}

Requirements:
- Detailed analysis with context
- Identify trends and patterns
- Professional, analytical tone
- Be specific and insightful

Analysis:"""
        
        try:
            content = self._call_llm(prompt, max_tokens=1200)
        except Exception as e:
            content = f"Analysis for {insight['aspect']} could not be generated: {e}"
        
        return {
            'title': insight['aspect'],
            'content': content,
            'key_points': insight['key_points'][:6],
            'source_count': insight['metadata']['total_sources'],
            'high_confidence_count': insight['metadata']['high_confidence_sources']
        }
    
    def _generate_verification(self, insights: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate verification items"""
        verification = []
        
        total_sources = sum(i['metadata']['total_sources'] for i in insights)
        hc_sources = sum(i['metadata']['high_confidence_sources'] for i in insights)
        
        verification.append({
            'claim': f"Research executed across {len(insights)} dimensions with multi-agent parallel search",
            'supported_by': [f"{len(insights)} independent research agents", "Cross-validated sources"]
        })
        
        verification.append({
            'claim': f"Found {total_sources} unique sources, {hc_sources} cross-validated across multiple queries",
            'supported_by': ["Self-Consistency validation", "Source deduplication"]
        })
        
        for insight in insights:
            if insight['metadata']['high_confidence_sources'] > 0:
                verification.append({
                    'claim': f"{insight['aspect']}: {insight['metadata']['high_confidence_sources']} high-confidence sources identified",
                    'supported_by': [f"Agent {insight.get('agent_id', 'N/A')}", "Multiple query validation"]
                })
        
        return verification
    
    def _call_llm(self, prompt: str, max_tokens: int = 1000) -> str:
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
                {
                    "role": "system",
                    "content": "You are an expert research analyst providing comprehensive, well-structured analysis."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": self.config.TEMPERATURE,
            "max_tokens": max_tokens
        }
        
        response = requests.post(self.config.OPENROUTER_BASE_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']

