"""
Heinrich Pipeline Modules
Core TRIZ processing pipeline components.
"""

from heinrich.pipelines.problem_parser import ProblemParser, ParsedProblem
from heinrich.pipelines.contradiction_identifier import ContradictionIdentifier, ContradictionResult
from heinrich.pipelines.principle_selector import PrincipleSelector, PrincipleSelectionResult
from heinrich.pipelines.effects_lookup import EffectsLookup, EffectRecommendation
from heinrich.pipelines.concept_generator import ConceptGenerator, ConceptGenerationResult
from heinrich.pipelines.adaptation_planner import AdaptationPlanner, AdaptationContext, AdaptationResult
from heinrich.pipelines.report_builder import ReportBuilder, TRIZReport

__all__ = [
    "ProblemParser",
    "ParsedProblem",
    "ContradictionIdentifier",
    "ContradictionResult",
    "PrincipleSelector",
    "PrincipleSelectionResult",
    "EffectsLookup",
    "EffectRecommendation",
    "ConceptGenerator",
    "ConceptGenerationResult",
    "AdaptationPlanner",
    "AdaptationContext",
    "AdaptationResult",
    "ReportBuilder",
    "TRIZReport"
]
