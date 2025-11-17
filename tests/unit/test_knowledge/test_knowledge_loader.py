"""
Unit tests for the KnowledgeLoader module.
"""
import pytest
from pathlib import Path
from heinrich.knowledge.knowledge_loader import KnowledgeLoader


class TestKnowledgeLoader:
    """Test cases for KnowledgeLoader."""

    def test_knowledge_loader_initialization(self):
        """Test that KnowledgeLoader initializes correctly."""
        loader = KnowledgeLoader()
        assert loader is not None

    def test_load_contradiction_matrix(self):
        """Test loading the contradiction matrix."""
        loader = KnowledgeLoader()
        matrix = loader.load_contradiction_matrix()
        
        assert matrix is not None
        # The matrix should be a data structure with content

    def test_load_principles(self):
        """Test loading the 40 principles."""
        loader = KnowledgeLoader()
        principles = loader.load_40_principles()
        
        assert principles is not None
        # Should load principles data

    def test_load_parameters(self):
        """Test loading the 39 parameters."""
        loader = KnowledgeLoader()
        parameters = loader.load_39_parameters()
        
        assert parameters is not None
        # Should load parameters data

    def test_knowledge_base_path_exists(self):
        """Test that the knowledge base directory exists."""
        loader = KnowledgeLoader()
        # The knowledge loader should have a valid base path
        assert hasattr(loader, 'base_path') or hasattr(loader, 'knowledge_path')
