"""
Heinrich LLM Integration
LLM adapters and prompt templates for TRIZ analysis.
"""

from heinrich.llm.base_adapter import BaseLLMAdapter
from heinrich.llm.adapters.ollama import OllamaAdapter

__all__ = [
    "BaseLLMAdapter",
    "OllamaAdapter"
]
