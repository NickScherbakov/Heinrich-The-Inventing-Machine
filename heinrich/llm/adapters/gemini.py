"""
Google Gemini LLM Adapter
Adapter for Google's Gemini models via Vertex AI / Google AI Studio.

Author: Copilot powered by Claude Opus
"""
from typing import Dict, Any, List, Optional
from heinrich.llm.base_adapter import BaseLLMAdapter, LLMResponse, Message
from heinrich.utils.logging_config import get_logger

logger = get_logger("llm.adapters.gemini")


class GeminiAdapter(BaseLLMAdapter):
    """
    Adapter for Google Gemini LLM provider.
    
    Supports both Google AI Studio (API key) and Vertex AI (service account).
    More info: https://ai.google.dev/
    
    Author: Copilot powered by Claude Opus
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the Gemini adapter.
        
        Args:
            config: Configuration dictionary with:
                - api_key: Google AI Studio API key (for direct API access)
                - project_id: GCP project ID (for Vertex AI)
                - location: GCP region (default: us-central1)
                - model: Model name (default: gemini-1.5-pro)
                - temperature: Sampling temperature
                - use_vertex: Whether to use Vertex AI (default: False)
        """
        super().__init__(config)
        
        self.api_key = config.get("api_key")
        self.project_id = config.get("project_id")
        self.location = config.get("location", "us-central1")
        self.model = config.get("model", "gemini-1.5-pro")
        self.use_vertex = config.get("use_vertex", False)
        
        self._client = None
        self._initialized = False
        
        logger.info(f"Initialized Gemini adapter with model: {self.model}")
    
    def _ensure_initialized(self) -> bool:
        """
        Lazy initialization of the Gemini client.
        
        Returns:
            True if initialization successful, False otherwise
        """
        if self._initialized:
            return True
        
        try:
            if self.use_vertex:
                # Use Vertex AI
                import vertexai
                from vertexai.generative_models import GenerativeModel
                
                vertexai.init(project=self.project_id, location=self.location)
                self._client = GenerativeModel(self.model)
                self._client_type = "vertex"
                
            else:
                # Use Google AI Studio (API key)
                import google.generativeai as genai
                
                if not self.api_key:
                    raise ValueError("API key required for Google AI Studio")
                
                genai.configure(api_key=self.api_key)
                self._client = genai.GenerativeModel(self.model)
                self._client_type = "genai"
            
            self._initialized = True
            logger.info(f"Gemini client initialized successfully ({self._client_type})")
            return True
            
        except ImportError as e:
            logger.error(
                f"Missing dependencies. Install with: "
                f"pip install google-generativeai (for AI Studio) or "
                f"pip install google-cloud-aiplatform (for Vertex AI). Error: {e}"
            )
            return False
        except Exception as e:
            logger.error(f"Failed to initialize Gemini client: {e}")
            return False
    
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ) -> LLMResponse:
        """
        Generate a response from Gemini.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            max_tokens: Maximum tokens to generate
            temperature: Temperature for sampling
            
        Returns:
            LLMResponse object
        """
        if not self._ensure_initialized():
            return LLMResponse(
                content="Error: Gemini client not initialized",
                model=self.model,
                metadata={"error": "initialization_failed"}
            )
        
        try:
            # Build the full prompt with system instruction
            full_prompt = prompt
            if system_prompt:
                full_prompt = f"{system_prompt}\n\n{prompt}"
            
            # Configure generation parameters
            generation_config = {
                "temperature": temperature or self.temperature,
            }
            if max_tokens:
                generation_config["max_output_tokens"] = max_tokens
            
            # Generate response
            response = self._client.generate_content(
                full_prompt,
                generation_config=generation_config
            )
            
            # Extract usage information if available
            usage = None
            if hasattr(response, 'usage_metadata'):
                usage = {
                    "prompt_tokens": getattr(response.usage_metadata, 'prompt_token_count', 0),
                    "completion_tokens": getattr(response.usage_metadata, 'candidates_token_count', 0),
                    "total_tokens": getattr(response.usage_metadata, 'total_token_count', 0),
                }
            
            return LLMResponse(
                content=response.text,
                model=self.model,
                usage=usage,
                metadata={
                    "provider": "google_gemini",
                    "client_type": self._client_type,
                    "finish_reason": getattr(response.candidates[0], 'finish_reason', None) if response.candidates else None
                }
            )
            
        except Exception as e:
            logger.error(f"Gemini generation failed: {e}")
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
        Have a conversation with Gemini.
        
        Args:
            messages: List of messages in the conversation
            max_tokens: Maximum tokens to generate
            temperature: Temperature for sampling
            
        Returns:
            LLMResponse object
        """
        if not self._ensure_initialized():
            return LLMResponse(
                content="Error: Gemini client not initialized",
                model=self.model,
                metadata={"error": "initialization_failed"}
            )
        
        try:
            # Extract system prompt if present
            system_prompt = None
            chat_messages = []
            
            for msg in messages:
                if msg.role == "system":
                    system_prompt = msg.content
                else:
                    chat_messages.append(msg)
            
            # Configure generation parameters
            generation_config = {
                "temperature": temperature or self.temperature,
            }
            if max_tokens:
                generation_config["max_output_tokens"] = max_tokens
            
            # Start chat with system instruction if available
            if self._client_type == "genai":
                import google.generativeai as genai
                
                # Recreate model with system instruction if needed
                if system_prompt:
                    model = genai.GenerativeModel(
                        self.model,
                        system_instruction=system_prompt
                    )
                else:
                    model = self._client
                
                # Build chat history
                history = []
                for msg in chat_messages[:-1]:  # All except last message
                    role = "user" if msg.role == "user" else "model"
                    history.append({
                        "role": role,
                        "parts": [msg.content]
                    })
                
                # Start chat and send last message
                chat = model.start_chat(history=history)
                last_message = chat_messages[-1].content if chat_messages else ""
                
                response = chat.send_message(
                    last_message,
                    generation_config=generation_config
                )
            else:
                # Vertex AI
                # Build conversation as a single prompt for simplicity
                conversation = ""
                if system_prompt:
                    conversation += f"System: {system_prompt}\n\n"
                
                for msg in chat_messages:
                    role_name = "User" if msg.role == "user" else "Assistant"
                    conversation += f"{role_name}: {msg.content}\n\n"
                
                conversation += "Assistant:"
                
                response = self._client.generate_content(
                    conversation,
                    generation_config=generation_config
                )
            
            # Extract usage information if available
            usage = None
            if hasattr(response, 'usage_metadata'):
                usage = {
                    "prompt_tokens": getattr(response.usage_metadata, 'prompt_token_count', 0),
                    "completion_tokens": getattr(response.usage_metadata, 'candidates_token_count', 0),
                    "total_tokens": getattr(response.usage_metadata, 'total_token_count', 0),
                }
            
            return LLMResponse(
                content=response.text,
                model=self.model,
                usage=usage,
                metadata={
                    "provider": "google_gemini",
                    "client_type": self._client_type,
                }
            )
            
        except Exception as e:
            logger.error(f"Gemini chat failed: {e}")
            return LLMResponse(
                content=f"Error: {str(e)}",
                model=self.model,
                metadata={"error": str(e)}
            )
    
    def count_tokens(self, text: str) -> int:
        """
        Count tokens in a text string.
        
        Args:
            text: Text to count tokens for
            
        Returns:
            Token count
        """
        if not self._ensure_initialized():
            return 0
        
        try:
            result = self._client.count_tokens(text)
            return result.total_tokens
        except Exception as e:
            logger.error(f"Token counting failed: {e}")
            return 0
    
    def list_models(self) -> List[str]:
        """
        List available Gemini models.
        
        Returns:
            List of model names
        """
        if self._client_type == "genai":
            try:
                import google.generativeai as genai
                models = genai.list_models()
                return [m.name for m in models if 'generateContent' in m.supported_generation_methods]
            except Exception as e:
                logger.error(f"Failed to list models: {e}")
                return []
        else:
            # Vertex AI - return known models
            return [
                "gemini-1.5-pro",
                "gemini-1.5-flash",
                "gemini-1.0-pro",
                "gemini-1.0-pro-vision",
            ]
