"""
Heinrich TRIZ Engine - Contradiction Identifier Module
Maps problems to the 39 TRIZ parameters and identifies technical contradictions.
"""

import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import yaml

@dataclass
class TechnicalContradiction:
    """Represents a technical contradiction between two TRIZ parameters."""

    improving_parameter: int
    improving_parameter_name: str
    worsening_parameter: int
    worsening_parameter_name: str
    confidence_score: float
    reasoning: str

@dataclass
class ContradictionResult:
    """Result of contradiction identification process."""

    contradictions: List[TechnicalContradiction]
    primary_contradiction: Optional[TechnicalContradiction]
    alternative_contradictions: List[TechnicalContradiction]

class ContradictionIdentifier:
    """Identifies technical contradictions by mapping problems to 39 TRIZ parameters."""

    def __init__(self, parameters_file: str = "heinrich/knowledge/39_parameters.yaml"):
        """Initialize with TRIZ parameters knowledge base."""
        with open(parameters_file, 'r', encoding='utf-8') as f:
            self.parameters_data = yaml.safe_load(f)

        self.parameters = self.parameters_data['parameters']
        self.parameter_keywords = self._build_parameter_keywords()

    def _build_parameter_keywords(self) -> Dict[str, List[str]]:
        """Build keyword mappings for each TRIZ parameter."""
        keywords = {}

        for param in self.parameters:
            param_id = param['id']
            name = param['name'].lower()
            description = param['description'].lower()

            # Extract key terms from parameter names and descriptions
            key_terms = []

            # Add words from parameter name
            words = re.findall(r'\b\w+\b', name)
            key_terms.extend(words)

            # Add words from description
            words = re.findall(r'\b\w+\b', description)
            key_terms.extend(words)

            # Remove common stop words
            stop_words = {'of', 'the', 'and', 'or', 'to', 'in', 'on', 'at', 'by', 'for', 'with'}
            key_terms = [word for word in key_terms if word not in stop_words and len(word) > 2]

            keywords[param_id] = list(set(key_terms))

        return keywords

    def identify_contradiction(self, problem_text: str) -> ContradictionResult:
        """
        Identify technical contradictions in a problem description.

        Args:
            problem_text: Natural language problem description

        Returns:
            ContradictionResult with identified contradictions
        """
        # Normalize text
        text = problem_text.lower()

        # Find improvement and worsening parameters
        improvement_candidates = self._find_improvement_parameters(text)
        worsening_candidates = self._find_worsening_parameters(text)

        # Generate contradiction pairs
        contradictions = []
        for imp_param_id, imp_score in improvement_candidates:
            for wors_param_id, wors_score in worsening_candidates:
                if imp_param_id != wors_param_id:  # Avoid self-contradictions
                    confidence = (imp_score + wors_score) / 2

                    imp_param = next(p for p in self.parameters if p['id'] == imp_param_id)
                    wors_param = next(p for p in self.parameters if p['id'] == wors_param_id)

                    contradiction = TechnicalContradiction(
                        improving_parameter=imp_param_id,
                        improving_parameter_name=imp_param['name'],
                        worsening_parameter=wors_param_id,
                        worsening_parameter_name=wors_param['name'],
                        confidence_score=confidence,
                        reasoning=f"Identified contradiction between improving {imp_param['name']} and worsening {wors_param['name']}"
                    )
                    contradictions.append(contradiction)

        # Sort by confidence score
        contradictions.sort(key=lambda x: x.confidence_score, reverse=True)

        # Select primary contradiction (highest confidence)
        primary = contradictions[0] if contradictions else None

        # Alternative contradictions (other high-confidence options)
        alternatives = [c for c in contradictions[1:] if c.confidence_score > 0.3]

        return ContradictionResult(
            contradictions=contradictions,
            primary_contradiction=primary,
            alternative_contradictions=alternatives
        )

    def _find_improvement_parameters(self, text: str) -> List[Tuple[int, float]]:
        """Find parameters that represent desired improvements."""
        candidates = []

        # Improvement keywords and phrases
        improvement_patterns = [
            r'(?:make|want|need|desire|improve|increase|enhance|optimize|better)\s+(?:more|less|better|faster|stronger|slower|weaker|cheaper|expensive)?\s*(\w+)',
            r'(?:increase|improve|enhance)\s+(?:the\s+)?(\w+)',
            r'(?:better|faster|stronger|lighter|cheaper)\s+(\w+)',
            r'(?:reduce|decrease|minimize)\s+(?:the\s+)?(\w+)'
        ]

        for pattern in improvement_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                keyword = match.group(1) if match.groups() else match.group(0)
                param_scores = self._match_keyword_to_parameters(keyword)
                candidates.extend(param_scores)

        # Score and rank candidates
        scored_candidates = {}
        for param_id, score in candidates:
            scored_candidates[param_id] = max(scored_candidates.get(param_id, 0), score)

        return list(scored_candidates.items())

    def _find_worsening_parameters(self, text: str) -> List[Tuple[int, float]]:
        """Find parameters that represent undesired consequences."""
        candidates = []

        # Worsening keywords and phrases
        worsening_patterns = [
            r'(?:but|however|unfortunately|causes|results?\s+in|leads?\s+to)\s+(?:more|increased|higher|worse|expensive|heavier|slower)\s*(\w+)',
            r'(?:at\s+the\s+cost\s+of|at\s+the\s+expense\s+of)\s+(?:more|increased|higher|worse)\s*(\w+)',
            r'(?:increases?|worsens?|degrades?)\s+(?:the\s+)?(\w+)',
            r'(?:problem|issue|difficulty|drawback)\s+(?:with|of|in)\s+(\w+)'
        ]

        for pattern in worsening_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                keyword = match.group(1) if match.groups() else match.group(0)
                param_scores = self._match_keyword_to_parameters(keyword)
                candidates.extend(param_scores)

        # Score and rank candidates
        scored_candidates = {}
        for param_id, score in candidates:
            scored_candidates[param_id] = max(scored_candidates.get(param_id, 0), score)

        return list(scored_candidates.items())

    def _match_keyword_to_parameters(self, keyword: str) -> List[Tuple[int, float]]:
        """Match a keyword to relevant TRIZ parameters with confidence scores."""
        matches = []
        keyword_lower = keyword.lower()

        for param_id, keywords in self.parameter_keywords.items():
            # Calculate similarity score
            score = 0.0

            # Exact match gets highest score
            if keyword_lower in [k.lower() for k in keywords]:
                score = 1.0
            else:
                # Partial matches get lower scores
                for param_keyword in keywords:
                    if keyword_lower in param_keyword or param_keyword in keyword_lower:
                        score = max(score, 0.7)
                    elif self._levenshtein_distance(keyword_lower, param_keyword) <= 2:
                        score = max(score, 0.5)

            if score > 0.3:  # Only include reasonably confident matches
                matches.append((param_id, score))

        return matches

    def _levenshtein_distance(self, s1: str, s2: str) -> int:
        """Calculate Levenshtein distance between two strings."""
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = list(range(len(s2) + 1))
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def get_parameter_info(self, param_id: int) -> Optional[Dict]:
        """Get detailed information about a specific parameter."""
        for param in self.parameters:
            if param['id'] == param_id:
                return param
        return None

    def list_all_parameters(self) -> List[Dict]:
        """Get list of all 39 TRIZ parameters."""
        return self.parameters.copy()
