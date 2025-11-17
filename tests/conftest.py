"""
pytest configuration file for Heinrich TRIZ Engine tests.
"""
import sys
import pytest
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

@pytest.fixture
def sample_problem_text():
    """Sample problem text for testing."""
    return "We need to make a car faster, but increasing engine power makes it consume more fuel."

@pytest.fixture
def sample_technical_contradiction():
    """Sample technical contradiction for testing."""
    return {
        "improving_parameter": "Speed",
        "worsening_parameter": "Energy consumption",
        "improving_index": 9,
        "worsening_index": 19
    }

@pytest.fixture
def sample_parsed_problem():
    """Sample parsed problem object for testing."""
    from heinrich.pipelines.problem_parser import ParsedProblem
    return ParsedProblem(
        technical_system="car",
        desired_improvement="faster",
        undesired_consequence="increasing engine power makes it consume more fuel",
        constraints=[],
        context={"domain": "automotive"}
    )
