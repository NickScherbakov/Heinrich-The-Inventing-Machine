"""
Ollama LLM Adapter
Adapter for local LLM models via Ollama.
"""
from typing import Dict, Any, List, Optional
import json
from heinrich.llm.base_adapter import BaseLLMAdapter, LLMResponse, Message
from heinrich.utils.logging_config import get_logger

logger = get_logger("llm.adapters.ollama")


class OllamaAdapter(BaseLLMAdapter):
    """
    Adapter for Ollama local LLM provider.
    
    Ollama allows running large language models locally.
    More info: https://ollama.ai/
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the Ollama adapter.
        
        Args:
            config: Configuration dictionary with:
                - base_url: Ollama API base URL (default: http://localhost:11434)
                - model: Model name (e.g., "llama2", "mistral")
                - temperature: Sampling temperature
        """
        super().__init__(config)
        self.base_url = config.get("base_url", "http://localhost:11434")
        self.api_url = f"{self.base_url}/api"
        
        logger.info(f"Initialized Ollama adapter with model: {self.model}")
    
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ) -> LLMResponse:
        """
        Generate a response from Ollama.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            max_tokens: Maximum tokens to generate
            temperature: Temperature for sampling
            
        Returns:
            LLMResponse object
        """
        try:
            import requests
        except ImportError:
            logger.error("requests library not installed. Install with: pip install requests")
            return LLMResponse(
                content="Error: requests library not installed",
                model=self.model,
                metadata={"error": "missing_dependency"}
            )
        
        url = f"{self.api_url}/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature or self.temperature,
            }
        }
        
        if system_prompt:
            payload["system"] = system_prompt
        
        if max_tokens:
            payload["options"]["num_predict"] = max_tokens
        
        try:
            response = requests.post(url, json=payload, timeout=60)
            response.raise_for_status()
            
            result = response.json()
            
            return LLMResponse(
                content=result.get("response", ""),
                model=self.model,
                usage={
                    "prompt_tokens": result.get("prompt_eval_count", 0),
                    "completion_tokens": result.get("eval_count", 0),
                },
                metadata=result
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"Ollama API request failed: {e}")
            return LLMResponse(
                content=f"Error: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )
    
    def chat(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ) -> LLMResponse:
        """
        Have a conversation with Ollama.
        
        Args:
            messages: List of messages in the conversation
            max_tokens: Maximum tokens to generate
            temperature: Temperature for sampling
            
        Returns:
            LLMResponse object
        """
        try:
            import requests
        except ImportError:
            logger.error("requests library not installed")
            return LLMResponse(
                content="Error: requests library not installed",
                model=self.model,
                metadata={"error": "missing_dependency"}
            )
        
        url = f"{self.api_url}/chat"
        
        payload = {
            "model": self.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "stream": False,
            "options": {
                "temperature": temperature or self.temperature,
            }
        }
        
        if max_tokens:
            payload["options"]["num_predict"] = max_tokens
        
        try:
            response = requests.post(url, json=payload, timeout=60)
            response.raise_for_status()
            
            result = response.json()
            message = result.get("message", {})
            
            return LLMResponse(
                content=message.get("content", ""),
                model=self.model,
                usage={
                    "prompt_tokens": result.get("prompt_eval_count", 0),
                    "completion_tokens": result.get("eval_count", 0),
                },
                metadata=result
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"Ollama chat API request failed: {e}")
            return LLMResponse(
                content=f"Error: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )
