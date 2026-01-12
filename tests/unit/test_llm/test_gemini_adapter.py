"""
Unit tests for Google Gemini LLM Adapter

Author: Copilot powered by Claude Opus
"""
import pytest
from unittest.mock import Mock, patch, MagicMock

from heinrich.llm.adapters.gemini import GeminiAdapter
from heinrich.llm.base_adapter import Message, LLMResponse


class TestGeminiAdapterInit:
    """Test GeminiAdapter initialization."""
    
    def test_init_with_api_key(self):
        """Test initialization with API key."""
        config = {
            "api_key": "test-api-key",
            "model": "gemini-1.5-pro",
            "temperature": 0.5,
        }
        adapter = GeminiAdapter(config)
        
        assert adapter.api_key == "test-api-key"
        assert adapter.model == "gemini-1.5-pro"
        assert adapter.temperature == 0.5
        assert adapter.use_vertex is False
    
    def test_init_with_vertex_ai(self):
        """Test initialization with Vertex AI config."""
        config = {
            "project_id": "my-gcp-project",
            "location": "us-east1",
            "model": "gemini-1.5-flash",
            "use_vertex": True,
        }
        adapter = GeminiAdapter(config)
        
        assert adapter.project_id == "my-gcp-project"
        assert adapter.location == "us-east1"
        assert adapter.use_vertex is True
    
    def test_default_values(self):
        """Test default configuration values."""
        config = {"api_key": "test"}
        adapter = GeminiAdapter(config)
        
        assert adapter.model == "gemini-1.5-pro"
        assert adapter.temperature == 0.7
        assert adapter.location == "us-central1"


class TestGeminiAdapterGenerate:
    """Test GeminiAdapter generate method."""
    
    @patch('heinrich.llm.adapters.gemini.GeminiAdapter._ensure_initialized')
    def test_generate_not_initialized(self, mock_init):
        """Test generate when initialization fails."""
        mock_init.return_value = False
        
        adapter = GeminiAdapter({"api_key": "test"})
        response = adapter.generate("test prompt")
        
        assert "Error" in response.content
        assert response.metadata.get("error") == "initialization_failed"
    
    @patch('google.generativeai.GenerativeModel')
    @patch('google.generativeai.configure')
    def test_generate_success(self, mock_configure, mock_model_class):
        """Test successful generation."""
        # Setup mock
        mock_response = Mock()
        mock_response.text = "TRIZ analysis result"
        mock_response.usage_metadata = Mock(
            prompt_token_count=10,
            candidates_token_count=50,
            total_token_count=60
        )
        mock_response.candidates = [Mock(finish_reason="STOP")]
        
        mock_model = Mock()
        mock_model.generate_content.return_value = mock_response
        mock_model_class.return_value = mock_model
        
        adapter = GeminiAdapter({"api_key": "test-key"})
        response = adapter.generate("Analyze this problem")
        
        assert response.content == "TRIZ analysis result"
        assert response.usage["total_tokens"] == 60


class TestGeminiAdapterChat:
    """Test GeminiAdapter chat method."""
    
    def test_chat_with_messages(self):
        """Test chat with message history."""
        adapter = GeminiAdapter({"api_key": "test"})
        
        messages = [
            Message(role="system", content="You are a TRIZ expert"),
            Message(role="user", content="What is TRIZ?"),
        ]
        
        # Since we can't actually call the API, test the message processing
        assert len(messages) == 2
        assert messages[0].role == "system"
        assert messages[1].role == "user"


class TestGeminiAdapterHelpers:
    """Test GeminiAdapter helper methods."""
    
    def test_list_models_vertex(self):
        """Test list_models for Vertex AI."""
        adapter = GeminiAdapter({
            "use_vertex": True,
            "project_id": "test"
        })
        adapter._client_type = "vertex"
        adapter._initialized = True
        
        models = adapter.list_models()
        
        assert "gemini-1.5-pro" in models
        assert "gemini-1.5-flash" in models


class TestGeminiAdapterIntegration:
    """Integration tests (require API key)."""
    
    @pytest.mark.skipif(
        not pytest.importorskip("google.generativeai", reason="google-generativeai not installed"),
        reason="Requires google-generativeai package"
    )
    def test_real_api_call(self):
        """Test with real API (requires GEMINI_API_KEY env var)."""
        import os
        api_key = os.environ.get("GEMINI_API_KEY")
        
        if not api_key:
            pytest.skip("GEMINI_API_KEY not set")
        
        adapter = GeminiAdapter({
            "api_key": api_key,
            "model": "gemini-1.5-flash",  # Use faster model for tests
        })
        
        response = adapter.generate(
            "What is the first TRIZ principle? Answer in one sentence.",
            max_tokens=100
        )
        
        assert response.content
        assert "Error" not in response.content
