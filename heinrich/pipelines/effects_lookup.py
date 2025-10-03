"""
Heinrich TRIZ Engine - Effects Lookup Module
Provides scientific effects and technical knowledge for solution generation.
"""

import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class ScientificEffect:
    """Represents a scientific effect or technical phenomenon."""

    id: str
    name: str
    description: str
    category: str
    applications: List[str]
    related_principles: List[int]
    technical_domains: List[str]

@dataclass
class EffectRecommendation:
    """Recommendation for using a scientific effect."""

    effect: ScientificEffect
    relevance_score: float
    reasoning: str
    combination_principles: List[int]

class EffectsLookup:
    """Provides scientific effects and technical knowledge for TRIZ solution generation."""

    def __init__(self, effects_file: str = "heinrich/knowledge/effects_database.json"):
        """Initialize with scientific effects database."""
        self.effects_database = self._load_effects_database(effects_file)

    def _load_effects_database(self, effects_file: str) -> Dict[str, ScientificEffect]:
        """Load the scientific effects database."""
        # For now, create a comprehensive effects database
        # In a full implementation, this would load from a JSON file

        effects_data = {
            "thermal_expansion": ScientificEffect(
                id="thermal_expansion",
                name="Thermal Expansion",
                description="Materials expand when heated and contract when cooled",
                category="Thermal",
                applications=[
                    "Bi-metal strips in thermostats",
                    "Expansion joints in bridges",
                    "Shrink-fit assembly"
                ],
                related_principles=[37, 15, 35],
                technical_domains=["Mechanical", "Civil", "Manufacturing"]
            ),

            "shape_memory": ScientificEffect(
                id="shape_memory",
                name="Shape Memory Effect",
                description="Certain alloys return to their original shape when heated",
                category="Material Science",
                applications=[
                    "Shape memory stents",
                    "Self-deploying structures",
                    "Temperature-activated fasteners"
                ],
                related_principles=[35, 15, 25],
                technical_domains=["Medical", "Aerospace", "Robotics"]
            ),

            "piezoelectric": ScientificEffect(
                id="piezoelectric",
                name="Piezoelectric Effect",
                description="Materials generate electricity when mechanically stressed",
                category="Electrical",
                applications=[
                    "Quartz watches",
                    "Ultrasonic transducers",
                    "Energy harvesting from vibration"
                ],
                related_principles=[15, 18, 23],
                technical_domains=["Electronics", "Sensors", "Energy"]
            ),

            "electrochromic": ScientificEffect(
                id="electrochromic",
                name="Electrochromic Effect",
                description="Materials change color when electric voltage is applied",
                category="Optical",
                applications=[
                    "Smart windows",
                    "Anti-glare mirrors",
                    "Display technologies"
                ],
                related_principles=[32, 35, 16],
                technical_domains=["Architecture", "Automotive", "Displays"]
            ),

            "superconductivity": ScientificEffect(
                id="superconductivity",
                name="Superconductivity",
                description="Zero electrical resistance at very low temperatures",
                category="Electrical",
                applications=[
                    "MRI machines",
                    "Maglev trains",
                    "Power transmission"
                ],
                related_principles=[36, 2, 12],
                technical_domains=["Medical", "Transportation", "Energy"]
            ),

            "aerogel": ScientificEffect(
                id="aerogel",
                name="Aerogel Properties",
                description="Extremely low density solid with excellent insulation properties",
                category="Material Science",
                applications=[
                    "Thermal insulation",
                    "Acoustic damping",
                    "Lightweight structures"
                ],
                related_principles=[31, 8, 40],
                technical_domains=["Aerospace", "Construction", "Energy"]
            ),

            "sonoluminescence": ScientificEffect(
                id="sonoluminescence",
                name="Sonoluminescence",
                description="Light emission from collapsing bubbles in liquid under sound waves",
                category="Acoustic",
                applications=[
                    "Sonochemistry",
                    "Medical imaging",
                    "Cleaning technologies"
                ],
                related_principles=[18, 31, 16],
                technical_domains=["Chemistry", "Medical", "Industrial"]
            ),

            "capillary_action": ScientificEffect(
                id="capillary_action",
                name="Capillary Action",
                description="Liquid movement through narrow spaces against gravity",
                category="Fluid",
                applications=[
                    "Wick in candles",
                    "Plant root systems",
                    "Porous media flow"
                ],
                related_principles=[31, 17, 29],
                technical_domains=["Chemical", "Agricultural", "Materials"]
            ),

            "thermoelectric": ScientificEffect(
                id="thermoelectric",
                name="Thermoelectric Effect",
                description="Direct conversion between temperature differences and electric voltage",
                category="Electrical",
                applications=[
                    "Waste heat recovery",
                    "Temperature sensors",
                    "Portable refrigerators"
                ],
                related_principles=[22, 23, 35],
                technical_domains=["Energy", "Sensors", "Electronics"]
            ),

            "magnetorheological": ScientificEffect(
                id="magnetorheological",
                name="Magnetorheological Effect",
                description="Fluids change viscosity in magnetic fields",
                category="Material Science",
                applications=[
                    "Adaptive shock absorbers",
                    "Clutches and brakes",
                    "Seismic dampers"
                ],
                related_principles=[15, 35, 16],
                technical_domains=["Automotive", "Civil", "Robotics"]
            )
        }

        return {effect_id: effect for effect_id, effect in effects_data.items()}

    def find_effects_for_principles(self, principle_ids: List[int],
                                  domain_keywords: List[str] = None) -> List[EffectRecommendation]:
        """
        Find scientific effects relevant to given TRIZ principles.

        Args:
            principle_ids: List of TRIZ principle IDs
            domain_keywords: Optional keywords for domain-specific filtering

        Returns:
            List of effect recommendations with relevance scores
        """
        recommendations = []

        for effect_id, effect in self.effects_database.items():
            # Calculate relevance based on principle overlap
            common_principles = set(principle_ids) & set(effect.related_principles)
            if not common_principles:
                continue

            relevance_score = len(common_principles) / len(principle_ids)

            # Boost score if domain keywords match
            if domain_keywords:
                domain_match = self._calculate_domain_match(effect, domain_keywords)
                relevance_score = (relevance_score + domain_match) / 2

            if relevance_score > 0.2:  # Minimum relevance threshold
                recommendation = EffectRecommendation(
                    effect=effect,
                    relevance_score=relevance_score,
                    reasoning=self._generate_effect_reasoning(effect, principle_ids, common_principles),
                    combination_principles=list(common_principles)
                )
                recommendations.append(recommendation)

        # Sort by relevance score
        recommendations.sort(key=lambda x: x.relevance_score, reverse=True)

        return recommendations

    def find_effects_for_contradiction(self, improving_param: int, worsening_param: int,
                                     domain_keywords: List[str] = None) -> List[EffectRecommendation]:
        """
        Find effects that can help resolve a specific contradiction.

        Args:
            improving_param: TRIZ parameter to improve
            worsening_param: TRIZ parameter that worsens
            domain_keywords: Optional domain-specific keywords

        Returns:
            List of effect recommendations
        """
        # Map parameters to relevant effect categories
        param_to_effects = {
            9: ["thermal_expansion", "shape_memory", "piezoelectric"],  # Speed
            14: ["shape_memory", "magnetorheological", "thermal_expansion"],  # Strength
            17: ["thermal_expansion", "shape_memory", "superconductivity"],  # Temperature
            19: ["thermoelectric", "capillary_action", "aerogel"],  # Energy consumption
            21: ["piezoelectric", "thermoelectric", "magnetorheological"],  # Power
        }

        relevant_effect_ids = set()
        for param in [improving_param, worsening_param]:
            if param in param_to_effects:
                relevant_effect_ids.update(param_to_effects[param])

        # Also include effects that match domain keywords
        if domain_keywords:
            for effect in self.effects_database.values():
                if self._matches_domain_keywords(effect, domain_keywords):
                    relevant_effect_ids.add(effect.id)

        recommendations = []
        for effect_id in relevant_effect_ids:
            if effect_id in self.effects_database:
                effect = self.effects_database[effect_id]

                # Calculate relevance for this contradiction
                relevance_score = self._calculate_contradiction_relevance(
                    effect, improving_param, worsening_param
                )

                if relevance_score > 0.1:
                    recommendation = EffectRecommendation(
                        effect=effect,
                        relevance_score=relevance_score,
                        reasoning=self._generate_contradiction_reasoning(
                            effect, improving_param, worsening_param
                        ),
                        combination_principles=effect.related_principles
                    )
                    recommendations.append(recommendation)

        # Sort by relevance score
        recommendations.sort(key=lambda x: x.relevance_score, reverse=True)

        return recommendations

    def _calculate_domain_match(self, effect: ScientificEffect, domain_keywords: List[str]) -> float:
        """Calculate how well an effect matches domain keywords."""
        score = 0.0
        keywords_lower = [kw.lower() for kw in domain_keywords]

        # Check applications
        for app in effect.applications:
            for keyword in keywords_lower:
                if keyword in app.lower():
                    score += 0.3

        # Check technical domains
        for domain in effect.technical_domains:
            for keyword in keywords_lower:
                if keyword in domain.lower():
                    score += 0.2

        return min(score, 1.0)

    def _matches_domain_keywords(self, effect: ScientificEffect, domain_keywords: List[str]) -> bool:
        """Check if effect matches any domain keywords."""
        keywords_lower = [kw.lower() for kw in domain_keywords]

        # Check applications
        for app in effect.applications:
            if any(kw in app.lower() for kw in keywords_lower):
                return True

        # Check technical domains
        for domain in effect.technical_domains:
            if any(kw in domain.lower() for kw in keywords_lower):
                return True

        return False

    def _calculate_contradiction_relevance(self, effect: ScientificEffect,
                                         improving_param: int, worsening_param: int) -> float:
        """Calculate relevance of an effect for a specific contradiction."""
        # Base relevance from related principles
        principle_relevance = len(set(effect.related_principles) & {15, 35, 2, 1}) / 4.0

        # Parameter-specific relevance
        param_relevance = 0.0
        if improving_param in {9, 19, 21}:  # Speed, Energy, Power
            if any(param in effect.technical_domains for param in ["Energy", "Electronics"]):
                param_relevance += 0.3

        if worsening_param in {1, 14}:  # Weight, Strength
            if any(param in effect.technical_domains for param in ["Materials", "Mechanical"]):
                param_relevance += 0.3

        return min(principle_relevance + param_relevance, 1.0)

    def _generate_effect_reasoning(self, effect: ScientificEffect,
                                 principles: List[int], common_principles: set) -> str:
        """Generate reasoning for effect recommendation."""
        reasoning = f"The '{effect.name}' effect can enhance solutions based on "

        principle_names = []
        for pid in common_principles:
            if pid in {1, 2, 3, 4, 5}:
                principle_names.append("separation principles")
            elif pid in {15, 35}:
                principle_names.append("dynamics and adaptation")
            else:
                principle_names.append(f"principle {pid}")

        reasoning += " and ".join(principle_names)
        reasoning += ". "

        if effect.applications:
            reasoning += f"For example, it has been used in {effect.applications[0].lower()}."

        return reasoning

    def _generate_contradiction_reasoning(self, effect: ScientificEffect,
                                       improving_param: int, worsening_param: int) -> str:
        """Generate reasoning for contradiction-specific recommendation."""
        param_names = {
            1: "weight", 9: "speed", 14: "strength", 19: "energy consumption",
            21: "power", 27: "reliability"
        }

        imp_name = param_names.get(improving_param, f"parameter {improving_param}")
        wors_name = param_names.get(worsening_param, f"parameter {worsening_param}")

        reasoning = f"The '{effect.name}' effect can help resolve the contradiction between "
        reasoning += f"improving {imp_name} while avoiding degradation of {wors_name}. "

        reasoning += f"This effect is particularly relevant for {', '.join(effect.technical_domains)} applications."

        return reasoning

    def get_effect_info(self, effect_id: str) -> Optional[ScientificEffect]:
        """Get detailed information about a specific effect."""
        return self.effects_database.get(effect_id)

    def list_all_effects(self) -> List[ScientificEffect]:
        """Get list of all available scientific effects."""
        return list(self.effects_database.values())

    def search_effects(self, query: str) -> List[ScientificEffect]:
        """Search effects by name, description, or application."""
        query_lower = query.lower()
        results = []

        for effect in self.effects_database.values():
            if (query_lower in effect.name.lower() or
                query_lower in effect.description.lower() or
                any(query_lower in app.lower() for app in effect.applications)):
                results.append(effect)

        return results
