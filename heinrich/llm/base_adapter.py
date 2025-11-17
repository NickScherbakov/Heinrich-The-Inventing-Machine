"""
Base LLM Adapter Interface
Defines the interface that all LLM adapters must implement.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class LLMResponse:
    """Response from an LLM."""
    content: str
    model: str
    usage: Optional[Dict[str, int]] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class Message:
    """Message in a conversation."""
    role: str  # "system", "user", "assistant"
    content: str


class BaseLLMAdapter(ABC):
    """
    Base class for LLM adapters.
    
    All LLM provider adapters (OpenAI, Anthropic, Ollama, etc.)
    must inherit from this class and implement its methods.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the LLM adapter.
        
        Args:
            config: Configuration dictionary for the LLM
        """
        self.config = config
        self.model = config.get("model", "default")
        self.temperature = config.get("temperature", 0.7)
    
    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ) -> LLMResponse:
        """
        Generate a response from the LLM.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            max_tokens: Maximum tokens to generate
            temperature: Temperature for sampling
            
        Returns:
            LLMResponse object
        """
        pass
    
    @abstractmethod
    def chat(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ) -> LLMResponse:
        """
        Have a conversation with the LLM.
        
        Args:
            messages: List of messages in the conversation
            max_tokens: Maximum tokens to generate
            temperature: Temperature for sampling
            
        Returns:
            LLMResponse object
        """
        pass
    
    def format_triz_prompt(
        self,
        step_name: str,
        context: Dict[str, Any],
        template: str
    ) -> str:
        """
        Format a TRIZ-specific prompt.
        
        Args:
            step_name: Name of the TRIZ step
            context: Context data for the prompt
            template: Prompt template string
            
        Returns:
            Formatted prompt
        """
        return template.format(**context)
