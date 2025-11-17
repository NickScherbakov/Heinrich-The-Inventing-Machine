"""
Unit tests for the PersonaManager module.
"""
import pytest
from heinrich.agents.persona_manager import PersonaManager


class TestPersonaManager:
    """Test cases for PersonaManager."""

    def test_persona_manager_initialization(self):
        """Test that PersonaManager initializes correctly."""
        manager = PersonaManager()
        assert manager is not None

    def test_persona_manager_has_persona(self):
        """Test that PersonaManager has a persona defined."""
        manager = PersonaManager()
        # Should have some persona-related attributes or methods
        assert hasattr(manager, 'get_persona') or hasattr(manager, 'persona')
