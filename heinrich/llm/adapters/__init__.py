"""
LLM Adapters Package

Supported providers:
- Ollama: Local LLM models
- Gemini: Google's Gemini models (AI Studio & Vertex AI)

Author: Copilot powered by Claude Opus
"""

from heinrich.llm.adapters.ollama import OllamaAdapter
from heinrich.llm.adapters.gemini import GeminiAdapter

__all__ = ["OllamaAdapter", "GeminiAdapter"]
