#!/usr/bin/env python3
"""
Heinrich TRIZ Engine with Google Gemini Integration

This example demonstrates how to use Heinrich with Google's Gemini LLM
for powerful TRIZ-based problem solving.

Author: Copilot powered by Claude Opus

Setup:
1. Get a Gemini API key from https://aistudio.google.com/
2. Set environment variable: export GEMINI_API_KEY="your-key"
3. Run: python examples/gemini_usage.py

For Vertex AI (GCP):
1. Set up GCP project with Vertex AI enabled
2. Configure authentication (gcloud auth application-default login)
3. Set USE_VERTEX=true and PROJECT_ID environment variables
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from heinrich.llm.adapters.gemini import GeminiAdapter
from heinrich.llm.base_adapter import Message


def main():
    """Main function demonstrating Gemini integration with Heinrich."""
    
    print("=" * 60)
    print("🚀 Heinrich TRIZ Engine + Google Gemini")
    print("=" * 60)
    print()
    
    # Configuration for Gemini
    api_key = os.environ.get("GEMINI_API_KEY")
    use_vertex = os.environ.get("USE_VERTEX", "false").lower() == "true"
    project_id = os.environ.get("PROJECT_ID")
    
    if not api_key and not use_vertex:
        print("⚠️  No API key found. Set GEMINI_API_KEY environment variable.")
        print("    Get your key at: https://aistudio.google.com/")
        print()
        print("For demo purposes, showing configuration example...")
        print()
        
        # Show configuration example
        print("Example configuration:")
        print("```python")
        print('config = {')
        print('    "api_key": "your-gemini-api-key",')
        print('    "model": "gemini-1.5-pro",')
        print('    "temperature": 0.7,')
        print('}')
        print('adapter = GeminiAdapter(config)')
        print("```")
        return
    
    # Initialize Gemini adapter
    config = {
        "api_key": api_key,
        "model": "gemini-1.5-pro",
        "temperature": 0.7,
        "use_vertex": use_vertex,
        "project_id": project_id,
    }
    
    adapter = GeminiAdapter(config)
    print(f"✅ Initialized Gemini adapter with model: {config['model']}")
    print()
    
    # TRIZ System Prompt
    triz_system_prompt = """You are Heinrich, an AI assistant specialized in TRIZ 
(Theory of Inventive Problem Solving) methodology. You help users identify 
technical and physical contradictions in their problems and suggest relevant 
TRIZ principles to resolve them.

Follow these steps:
1. Analyze the problem to identify the technical system
2. Identify contradictions (improving one parameter worsens another)
3. Map to TRIZ 39 parameters
4. Suggest applicable principles from the 40 inventive principles
5. Generate solution concepts based on the principles

Be systematic, educational, and provide reasoning for each step."""

    # Example problem
    problem = """
    We are developing a drone for package delivery. We need the drone to carry 
    heavier packages, but increasing payload capacity requires larger batteries 
    which make the drone heavier and reduce flight time.
    """
    
    print("📋 Problem:")
    print("-" * 40)
    print(problem.strip())
    print("-" * 40)
    print()
    
    # Generate TRIZ analysis
    print("🔍 Generating TRIZ Analysis with Gemini...")
    print()
    
    prompt = f"""Analyze the following problem using TRIZ methodology:

{problem}

Provide:
1. Technical System identification
2. Technical Contradiction (Parameter to improve vs Parameter that worsens)
3. Physical Contradiction (if any)
4. Recommended TRIZ Principles (from the 40 principles)
5. Solution Concepts for each principle

Format your response clearly with numbered sections."""

    response = adapter.generate(
        prompt=prompt,
        system_prompt=triz_system_prompt,
        max_tokens=2000,
        temperature=0.7
    )
    
    if "Error" in response.content:
        print(f"❌ {response.content}")
        return
    
    print("📊 TRIZ Analysis Results:")
    print("=" * 60)
    print(response.content)
    print("=" * 60)
    print()
    
    # Show usage statistics
    if response.usage:
        print("📈 Token Usage:")
        print(f"   Prompt tokens: {response.usage.get('prompt_tokens', 'N/A')}")
        print(f"   Completion tokens: {response.usage.get('completion_tokens', 'N/A')}")
        print(f"   Total tokens: {response.usage.get('total_tokens', 'N/A')}")
    
    print()
    print("✨ Analysis complete!")
    print()
    print("Powered by: Heinrich TRIZ Engine + Google Gemini")
    print("Author: Copilot powered by Claude Opus")


def demo_chat_mode():
    """Demonstrate interactive chat mode with Gemini."""
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Set GEMINI_API_KEY to use chat mode")
        return
    
    config = {
        "api_key": api_key,
        "model": "gemini-1.5-flash",  # Faster model for chat
        "temperature": 0.7,
    }
    
    adapter = GeminiAdapter(config)
    
    messages = [
        Message(role="system", content="You are Heinrich, a TRIZ methodology expert."),
        Message(role="user", content="What are the 40 inventive principles in TRIZ?"),
    ]
    
    response = adapter.chat(messages, max_tokens=1000)
    print(response.content)


if __name__ == "__main__":
    main()
