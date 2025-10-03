"""
Heinrich TRIZ Engine - Principle Selector Module
Selects relevant TRIZ principles using the contradiction matrix.
"""

import yaml
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class PrincipleRecommendation:
    """Represents a recommended TRIZ principle for solving a contradiction."""

    principle_id: int
    principle_name: str
    principle_description: str
    relevance_score: float
    reasoning: str
    examples: List[str]

@dataclass
class PrincipleSelectionResult:
    """Result of principle selection process."""

    recommendations: List[PrincipleRecommendation]
    primary_principles: List[PrincipleRecommendation]
    supporting_principles: List[PrincipleRecommendation]
    matrix_source: str

class PrincipleSelector:
    """Selects TRIZ principles based on identified contradictions using the contradiction matrix."""

    def __init__(self,
                 principles_file: str = "heinrich/knowledge/40_principles.yaml",
                 matrix_file: str = "heinrich/knowledge/contradiction_matrix.csv"):
        """Initialize with TRIZ principles and contradiction matrix."""
        # Load 40 principles
        with open(principles_file, 'r', encoding='utf-8') as f:
            self.principles_data = yaml.safe_load(f)

        self.principles = {p['id']: p for p in self.principles_data['principles']}

        # Load contradiction matrix (simplified version for now)
        self.contradiction_matrix = self._load_contradiction_matrix(matrix_file)

    def _load_contradiction_matrix(self, matrix_file: str) -> Dict[Tuple[int, int], List[int]]:
        """Load the 39x39 contradiction matrix."""
        matrix = {}

        # For now, create a simplified matrix with some known relationships
        # In a full implementation, this would load from a CSV file

        # Some well-known contradiction relationships
        known_relationships = [
            # Speed vs Energy consumption (common automotive contradiction)
            ((9, 19), [15, 2, 35, 18]),  # Speed vs Energy consumption

            # Weight vs Strength
            ((1, 14), [1, 8, 15, 40]),   # Weight vs Strength

            # Speed vs Accuracy
            ((9, 28), [28, 32, 35, 13]), # Speed vs Accuracy

            # Complexity vs Reliability
            ((36, 27), [1, 13, 22, 35]), # Complexity vs Reliability

            # Cost vs Quality/Productivity
            ((39, 27), [2, 25, 35, 13]), # Productivity vs Reliability

            # Size vs Strength
            ((3, 14), [1, 8, 14, 15]),   # Length vs Strength
        ]

        for (param1, param2), principles in known_relationships:
            # Matrix is symmetric
            matrix[(param1, param2)] = principles
            matrix[(param2, param1)] = principles

        return matrix

    def select_principles(self, improving_param: int, worsening_param: int) -> PrincipleSelectionResult:
        """
        Select TRIZ principles for a specific contradiction.

        Args:
            improving_param: ID of parameter to improve
            worsening_param: ID of parameter that worsens

        Returns:
            PrincipleSelectionResult with recommended principles
        """
        matrix_key = (improving_param, worsening_param)

        if matrix_key in self.contradiction_matrix:
            principle_ids = self.contradiction_matrix[matrix_key]
        else:
            # No direct mapping found, use heuristic approach
            principle_ids = self._heuristic_principle_selection(improving_param, worsening_param)

        # Create recommendations for each principle
        recommendations = []
        for principle_id in principle_ids:
            if principle_id in self.principles:
                principle_data = self.principles[principle_id]

                # Calculate relevance score based on how well this principle fits
                relevance_score = self._calculate_relevance_score(
                    principle_id, improving_param, worsening_param
                )

                recommendation = PrincipleRecommendation(
                    principle_id=principle_id,
                    principle_name=principle_data['name'],
                    principle_description=principle_data['description'],
                    relevance_score=relevance_score,
                    reasoning=self._generate_reasoning(principle_id, improving_param, worsening_param),
                    examples=principle_data.get('examples', [])[:3]  # Limit examples
                )
                recommendations.append(recommendation)

        # Sort by relevance score
        recommendations.sort(key=lambda x: x.relevance_score, reverse=True)

        # Split into primary and supporting principles
        primary_threshold = 0.7
        primary_principles = [r for r in recommendations if r.relevance_score >= primary_threshold]
        supporting_principles = [r for r in recommendations if r.relevance_score < primary_threshold]

        return PrincipleSelectionResult(
            recommendations=recommendations,
            primary_principles=primary_principles,
            supporting_principles=supporting_principles,
            matrix_source="contradiction_matrix" if matrix_key in self.contradiction_matrix else "heuristic"
        )

    def _heuristic_principle_selection(self, improving_param: int, worsening_param: int) -> List[int]:
        """Use heuristic rules when direct matrix lookup fails."""
        # Simple heuristic based on parameter types

        # Physical contradictions often benefit from separation principles
        if self._is_physical_contradiction(improving_param, worsening_param):
            return [1, 2, 3, 7]  # Segmentation, Taking out, Local quality, Nested doll

        # Technical contradictions often benefit from dynamics and adaptation
        elif self._is_technical_contradiction(improving_param, worsening_param):
            return [15, 35, 36, 16]  # Dynamics, Parameter changes, Phase transitions, Partial action

        # Default fallback principles
        return [13, 1, 8, 15]  # The other way round, Segmentation, Anti-weight, Dynamics

    def _is_physical_contradiction(self, param1: int, param2: int) -> bool:
        """Check if this represents a physical contradiction."""
        # Physical contradictions occur when the same parameter needs opposite states
        physical_params = {1, 2, 3, 4, 5, 6, 7, 8, 9, 17}  # Weight, length, area, volume, speed, temperature
        return param1 in physical_params and param2 in physical_params

    def _is_technical_contradiction(self, param1: int, param2: int) -> bool:
        """Check if this represents a technical contradiction."""
        # Technical contradictions occur between different parameters
        return not self._is_physical_contradiction(param1, param2)

    def _calculate_relevance_score(self, principle_id: int, improving_param: int, worsening_param: int) -> float:
        """Calculate how relevant a principle is for this contradiction."""
        # Base score from matrix (0.8 if direct match, 0.4 if heuristic)
        base_score = 0.8 if (improving_param, worsening_param) in self.contradiction_matrix else 0.4

        # Adjust based on principle characteristics
        principle_data = self.principles[principle_id]

        # Some principles are more universally applicable
        universal_principles = {1, 8, 13, 15, 35}  # Segmentation, Anti-weight, The other way round, Dynamics, Parameter changes
        if principle_id in universal_principles:
            base_score += 0.1

        # Parameter-specific adjustments
        if improving_param == 9 and principle_id in {15, 18, 28}:  # Speed improvements
            base_score += 0.15

        return min(base_score, 1.0)  # Cap at 1.0

    def _generate_reasoning(self, principle_id: int, improving_param: int, worsening_param: int) -> str:
        """Generate reasoning for why this principle is recommended."""
        principle_data = self.principles[principle_id]

        improving_name = next(p['name'] for p in self.parameters_data['parameters'] if p['id'] == improving_param)
        worsening_name = next(p['name'] for p in self.parameters_data['parameters'] if p['id'] == worsening_param)

        reasoning = f"Principle {principle_id} '{principle_data['name']}' is recommended "
        reasoning += f"to resolve the contradiction between improving '{improving_name}' "
        reasoning += f"and avoiding degradation of '{worsening_name}'. "

        if principle_id == 15:  # Dynamics
            reasoning += "This principle suggests making the system or its parameters dynamic to achieve the desired improvement without compromising other aspects."
        elif principle_id == 1:  # Segmentation
            reasoning += "This principle suggests dividing the system into independent parts that can be optimized separately."
        elif principle_id == 2:  # Taking out
            reasoning += "This principle suggests separating the conflicting properties in space, time, or condition."

        return reasoning

    def get_principle_info(self, principle_id: int) -> Optional[Dict]:
        """Get detailed information about a specific principle."""
        return self.principles.get(principle_id)

    def list_all_principles(self) -> List[Dict]:
        """Get list of all 40 TRIZ principles."""
        return list(self.principles.values())

    def select_principles_for_contradictions(self, contradictions: List[Dict]) -> List[PrincipleSelectionResult]:
        """
        Select principles for multiple contradictions.

        Args:
            contradictions: List of contradiction dictionaries with 'improving' and 'worsening' keys

        Returns:
            List of PrincipleSelectionResult objects
        """
        results = []
        for contradiction in contradictions:
            result = self.select_principles(
                contradiction['improving_parameter'],
                contradiction['worsening_parameter']
            )
            results.append(result)

        return results
