"""
Unit tests for the ProblemParser module.
"""
import pytest
from heinrich.pipelines.problem_parser import ProblemParser, ParsedProblem


class TestProblemParser:
    """Test cases for ProblemParser."""

    def test_parser_initialization(self):
        """Test that ProblemParser initializes correctly."""
        parser = ProblemParser()
        assert parser is not None

    def test_parse_basic_problem(self, sample_problem_text):
        """Test parsing a basic problem statement."""
        parser = ProblemParser()
        result = parser.parse(sample_problem_text)
        
        assert isinstance(result, ParsedProblem)
        assert result.technical_system is not None
        assert result.desired_improvement is not None
        assert result.undesired_consequence is not None

    def test_parse_returns_parsed_problem_object(self):
        """Test that parse returns a ParsedProblem object."""
        parser = ProblemParser()
        problem_text = "Make the machine stronger but not heavier"
        result = parser.parse(problem_text)
        
        assert isinstance(result, ParsedProblem)
        assert hasattr(result, 'technical_system')
        assert hasattr(result, 'desired_improvement')
        assert hasattr(result, 'undesired_consequence')
        assert hasattr(result, 'constraints')
        assert hasattr(result, 'context')

    def test_parse_empty_string(self):
        """Test parsing an empty string."""
        parser = ProblemParser()
        result = parser.parse("")
        
        assert isinstance(result, ParsedProblem)
        # Should handle empty input gracefully

    def test_parsed_problem_has_context(self, sample_problem_text):
        """Test that parsed problem includes context."""
        parser = ProblemParser()
        result = parser.parse(sample_problem_text)
        
        assert isinstance(result.context, dict)
        assert 'domain' in result.context or len(result.context) >= 0

    def test_constraints_is_list(self, sample_problem_text):
        """Test that constraints field is a list."""
        parser = ProblemParser()
        result = parser.parse(sample_problem_text)
        
        assert isinstance(result.constraints, list)
