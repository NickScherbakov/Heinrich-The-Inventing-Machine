"""
Unit tests for LLM adapters.
"""
import pytest
from heinrich.llm.base_adapter import BaseLLMAdapter, LLMResponse, Message
from heinrich.llm.adapters.ollama import OllamaAdapter


class TestBaseLLMAdapter:
    """Test cases for BaseLLMAdapter."""

    def test_base_adapter_is_abstract(self):
        """Test that BaseLLMAdapter cannot be instantiated directly."""
        with pytest.raises(TypeError):
            BaseLLMAdapter({})


class TestOllamaAdapter:
    """Test cases for OllamaAdapter."""

    def test_ollama_adapter_initialization(self):
        """Test that OllamaAdapter initializes correctly."""
        config = {
            "model": "llama2",
            "base_url": "http://localhost:11434",
            "temperature": 0.7
        }
        adapter = OllamaAdapter(config)
        
        assert adapter is not None
        assert adapter.model == "llama2"
        assert adapter.temperature == 0.7
        assert adapter.base_url == "http://localhost:11434"

    def test_ollama_adapter_default_config(self):
        """Test OllamaAdapter with minimal configuration."""
        config = {"model": "llama2"}
        adapter = OllamaAdapter(config)
        
        assert adapter.base_url == "http://localhost:11434"
        assert adapter.temperature == 0.7

    def test_message_creation(self):
        """Test creating Message objects."""
        msg = Message(role="user", content="Hello")
        
        assert msg.role == "user"
        assert msg.content == "Hello"

    def test_llm_response_creation(self):
        """Test creating LLMResponse objects."""
        response = LLMResponse(
            content="Test response",
            model="llama2",
            usage={"prompt_tokens": 10, "completion_tokens": 20}
        )
        
        assert response.content == "Test response"
        assert response.model == "llama2"
        assert response.usage["prompt_tokens"] == 10
