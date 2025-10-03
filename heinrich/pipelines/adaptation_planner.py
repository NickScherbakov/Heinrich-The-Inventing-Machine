"""
Heinrich TRIZ Engine - Adaptation Planner Module
Adapts solution concepts to specific contexts and constraints.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class AdaptationContext:
    """Context information for concept adaptation."""

    industry: str
    company_size: str  # "Startup", "SME", "Enterprise"
    budget_level: str   # "Low", "Medium", "High"
    timeline: str       # "Short-term", "Medium-term", "Long-term"
    technical_expertise: str  # "Low", "Medium", "High"
    risk_tolerance: str       # "Conservative", "Moderate", "Aggressive"
    existing_infrastructure: List[str]
    regulatory_constraints: List[str]
    market_requirements: List[str]

@dataclass
class AdaptedConcept:
    """A solution concept adapted to specific context."""

    original_concept_id: str
    adapted_title: str
    adapted_description: str
    contextual_modifications: List[str]
    implementation_roadmap: List[str]
    resource_requirements: Dict[str, str]
    risk_assessment: Dict[str, str]
    success_metrics: List[str]
    adaptation_confidence: float

@dataclass
class AdaptationResult:
    """Result of adaptation planning process."""

    adapted_concepts: List[AdaptedConcept]
    recommended_concept: Optional[AdaptedConcept]
    adaptation_strategy: str
    contextual_insights: List[str]

class AdaptationPlanner:
    """Adapts TRIZ solution concepts to specific organizational and market contexts."""

    def __init__(self):
        """Initialize the adaptation planner."""
        self.adaptation_rules = self._load_adaptation_rules()

    def _load_adaptation_rules(self) -> Dict[str, Dict]:
        """Load adaptation rules for different contexts."""
        return {
            "budget_constraints": {
                "low": {
                    "focus": ["low-cost materials", "existing infrastructure", "phased implementation"],
                    "avoid": ["custom development", "premium materials", "complex systems"]
                },
                "medium": {
                    "focus": ["balanced approach", "some customization", "moderate investment"],
                    "avoid": ["extreme complexity", "very long timelines"]
                },
                "high": {
                    "focus": ["premium solutions", "custom development", "cutting-edge technology"],
                    "avoid": ["budget limitations", "timeline constraints"]
                }
            },

            "timeline_constraints": {
                "short": {
                    "focus": ["quick wins", "existing solutions", "minimal development"],
                    "avoid": ["long R&D cycles", "complex integration", "extensive testing"]
                },
                "medium": {
                    "focus": ["balanced development", "some innovation", "moderate testing"],
                    "avoid": ["very aggressive timelines", "insufficient validation"]
                },
                "long": {
                    "focus": ["breakthrough innovation", "extensive R&D", "thorough validation"],
                    "avoid": ["rushed implementation", "insufficient research"]
                }
            },

            "technical_expertise": {
                "low": {
                    "focus": ["simple solutions", "off-the-shelf components", "external expertise"],
                    "avoid": ["complex customization", "advanced materials", "novel processes"]
                },
                "medium": {
                    "focus": ["moderate complexity", "some customization", "internal development"],
                    "avoid": ["very high complexity", "unproven technology"]
                },
                "high": {
                    "focus": ["complex solutions", "advanced materials", "innovative approaches"],
                    "avoid": ["oversimplified solutions", "limited innovation potential"]
                }
            }
        }

    def adapt_concepts(self,
                      concepts: List[Dict],
                      context: AdaptationContext,
                      num_adaptations: int = 2) -> AdaptationResult:
        """
        Adapt solution concepts to specific organizational context.

        Args:
            concepts: List of solution concept dictionaries
            context: Adaptation context information
            num_adaptations: Number of adapted concepts to generate

        Returns:
            AdaptationResult with adapted concepts and recommendations
        """
        adapted_concepts = []

        for i, concept in enumerate(concepts[:num_adaptations]):
            adapted = self._adapt_single_concept(concept, context, i + 1)
            adapted_concepts.append(adapted)

        # Select recommended concept based on context fit
        recommended_concept = self._select_recommended_concept(adapted_concepts, context)

        # Generate adaptation strategy
        strategy = self._generate_adaptation_strategy(context)

        # Generate contextual insights
        insights = self._generate_contextual_insights(context, adapted_concepts)

        return AdaptationResult(
            adapted_concepts=adapted_concepts,
            recommended_concept=recommended_concept,
            adaptation_strategy=strategy,
            contextual_insights=insights
        )

    def _adapt_single_concept(self,
                            concept: Dict,
                            context: AdaptationContext,
                            adaptation_number: int) -> AdaptedConcept:
        """Adapt a single concept to the given context."""

        # Generate adapted title and description
        adapted_title = self._adapt_concept_title(concept['title'], context)
        adapted_description = self._adapt_concept_description(concept['description'], context)

        # Generate contextual modifications
        modifications = self._generate_contextual_modifications(concept, context)

        # Generate implementation roadmap
        roadmap = self._generate_implementation_roadmap(concept, context)

        # Assess resource requirements
        resources = self._assess_resource_requirements(concept, context)

        # Assess risks
        risks = self._assess_risks(concept, context)

        # Define success metrics
        metrics = self._define_success_metrics(concept, context)

        # Calculate adaptation confidence
        confidence = self._calculate_adaptation_confidence(concept, context)

        return AdaptedConcept(
            original_concept_id=concept['concept_id'],
            adapted_title=adapted_title,
            adapted_description=adapted_description,
            contextual_modifications=modifications,
            implementation_roadmap=roadmap,
            resource_requirements=resources,
            risk_assessment=risks,
            success_metrics=metrics,
            adaptation_confidence=confidence
        )

    def _adapt_concept_title(self, original_title: str, context: AdaptationContext) -> str:
        """Adapt concept title for the specific context."""
        # Add context-specific prefixes or suffixes
        if context.budget_level == "low":
            return f"Budget-Friendly {original_title}"
        elif context.timeline == "short":
            return f"Quick-Implementation {original_title}"
        elif context.company_size == "startup":
            return f"Startup-Suitable {original_title}"
        else:
            return f"Enterprise {original_title}"

    def _adapt_concept_description(self, original_description: str, context: AdaptationContext) -> str:
        """Adapt concept description for the specific context."""
        # Modify description based on context constraints
        adapted = original_description

        if context.budget_level == "low":
            adapted += " This adaptation focuses on cost-effective implementation using available resources."
        elif context.technical_expertise == "low":
            adapted += " This approach uses accessible technology and can leverage external expertise."
        elif context.timeline == "short":
            adapted += " This implementation prioritizes quick deployment and immediate benefits."

        return adapted

    def _generate_contextual_modifications(self, concept: Dict, context: AdaptationContext) -> List[str]:
        """Generate context-specific modifications to the concept."""
        modifications = []

        # Budget-based modifications
        if context.budget_level == "low":
            modifications.extend([
                "Use off-the-shelf components instead of custom development",
                "Implement in phases to spread costs over time",
                "Leverage existing infrastructure and tools"
            ])
        elif context.budget_level == "high":
            modifications.extend([
                "Incorporate premium materials for enhanced performance",
                "Invest in custom development for optimal results",
                "Include comprehensive testing and validation"
            ])

        # Timeline-based modifications
        if context.timeline == "short":
            modifications.extend([
                "Prioritize quick wins and immediate benefits",
                "Use proven technologies to minimize development time",
                "Implement with minimal customization initially"
            ])
        elif context.timeline == "long":
            modifications.extend([
                "Include thorough research and development phase",
                "Plan for extensive testing and validation",
                "Consider breakthrough innovations that require more time"
            ])

        # Expertise-based modifications
        if context.technical_expertise == "low":
            modifications.extend([
                "Partner with external experts for complex aspects",
                "Use simplified versions of advanced technologies",
                "Include comprehensive training and documentation"
            ])
        elif context.technical_expertise == "high":
            modifications.extend([
                "Leverage internal expertise for custom optimization",
                "Explore advanced variations of the core concept",
                "Include research components for further innovation"
            ])

        return modifications[:5]  # Limit to 5 modifications

    def _generate_implementation_roadmap(self, concept: Dict, context: AdaptationContext) -> List[str]:
        """Generate a context-appropriate implementation roadmap."""
        base_steps = [
            "1. Assess current capabilities and resources",
            "2. Acquire necessary materials and components",
            "3. Develop prototype or pilot implementation",
            "4. Test and validate the solution",
            "5. Deploy and monitor performance",
            "6. Optimize based on real-world feedback"
        ]

        # Adjust timeline based on context
        if context.timeline == "short":
            # Compress timeline, combine steps
            roadmap = [
                "1. Quick assessment and resource acquisition (1-2 weeks)",
                "2. Rapid prototyping and initial testing (2-4 weeks)",
                "3. Immediate deployment with basic optimization (1-2 weeks)",
                "4. Performance monitoring and quick iterations (ongoing)"
            ]
        elif context.timeline == "long":
            # Expand timeline, add more detailed steps
            roadmap = [
                "1. Comprehensive capability and resource assessment (2-4 weeks)",
                "2. Detailed planning and specification development (3-6 weeks)",
                "3. Extensive prototyping with multiple iterations (8-12 weeks)",
                "4. Thorough testing and validation across scenarios (6-8 weeks)",
                "5. Phased deployment with monitoring (4-6 weeks)",
                "6. Continuous optimization and enhancement (ongoing)"
            ]
        else:
            roadmap = base_steps

        # Adjust based on budget
        if context.budget_level == "low":
            for i, step in enumerate(roadmap):
                roadmap[i] = step.replace("comprehensive", "focused").replace("extensive", "targeted")

        return roadmap

    def _assess_resource_requirements(self, concept: Dict, context: AdaptationContext) -> Dict[str, str]:
        """Assess resource requirements for the adapted concept."""
        requirements = {}

        # Budget assessment
        if context.budget_level == "low":
            requirements["financial"] = "Minimal investment required - leverage existing resources"
        elif context.budget_level == "medium":
            requirements["financial"] = "Moderate investment - some new equipment or materials needed"
        else:
            requirements["financial"] = "Significant investment - custom development and premium components"

        # Time assessment
        if context.timeline == "short":
            requirements["time"] = "1-3 months for initial implementation"
        elif context.timeline == "medium":
            requirements["time"] = "3-6 months for full implementation"
        else:
            requirements["time"] = "6-12 months for complete development and deployment"

        # Expertise assessment
        if context.technical_expertise == "low":
            requirements["expertise"] = "External consultation recommended for complex aspects"
        elif context.technical_expertise == "medium":
            requirements["expertise"] = "Internal team can handle most aspects with some training"
        else:
            requirements["expertise"] = "Internal expertise sufficient for full implementation"

        # Infrastructure assessment
        existing_infra = context.existing_infrastructure
        if existing_infra:
            requirements["infrastructure"] = f"Can leverage: {', '.join(existing_infra[:3])}"
        else:
            requirements["infrastructure"] = "New infrastructure investment may be required"

        return requirements

    def _assess_risks(self, concept: Dict, context: AdaptationContext) -> Dict[str, str]:
        """Assess risks for the adapted concept."""
        risks = {}

        # Technical risks
        if context.technical_expertise == "low":
            risks["technical"] = "Medium - Limited internal expertise may require external support"
        else:
            risks["technical"] = "Low - Sufficient expertise to manage implementation"

        # Financial risks
        if context.budget_level == "low":
            risks["financial"] = "Low - Minimal financial exposure"
        elif context.budget_level == "high":
            risks["financial"] = "Medium - Significant investment with potential overruns"
        else:
            risks["financial"] = "Low - Moderate investment with controlled budget"

        # Timeline risks
        if context.timeline == "short":
            risks["timeline"] = "High - Aggressive schedule may compromise quality"
        elif context.timeline == "long":
            risks["timeline"] = "Low - Ample time for proper development"
        else:
            risks["timeline"] = "Medium - Standard timeline with some flexibility"

        # Market/regulatory risks
        if context.regulatory_constraints:
            risks["regulatory"] = f"Medium - Must address: {', '.join(context.regulatory_constraints[:2])}"
        else:
            risks["regulatory"] = "Low - No significant regulatory concerns"

        return risks

    def _define_success_metrics(self, concept: Dict, context: AdaptationContext) -> List[str]:
        """Define success metrics for the adapted concept."""
        metrics = [
            "Achievement of original performance objectives",
            "Implementation within budget constraints",
            "Deployment within specified timeline",
            "User satisfaction and acceptance"
        ]

        # Context-specific metrics
        if context.industry.lower() in ["automotive", "manufacturing"]:
            metrics.append("Improvement in production efficiency or quality")
        elif context.industry.lower() in ["medical", "healthcare"]:
            metrics.append("Compliance with regulatory requirements and safety standards")
        elif context.industry.lower() in ["energy", "environmental"]:
            metrics.append("Reduction in environmental impact or energy consumption")

        # Company size specific metrics
        if context.company_size == "startup":
            metrics.append("Time to market and competitive advantage")
        elif context.company_size == "enterprise":
            metrics.append("Scalability and integration with existing systems")

        return metrics

    def _calculate_adaptation_confidence(self, concept: Dict, context: AdaptationContext) -> float:
        """Calculate confidence level for the adaptation."""
        confidence = 0.5  # Base confidence

        # Boost confidence based on context alignment
        if context.budget_level == "medium":
            confidence += 0.2  # Balanced budget is most flexible
        if context.timeline == "medium":
            confidence += 0.2  # Balanced timeline allows proper development
        if context.technical_expertise == "medium":
            confidence += 0.2  # Medium expertise is often optimal

        # Reduce confidence for extreme constraints
        if context.budget_level == "low" and concept.get('estimated_complexity') == "High":
            confidence -= 0.2
        if context.timeline == "short" and concept.get('innovation_level') == "Breakthrough":
            confidence -= 0.2

        return max(0.1, min(1.0, confidence))  # Clamp between 0.1 and 1.0

    def _select_recommended_concept(self,
                                  adapted_concepts: List[AdaptedConcept],
                                  context: AdaptationContext) -> Optional[AdaptedConcept]:
        """Select the best concept for the given context."""
        if not adapted_concepts:
            return None

        # Score concepts based on context fit
        scored_concepts = []
        for concept in adapted_concepts:
            score = concept.adaptation_confidence

            # Bonus for matching company size
            if context.company_size == "startup" and len(concept.implementation_roadmap) <= 4:
                score += 0.1
            elif context.company_size == "enterprise" and concept.risk_assessment.get("technical") == "Low":
                score += 0.1

            scored_concepts.append((concept, score))

        # Return highest scoring concept
        scored_concepts.sort(key=lambda x: x[1], reverse=True)
        return scored_concepts[0][0]

    def _generate_adaptation_strategy(self, context: AdaptationContext) -> str:
        """Generate overall adaptation strategy."""
        strategy = f"Adaptation Strategy for {context.company_size} {context.industry} Company:\n\n"

        if context.budget_level == "low":
            strategy += "• Focus on cost-effective, incremental improvements\n"
            strategy += "• Leverage existing infrastructure and expertise\n"
            strategy += "• Implement in phases to manage budget constraints\n"
        elif context.budget_level == "high":
            strategy += "• Invest in breakthrough innovations and custom solutions\n"
            strategy += "• Accept higher complexity for superior performance\n"
            strategy += "• Plan for comprehensive testing and validation\n"

        if context.timeline == "short":
            strategy += "• Prioritize quick wins and immediate benefits\n"
            strategy += "• Use proven technologies to minimize development time\n"
            strategy += "• Consider phased implementation for rapid deployment\n"
        elif context.timeline == "long":
            strategy += "• Plan for thorough research and extensive testing\n"
            strategy += "• Include buffer time for unexpected challenges\n"
            strategy += "• Consider breakthrough innovations that require more time\n"

        return strategy

    def _generate_contextual_insights(self,
                                   context: AdaptationContext,
                                   adapted_concepts: List[AdaptedConcept]) -> List[str]:
        """Generate insights about the adaptation context."""
        insights = []

        # Industry-specific insights
        if context.industry.lower() == "automotive":
            insights.append("Automotive industry emphasizes safety, reliability, and regulatory compliance")
        elif context.industry.lower() == "medical":
            insights.append("Healthcare applications require extensive validation and regulatory approval")
        elif context.industry.lower() == "energy":
            insights.append("Energy sector focuses on efficiency, sustainability, and long-term ROI")

        # Company size insights
        if context.company_size == "startup":
            insights.append("Startups should prioritize speed to market and competitive differentiation")
        elif context.company_size == "enterprise":
            insights.append("Large organizations benefit from scalable solutions and integration capabilities")

        # Risk tolerance insights
        if context.risk_tolerance == "conservative":
            insights.append("Conservative approach favors proven technologies and incremental improvements")
        elif context.risk_tolerance == "aggressive":
            insights.append("Aggressive approach enables breakthrough innovations and competitive advantages")

        return insights
