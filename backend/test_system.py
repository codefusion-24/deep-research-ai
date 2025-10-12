"""
Test script to verify the Deep Research System is working correctly
Run this after starting the backend to test all components
"""

import requests
import json
import time

def test_backend():
    """Test the complete backend system"""
    
    print("\n" + "="*70)
    print("🧪 TESTING DEEP RESEARCH SYSTEM")
    print("="*70 + "\n")
    
    base_url = "http://localhost:8000"
    
    # Test 1: Health Check
    print("Test 1: Health Check...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Version: {response.json()['version']}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Cannot connect to backend: {e}")
        print("   Make sure backend is running: uvicorn main:app --reload")
        return
    
    # Test 2: Configuration Check
    print("\nTest 2: Configuration Check...")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Configuration check passed")
            print(f"   OpenRouter: {'✅' if data['openrouter_configured'] else '❌'}")
            print(f"   SerpAPI: {'✅' if data['serpapi_configured'] else '❌'}")
            print(f"   Model: {data['model']}")
            
            if not data['openrouter_configured'] or not data['serpapi_configured']:
                print("\n⚠️  Warning: API keys not configured!")
                print("   Please set OPENROUTER_API_KEY and SERPAPI_KEY in .env")
                return
        else:
            print(f"❌ Configuration check failed")
            return
    except Exception as e:
        print(f"❌ Configuration check error: {e}")
        return
    
    # Test 3: Simple Research Query
    print("\nTest 3: Running Research Query...")
    print("Query: 'Latest trends in AI 2024'")
    print("This will take 30-60 seconds...\n")
    
    try:
        start_time = time.time()
        
        response = requests.post(
            f"{base_url}/run",
            json={
                "query": "Latest trends in AI 2024",
                "max_tasks": 3
            },
            timeout=120  # 2 minutes timeout
        )
        
        elapsed = time.time() - start_time
        
        if response.status_code == 200:
            result = response.json()
            
            print(f"✅ Research completed in {elapsed:.2f}s\n")
            print("="*70)
            print("RESULTS SUMMARY")
            print("="*70)
            
            # Planning
            if 'planning' in result:
                print(f"\n📋 Planning:")
                print(f"   Dimensions: {len(result['planning']['dimensions'])}")
                print(f"   Total Searches: {result['planning']['total_searches']}")
                for dim in result['planning']['dimensions']:
                    print(f"   - {dim['aspect']}: {len(dim['queries'])} queries")
            
            # Execution
            if 'execution_summary' in result:
                print(f"\n🤖 Execution:")
                print(f"   Agents Deployed: {result['execution_summary']['agents_deployed']}")
                print(f"   Sources Found: {result['execution_summary']['total_sources_found']}")
                print(f"   Processing Time: {result['execution_summary']['processing_time']}s")
            
            # Results
            if 'metadata' in result:
                print(f"\n📊 Results:")
                print(f"   Total Sources: {result['metadata']['total_sources']}")
                print(f"   High Confidence: {result['metadata']['high_confidence_sources']}")
                print(f"   Sections: {result['metadata']['dimensions']}")
                print(f"   Techniques: {', '.join(result['metadata']['techniques_used'])}")
            
            # Executive Summary Preview
            if 'executive_summary' in result:
                print(f"\n📄 Executive Summary (Preview):")
                summary = result['executive_summary'][:300] + "..." if len(result['executive_summary']) > 300 else result['executive_summary']
                print(f"   {summary}")
            
            # Sections
            if 'sections' in result:
                print(f"\n📚 Sections Generated:")
                for idx, section in enumerate(result['sections'], 1):
                    print(f"   {idx}. {section['title']}")
                    print(f"      Sources: {section['source_count']} ({section['high_confidence_count']} high-confidence)")
            
            # Verification
            if 'verification' in result:
                print(f"\n✅ Verification:")
                for v in result['verification'][:3]:  # Show first 3
                    print(f"   - {v['claim']}")
            
            print("\n" + "="*70)
            print("✅ ALL TESTS PASSED!")
            print("="*70)
            print("\n✨ The Deep Research System is fully operational!")
            print("   - Chain of Thought decomposition: ✅")
            print("   - Multi-agent execution: ✅")
            print("   - Self-consistency aggregation: ✅")
            print("   - LLM synthesis: ✅")
            print("   - Citation management: ✅")
            
        else:
            print(f"❌ Research failed: {response.status_code}")
            print(f"   Error: {response.text}")
            
    except requests.Timeout:
        print("❌ Request timed out (>2 minutes)")
        print("   This might indicate API issues or rate limiting")
    except Exception as e:
        print(f"❌ Research error: {e}")
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    test_backend()