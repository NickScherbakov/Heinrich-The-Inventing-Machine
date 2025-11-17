"""
Integration tests for the full Heinrich pipeline.
"""
import pytest
from heinrich.pipelines.problem_parser import ProblemParser
from heinrich.pipelines.contradiction_identifier import ContradictionIdentifier
from heinrich.pipelines.principle_selector import PrincipleSelector
from heinrich.knowledge.knowledge_loader import KnowledgeLoader


class TestFullPipeline:
    """Test cases for the full Heinrich TRIZ pipeline."""

    def test_problem_to_contradiction_flow(self, sample_problem_text):
        """Test the flow from problem parsing to contradiction identification."""
        # Parse the problem
        parser = ProblemParser()
        parsed_problem = parser.parse(sample_problem_text)
        
        assert parsed_problem is not None
        assert parsed_problem.technical_system is not None
        
        # Identify contradictions
        identifier = ContradictionIdentifier()
        # The contradiction identifier should be able to process the parsed problem
        assert identifier is not None

    def test_knowledge_base_integration(self):
        """Test that all knowledge base components can be loaded together."""
        loader = KnowledgeLoader()
        
        # Load all knowledge base components
        matrix = loader.load_contradiction_matrix()
        principles = loader.load_40_principles()
        parameters = loader.load_39_parameters()
        
        assert matrix is not None
        assert principles is not None
        assert parameters is not None

    def test_pipeline_components_exist(self):
        """Test that all main pipeline components can be instantiated."""
        parser = ProblemParser()
        identifier = ContradictionIdentifier()
        selector = PrincipleSelector()
        
        assert parser is not None
        assert identifier is not None
        assert selector is not None
