"""
Heinrich TRIZ Engine - Knowledge Base Loader
Loads and provides access to TRIZ knowledge base components.
"""

import yaml
import csv
from typing import Dict, List, Optional, Tuple
from pathlib import Path

class KnowledgeLoader:
    """Loads and provides access to the complete TRIZ knowledge base."""

    def __init__(self, knowledge_base_path: str = "heinrich/knowledge"):
        """Initialize with path to knowledge base directory."""
        self.knowledge_path = Path(knowledge_base_path)
        self.parameters = None
        self.principles = None
        self.contradiction_matrix = None

    def load_39_parameters(self) -> Dict:
        """Load the 39 TRIZ parameters."""
        if self.parameters is None:
            with open(self.knowledge_path / "39_parameters.yaml", 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                self.parameters = {p['id']: p for p in data['parameters']}
        return self.parameters

    def load_40_principles(self) -> Dict:
        """Load the 40 TRIZ principles."""
        if self.principles is None:
            with open(self.knowledge_path / "40_principles.yaml", 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                self.principles = {p['id']: p for p in data['principles']}
        return self.principles

    def load_contradiction_matrix(self) -> Dict[Tuple[int, int], List[int]]:
        """Load the contradiction matrix."""
        if self.contradiction_matrix is None:
            matrix = {}
            with open(self.knowledge_path / "contradiction_matrix.csv", 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    imp_param = int(row['improving_parameter'])
                    wors_param = int(row['worsening_parameter'])
                    principles = [int(p.strip()) for p in row['recommended_principles'].split(';')]

                    # Matrix is symmetric
                    matrix[(imp_param, wors_param)] = principles
                    matrix[(wors_param, imp_param)] = principles

            self.contradiction_matrix = matrix
        return self.contradiction_matrix

    def get_parameter_info(self, parameter_id: int) -> Optional[Dict]:
        """Get information about a specific parameter."""
        parameters = self.load_39_parameters()
        return parameters.get(parameter_id)

    def get_principle_info(self, principle_id: int) -> Optional[Dict]:
        """Get information about a specific principle."""
        principles = self.load_40_principles()
        return principles.get(principle_id)

    def get_principles_for_contradiction(self, improving_param: int, worsening_param: int) -> List[int]:
        """Get recommended principles for a specific contradiction."""
        matrix = self.load_contradiction_matrix()
        return matrix.get((improving_param, worsening_param), [])

    def search_parameters(self, query: str) -> List[Dict]:
        """Search parameters by name or description."""
        parameters = self.load_39_parameters()
        query_lower = query.lower()
        results = []

        for param_id, param_data in parameters.items():
            name_lower = param_data['name'].lower()
            desc_lower = param_data['description'].lower()

            if query_lower in name_lower or query_lower in desc_lower:
                results.append(param_data)

        return results

    def search_principles(self, query: str) -> List[Dict]:
        """Search principles by name or description."""
        principles = self.load_40_principles()
        query_lower = query.lower()
        results = []

        for princ_id, princ_data in principles.items():
            name_lower = princ_data['name'].lower()
            desc_lower = princ_data['description'].lower()

            if query_lower in name_lower or query_lower in desc_lower:
                results.append(princ_data)

        return results

    def get_all_parameters(self) -> List[Dict]:
        """Get all 39 TRIZ parameters."""
        parameters = self.load_39_parameters()
        return list(parameters.values())

    def get_all_principles(self) -> List[Dict]:
        """Get all 40 TRIZ principles."""
        principles = self.load_40_principles()
        return list(principles.values())

    def validate_contradiction_matrix(self) -> bool:
        """Validate that the contradiction matrix is properly formatted."""
        try:
            matrix = self.load_contradiction_matrix()
            parameters = self.load_39_parameters()
            principles = self.load_40_principles()

            # Check that all matrix entries reference valid parameters and principles
            for (param1, param2), princ_list in matrix.items():
                if param1 not in parameters or param2 not in parameters:
                    return False
                for princ_id in princ_list:
                    if princ_id not in principles:
                        return False

            return True
        except Exception:
            return False
