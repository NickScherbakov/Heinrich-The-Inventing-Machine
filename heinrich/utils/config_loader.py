"""
Configuration loader for Heinrich TRIZ Engine.
Handles loading configuration from environment variables and files.
"""
import os
from pathlib import Path
from typing import Any, Dict, Optional
import yaml


class ConfigLoader:
    """
    Load and manage configuration for Heinrich.
    
    Supports loading from:
    - Environment variables
    - YAML configuration files
    - Default values
    """
    
    def __init__(self, config_file: Optional[Path] = None):
        """
        Initialize the configuration loader.
        
        Args:
            config_file: Optional path to YAML configuration file
        """
        self.config: Dict[str, Any] = {}
        self.config_file = config_file
        
        # Load configuration in order of precedence
        self._load_defaults()
        if config_file and config_file.exists():
            self._load_from_file(config_file)
        self._load_from_env()
    
    def _load_defaults(self) -> None:
        """Load default configuration values."""
        self.config = {
            "llm_provider": "ollama",
            "log_level": "INFO",
            "output_format": "markdown",
            "interactive_mode": True,
            "language": "en",
            "enable_cache": True,
            "cache_ttl": 3600,
            "max_concurrent_requests": 10,
            "request_timeout": 60,
            "debug": False,
        }
    
    def _load_from_file(self, config_file: Path) -> None:
        """
        Load configuration from YAML file.
        
        Args:
            config_file: Path to YAML configuration file
        """
        with open(config_file, 'r', encoding='utf-8') as f:
            file_config = yaml.safe_load(f)
            if file_config:
                self.config.update(file_config)
    
    def _load_from_env(self) -> None:
        """Load configuration from environment variables."""
        env_mappings = {
            "LLM_PROVIDER": "llm_provider",
            "LOG_LEVEL": "log_level",
            "OUTPUT_FORMAT": "output_format",
            "INTERACTIVE_MODE": "interactive_mode",
            "LANGUAGE": "language",
            "ENABLE_CACHE": "enable_cache",
            "CACHE_TTL": "cache_ttl",
            "MAX_CONCURRENT_REQUESTS": "max_concurrent_requests",
            "REQUEST_TIMEOUT": "request_timeout",
            "DEBUG": "debug",
            "OPENAI_API_KEY": "openai_api_key",
            "ANTHROPIC_API_KEY": "anthropic_api_key",
            "OLLAMA_BASE_URL": "ollama_base_url",
            "OLLAMA_MODEL": "ollama_model",
        }
        
        for env_var, config_key in env_mappings.items():
            value = os.getenv(env_var)
            if value is not None:
                # Convert string booleans
                if value.lower() in ('true', 'false'):
                    value = value.lower() == 'true'
                # Convert numeric values
                elif value.isdigit():
                    value = int(value)
                
                self.config[config_key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self.config[key] = value
    
    def get_llm_config(self) -> Dict[str, Any]:
        """
        Get LLM-specific configuration.
        
        Returns:
            Dictionary with LLM configuration
        """
        provider = self.get("llm_provider", "ollama")
        
        if provider == "openai":
            return {
                "provider": "openai",
                "api_key": self.get("openai_api_key"),
                "model": self.get("openai_model", "gpt-4"),
                "temperature": self.get("openai_temperature", 0.7),
                "max_tokens": self.get("openai_max_tokens", 2000),
            }
        elif provider == "anthropic":
            return {
                "provider": "anthropic",
                "api_key": self.get("anthropic_api_key"),
                "model": self.get("anthropic_model", "claude-3-opus-20240229"),
                "temperature": self.get("anthropic_temperature", 0.7),
                "max_tokens": self.get("anthropic_max_tokens", 2000),
            }
        elif provider == "ollama":
            return {
                "provider": "ollama",
                "base_url": self.get("ollama_base_url", "http://localhost:11434"),
                "model": self.get("ollama_model", "llama2"),
                "temperature": self.get("ollama_temperature", 0.7),
            }
        else:
            raise ValueError(f"Unknown LLM provider: {provider}")
    
    def __repr__(self) -> str:
        """String representation of the configuration."""
        return f"ConfigLoader(config_file={self.config_file})"
