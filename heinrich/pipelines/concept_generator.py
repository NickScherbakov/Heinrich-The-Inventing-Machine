"""
Heinrich TRIZ Engine - Concept Generator Module
Generates concrete solution concepts by combining TRIZ principles with scientific effects.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
import random

@dataclass
class SolutionConcept:
    """Represents a concrete solution concept generated from TRIZ principles."""

    concept_id: str
    title: str
    description: str
    principles_used: List[int]
    effects_used: List[str]
    implementation_steps: List[str]
    advantages: List[str]
    potential_challenges: List[str]
    domain_applications: List[str]
    estimated_complexity: str  # "Low", "Medium", "High"
    innovation_level: str     # "Incremental", "Radical", "Breakthrough"

@dataclass
class ConceptGenerationResult:
    """Result of concept generation process."""

    concepts: List[SolutionConcept]
    primary_concept: Optional[SolutionConcept]
    alternative_concepts: List[SolutionConcept]
    generation_metadata: Dict[str, str]

class ConceptGenerator:
    """Generates concrete solution concepts by combining TRIZ principles with scientific effects."""

    def __init__(self):
        """Initialize the concept generator."""
        self.concept_templates = self._load_concept_templates()

    def _load_concept_templates(self) -> Dict[str, Dict]:
        """Load templates for generating solution concepts."""
        return {
            "dynamics": {
                "template": "Implement {principle} by making the {component} {dynamic_property} in response to {trigger}",
                "examples": [
                    "Variable geometry wings that change shape based on flight conditions",
                    "Adaptive suspension that adjusts stiffness based on road conditions",
                    "Smart materials that change properties based on temperature"
                ]
            },

            "segmentation": {
                "template": "Apply {principle} by dividing the {system} into {segments} that can {function} independently",
                "examples": [
                    "Modular product design with interchangeable components",
                    "Segmented manufacturing processes for flexibility",
                    "Divided control systems for fault isolation"
                ]
            },

            "local_quality": {
                "template": "Use {principle} to create {gradient} in {property} across the {component}",
                "examples": [
                    "Gradient materials with varying properties",
                    "Non-uniform surface treatments for specific functions",
                    "Spatially varying control parameters"
                ]
            },

            "anti_weight": {
                "template": "Apply {principle} by {compensation_method} to counteract the {negative_effect}",
                "examples": [
                    "Counter-rotating masses to reduce vibration",
                    "Aerodynamic lift to compensate for weight",
                    "Buoyancy to offset gravity effects"
                ]
            },

            "parameter_changes": {
                "template": "Implement {principle} by changing {parameter} from {initial_state} to {final_state}",
                "examples": [
                    "Phase change materials for thermal management",
                    "Shape memory alloys for actuation",
                    "Variable viscosity fluids for adaptive damping"
                ]
            }
        }

    def generate_concepts(self,
                         principles: List[Dict],
                         effects: List[Dict],
                         problem_context: Dict,
                         num_concepts: int = 3) -> ConceptGenerationResult:
        """
        Generate solution concepts by combining TRIZ principles with scientific effects.

        Args:
            principles: List of TRIZ principle dictionaries
            effects: List of scientific effect dictionaries
            problem_context: Context about the original problem
            num_concepts: Number of concepts to generate

        Returns:
            ConceptGenerationResult with generated concepts
        """
        concepts = []

        # Generate concepts by combining principles with effects
        for i in range(min(num_concepts, len(principles) * len(effects))):
            principle = principles[i % len(principles)]
            effect = effects[i % len(effects)]

            concept = self._generate_single_concept(
                principle, effect, problem_context, i + 1
            )
            concepts.append(concept)

        # Sort concepts by innovation potential
        concepts.sort(key=lambda x: self._assess_innovation_potential(x), reverse=True)

        # Select primary and alternative concepts
        primary_concept = concepts[0] if concepts else None
        alternative_concepts = concepts[1:]

        metadata = {
            "total_principles": str(len(principles)),
            "total_effects": str(len(effects)),
            "concepts_generated": str(len(concepts)),
            "generation_method": "principle_effect_combination"
        }

        return ConceptGenerationResult(
            concepts=concepts,
            primary_concept=primary_concept,
            alternative_concepts=alternative_concepts,
            generation_metadata=metadata
        )

    def _generate_single_concept(self,
                               principle: Dict,
                               effect: Dict,
                               problem_context: Dict,
                               concept_number: int) -> SolutionConcept:
        """Generate a single solution concept."""

        # Extract key information
        principle_id = principle['id']
        principle_name = principle['name']
        effect_name = effect['name']

        # Generate concept content
        title = self._generate_concept_title(principle_name, effect_name)
        description = self._generate_concept_description(principle, effect, problem_context)

        # Generate implementation steps
        implementation_steps = self._generate_implementation_steps(principle, effect)

        # Assess concept characteristics
        advantages = self._generate_advantages(principle, effect)
        challenges = self._generate_challenges(principle, effect)
        complexity = self._assess_complexity(principle, effect)
        innovation_level = self._assess_innovation_level(principle, effect)

        # Determine applicable domains
        domains = self._determine_applicable_domains(principle, effect, problem_context)

        return SolutionConcept(
            concept_id=f"concept_{concept_number:03d}",
            title=title,
            description=description,
            principles_used=[principle_id],
            effects_used=[effect['id']],
            implementation_steps=implementation_steps,
            advantages=advantages,
            potential_challenges=challenges,
            domain_applications=domains,
            estimated_complexity=complexity,
            innovation_level=innovation_level
        )

    def _generate_concept_title(self, principle_name: str, effect_name: str) -> str:
        """Generate a catchy title for the concept."""
        title_templates = [
            f"{principle_name} with {effect_name}",
            f"{effect_name}-Enhanced {principle_name}",
            f"Dynamic {principle_name} using {effect_name}",
            f"Adaptive {principle_name} via {effect_name}",
            f"Smart {principle_name} through {effect_name}"
        ]

        return random.choice(title_templates)

    def _generate_concept_description(self,
                                    principle: Dict,
                                    effect: Dict,
                                    problem_context: Dict) -> str:
        """Generate a detailed description of the concept."""

        # Get context information
        system = problem_context.get('technical_system', 'the system')
        improvement = problem_context.get('desired_improvement', 'performance')
        constraint = problem_context.get('constraint', 'constraints')

        # Create description based on principle and effect
        if principle['id'] == 15:  # Dynamics
            description = f"This concept applies dynamic {principle['name'].lower()} "
            description += f"to {system}, utilizing the {effect['name']} "
            description += f"to achieve {improvement} while respecting {constraint}. "
            description += f"The {effect['name'].lower()} enables real-time adaptation "

        elif principle['id'] in [1, 2, 3]:  # Separation principles
            description = f"This approach uses {principle['name'].lower()} "
            description += f"to separate conflicting requirements in {system}. "
            description += f"By leveraging {effect['name']}, "
            description += f"we can achieve {improvement} without compromising other aspects. "

        else:
            description = f"This innovative solution combines {principle['name']} "
            description += f"with the {effect['name']} to address the core contradiction. "
            description += f"The concept enables {improvement} while maintaining {constraint}. "

        # Add specific implementation hint
        if effect['applications']:
            description += f"Similar to how {effect['name'].lower()} is used in {effect['applications'][0].lower()}, "
            description += f"this concept adapts the principle for {system} applications."

        return description

    def _generate_implementation_steps(self, principle: Dict, effect: Dict) -> List[str]:
        """Generate step-by-step implementation guidance."""
        steps = [
            f"1. Analyze the current {principle['name'].lower()} limitations in your system",
            f"2. Identify specific areas where {effect['name']} can be applied",
            f"3. Design the integration mechanism for {principle['name']} and {effect['name']}",
            f"4. Prototype the combined solution at small scale",
            f"5. Test and validate the {effect['name']} response",
            f"6. Optimize the {principle['name'].lower()} parameters",
            f"7. Scale up for full implementation"
        ]
        return steps

    def _generate_advantages(self, principle: Dict, effect: Dict) -> List[str]:
        """Generate list of concept advantages."""
        advantages = []

        # Principle-based advantages
        if principle['id'] == 15:  # Dynamics
            advantages.extend([
                "Adaptive response to changing conditions",
                "Optimal performance across operating range",
                "Reduced need for manual adjustments"
            ])
        elif principle['id'] == 1:  # Segmentation
            advantages.extend([
                "Modular design enables easy maintenance",
                "Independent optimization of components",
                "Fault isolation and graceful degradation"
            ])
        elif principle['id'] == 35:  # Parameter changes
            advantages.extend([
                "Multi-state operation capabilities",
                "Phase-based functionality",
                "Enhanced system flexibility"
            ])

        # Effect-based advantages
        if "thermal" in effect['name'].lower():
            advantages.append("Temperature-responsive behavior")
        if "piezo" in effect['name'].lower():
            advantages.append("Energy harvesting from mechanical stress")
        if "shape memory" in effect['name'].lower():
            advantages.append("Temperature-activated shape recovery")

        # General advantages
        advantages.extend([
            "Systematic approach based on proven TRIZ methodology",
            "Integration of scientific principles with engineering practice",
            "Potential for patentable innovation"
        ])

        return advantages[:5]  # Limit to 5 advantages

    def _generate_challenges(self, principle: Dict, effect: Dict) -> List[str]:
        """Generate list of potential implementation challenges."""
        challenges = []

        # Principle-based challenges
        if principle['id'] == 15:  # Dynamics
            challenges.append("Complexity of dynamic control systems")
        elif principle['id'] in [36, 35]:  # Phase transitions, Parameter changes
            challenges.append("Precise control of transition conditions")
        elif principle['id'] == 1:  # Segmentation
            challenges.append("Integration complexity of multiple segments")

        # Effect-based challenges
        if "thermal" in effect['name'].lower():
            challenges.append("Temperature sensitivity and thermal management")
        if "quantum" in effect['name'].lower():
            challenges.append("Scale-up challenges from quantum effects")
        if "nano" in effect['name'].lower():
            challenges.append("Manufacturing and stability of nanostructures")

        # General challenges
        challenges.extend([
            "Development time and testing requirements",
            "Cost of implementing new technology",
            "Integration with existing systems"
        ])

        return challenges[:4]  # Limit to 4 challenges

    def _assess_complexity(self, principle: Dict, effect: Dict) -> str:
        """Assess implementation complexity."""
        # Base complexity from principle
        if principle['id'] in [1, 8, 13]:  # Simple principles
            complexity_score = 1
        elif principle['id'] in [15, 35, 36]:  # Dynamic/complex principles
            complexity_score = 3
        else:
            complexity_score = 2

        # Adjust based on effect
        if "quantum" in effect['name'].lower() or "nano" in effect['name'].lower():
            complexity_score += 2
        elif "thermal" in effect['name'].lower() or "shape memory" in effect['name'].lower():
            complexity_score += 1

        if complexity_score <= 2:
            return "Low"
        elif complexity_score <= 4:
            return "Medium"
        else:
            return "High"

    def _assess_innovation_level(self, principle: Dict, effect: Dict) -> str:
        """Assess innovation level of the concept."""
        # Rare principle-effect combinations tend to be more innovative
        rare_combinations = {
            (15, "quantum_tunneling"),  # Dynamics + Quantum tunneling
            (35, "shape_memory"),       # Parameter changes + Shape memory
            (18, "sonoluminescence"),   # Mechanical vibration + Sonoluminescence
            (36, "superconductivity"),  # Phase transitions + Superconductivity
        }

        current_combination = (principle['id'], effect['id'])

        if current_combination in rare_combinations:
            return "Breakthrough"
        elif principle['id'] in [15, 35, 36] or effect['id'] in ["quantum_tunneling", "shape_memory"]:
            return "Radical"
        else:
            return "Incremental"

    def _determine_applicable_domains(self, principle: Dict, effect: Dict, problem_context: Dict) -> List[str]:
        """Determine which domains this concept applies to."""
        domains = set()

        # Add effect domains
        domains.update(effect['technical_domains'])

        # Add context-specific domains
        system = problem_context.get('technical_system', '').lower()
        if 'automotive' in system or 'car' in system or 'vehicle' in system:
            domains.update(["Automotive", "Transportation"])
        if 'aerospace' in system or 'aircraft' in system or 'plane' in system:
            domains.update(["Aerospace", "Aviation"])
        if 'medical' in system or 'health' in system:
            domains.update(["Medical", "Healthcare"])

        # Add general domains based on principle
        if principle['id'] in [15, 35]:  # Dynamic principles
            domains.update(["Robotics", "Automation"])

        return list(domains)[:4]  # Limit to 4 domains

    def _assess_innovation_potential(self, concept: SolutionConcept) -> float:
        """Assess overall innovation potential of a concept."""
        score = 0.0

        # Innovation level scoring
        innovation_scores = {"Incremental": 1.0, "Radical": 2.0, "Breakthrough": 3.0}
        score += innovation_scores.get(concept.innovation_level, 1.0)

        # Complexity bonus (moderate complexity is often most innovative)
        complexity_scores = {"Low": 0.5, "Medium": 1.0, "High": 0.8}
        score += complexity_scores.get(concept.estimated_complexity, 0.5)

        # Number of advantages
        score += len(concept.advantages) * 0.2

        # Domain diversity
        score += len(concept.domain_applications) * 0.1

        return score

    def generate_variations(self,
                           base_concept: SolutionConcept,
                           variation_count: int = 2) -> List[SolutionConcept]:
        """Generate variations of a base concept."""
        variations = []

        for i in range(variation_count):
            variation = SolutionConcept(
                concept_id=f"{base_concept.concept_id}_var_{i+1}",
                title=f"{base_concept.title} - Variation {i+1}",
                description=f"Variation of: {base_concept.description}",
                principles_used=base_concept.principles_used.copy(),
                effects_used=base_concept.effects_used.copy(),
                implementation_steps=self._vary_implementation_steps(base_concept.implementation_steps),
                advantages=self._vary_advantages(base_concept.advantages),
                potential_challenges=base_concept.potential_challenges.copy(),
                domain_applications=self._vary_domains(base_concept.domain_applications),
                estimated_complexity=base_concept.estimated_complexity,
                innovation_level=base_concept.innovation_level
            )
            variations.append(variation)

        return variations

    def _vary_implementation_steps(self, steps: List[str]) -> List[str]:
        """Create variations in implementation steps."""
        if len(steps) < 3:
            return steps

        # Simple variation: swap some steps or modify slightly
        varied_steps = steps.copy()
        if len(varied_steps) >= 3:
            # Swap steps 2 and 3
            varied_steps[1], varied_steps[2] = varied_steps[2], varied_steps[1]

        return varied_steps

    def _vary_advantages(self, advantages: List[str]) -> List[str]:
        """Create variations in advantages list."""
        if len(advantages) <= 2:
            return advantages

        # Simple variation: reorder advantages
        varied = advantages.copy()
        random.shuffle(varied)
        return varied

    def _vary_domains(self, domains: List[str]) -> List[str]:
        """Create variations in applicable domains."""
        # Could add related domains or modify existing ones
        variations = domains.copy()

        # Add some related domains based on existing ones
        related_domains = {
            "Automotive": ["Transportation", "Manufacturing"],
            "Medical": ["Healthcare", "Biotechnology"],
            "Aerospace": ["Aviation", "Defense"],
            "Electronics": ["Computing", "Communications"]
        }

        for domain in domains:
            if domain in related_domains:
                related = related_domains[domain]
                for rel_domain in related:
                    if rel_domain not in variations:
                        variations.append(rel_domain)
                        break

        return variations[:5]  # Limit to 5 domains
