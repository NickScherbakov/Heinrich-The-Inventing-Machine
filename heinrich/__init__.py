"""
Heinrich: The Inventing Machine - Main Package
Open-source AI system for TRIZ-based inventive problem solving.
"""

from heinrich.version import __version__, __author__, __description__

__all__ = [
    "__version__",
    "__author__",
    "__description__"
]

# Import key classes for easy access
try:
    from heinrich.pipelines.problem_parser import ProblemParser
    from heinrich.pipelines.contradiction_identifier import ContradictionIdentifier
    from heinrich.pipelines.principle_selector import PrincipleSelector
    from heinrich.pipelines.concept_generator import ConceptGenerator
    from heinrich.agents.persona_manager import PersonaManager

    __all__.extend([
        "ProblemParser",
        "ContradictionIdentifier",
        "PrincipleSelector",
        "ConceptGenerator",
        "PersonaManager"
    ])
except ImportError:
    # Handle case where dependencies aren't installed yet
    pass
