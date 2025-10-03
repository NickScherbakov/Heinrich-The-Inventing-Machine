
"""
Heinrich TRIZ Engine - Problem Parser Module
Extracts and normalizes problem descriptions for TRIZ analysis.
"""

import re
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class ParsedProblem:
    """Structured representation of a parsed problem."""

    original_text: str
    normalized_description: str
    technical_system: Optional[str]
    desired_improvement: Optional[str] 
    undesired_consequence: Optional[str]
    constraints: List[str]
    context: Dict[str, str]


class ProblemParser:
    """Parses and normalizes problem descriptions for TRIZ analysis."""

    def __init__(self):
        self.improvement_keywords = [
            'faster', 'stronger', 'lighter', 'cheaper', 'more efficient',
            'increase', 'improve', 'enhance', 'optimize', 'better'
        ]

        self.consequence_keywords = [
            'but', 'however', 'causes', 'results in', 'leads to',
            'at the cost of', 'unfortunately', 'downside'
        ]

    def parse(self, problem_text: str) -> ParsedProblem:
        """
        Parse a natural language problem description.

        Args:
            problem_text: Raw problem description

        Returns:
            ParsedProblem with structured components

        Example:
            >>> parser = ProblemParser()
            >>> problem = "Make car faster but not use more fuel"
            >>> parsed = parser.parse(problem)
            >>> print(parsed.desired_improvement)  # "faster"
        """

        # Normalize text
        normalized = self._normalize_text(problem_text)

        # Extract components
        technical_system = self._extract_technical_system(normalized)
        improvement = self._extract_desired_improvement(normalized)
        consequence = self._extract_undesired_consequence(normalized)
        constraints = self._extract_constraints(normalized)
        context = self._extract_context(normalized)

        return ParsedProblem(
            original_text=problem_text,
            normalized_description=normalized,
            technical_system=technical_system,
            desired_improvement=improvement,
            undesired_consequence=consequence,
            constraints=constraints,
            context=context
        )

    def _normalize_text(self, text: str) -> str:
        """Clean and normalize input text."""
        # Basic cleaning
        text = re.sub(r'\s+', ' ', text.strip())
        text = text.lower()
        return text

    def _extract_technical_system(self, text: str) -> Optional[str]:
        """Extract the technical system being discussed."""
        # Simple pattern matching - in real implementation would be more sophisticated
        system_patterns = [
            r'(car|vehicle|automobile)',
            r'(engine|motor)',
            r'(machine|device|system)'
        ]

        for pattern in system_patterns:
            match = re.search(pattern, text)
            if match:
                return match.group(1)

        return None

    def _extract_desired_improvement(self, text: str) -> Optional[str]:
        """Extract what needs to be improved."""
        for keyword in self.improvement_keywords:
            if keyword in text:
                return keyword
        return None

    def _extract_undesired_consequence(self, text: str) -> Optional[str]:
        """Extract the undesired side effect."""
        # Look for consequence keywords and extract what follows
        for keyword in self.consequence_keywords:
            if keyword in text:
                parts = text.split(keyword, 1)
                if len(parts) > 1:
                    consequence = parts[1].strip()
                    return consequence[:50]  # Truncate for brevity
        return None

    def _extract_constraints(self, text: str) -> List[str]:
        """Extract any constraints mentioned."""
        constraints = []

        # Look for constraint indicators
        constraint_patterns = [
            r'without (\w+)',
            r'must not (\w+)',
            r'cannot (\w+)'
        ]

        for pattern in constraint_patterns:
            matches = re.findall(pattern, text)
            constraints.extend(matches)

        return constraints

    def _extract_context(self, text: str) -> Dict[str, str]:
        """Extract contextual information."""
        context = {}

        # Domain detection
        if any(word in text for word in ['car', 'vehicle', 'engine']):
            context['domain'] = 'automotive'
        elif any(word in text for word in ['machine', 'manufacturing']):
            context['domain'] = 'manufacturing'
        else:
            context['domain'] = 'general'

        return context


if __name__ == "__main__":
    # Example usage
    parser = ProblemParser()

    test_problems = [
        "We need to make a car faster, but increasing engine power makes it consume more fuel.",
        "The machine needs to be stronger but not heavier.",
        "Improve product quality without increasing manufacturing time."
    ]

    for problem in test_problems:
        parsed = parser.parse(problem)
        print(f"Original: {parsed.original_text}")
        print(f"System: {parsed.technical_system}")
        print(f"Improvement: {parsed.desired_improvement}")
        print(f"Consequence: {parsed.undesired_consequence}")
        print(f"Context: {parsed.context}")
        print("-" * 50)
