from typing import List, Dict, Any


class CitationManager:
    """
    Manages citations and source attribution
    """
    
    @staticmethod
    def format_sources(sources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Format sources with proper citation info"""
        formatted = []
        
        for idx, source in enumerate(sources, 1):
            formatted.append({
                'citation_number': idx,
                'title': source.get('title', 'Untitled'),
                'url': source.get('url', ''),
                'snippet': source.get('snippet', ''),
                'confidence_score': source.get('confidence', 1),
                'is_high_confidence': source.get('confidence', 1) >= 2
            })
        
        return formatted
    
    @staticmethod
    def generate_bibliography(sources: List[Dict[str, Any]]) -> str:
        """Generate formatted bibliography"""
        bib = "BIBLIOGRAPHY\n" + "="*50 + "\n\n"
        
        for source in sources:
            bib += f"[{source['citation_number']}] {source['title']}\n"
            bib += f"    URL: {source['url']}\n"
            if source['is_high_confidence']:
                bib += f"    ⭐ High Confidence (Cross-validated {source['confidence_score']}x)\n"
            bib += "\n"
        
        return bib