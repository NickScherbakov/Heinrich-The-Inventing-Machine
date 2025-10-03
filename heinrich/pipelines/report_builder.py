"""
Heinrich TRIZ Engine - Report Builder Module
Generates comprehensive, structured reports from TRIZ analysis results.
"""

import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime
import textwrap

@dataclass
class ReportSection:
    """A section of the TRIZ analysis report."""

    title: str
    content: str
    section_type: str  # "summary", "analysis", "recommendation", "implementation"
    importance: str    # "high", "medium", "low"

@dataclass
class TRIZReport:
    """Complete TRIZ analysis report."""

    report_id: str
    timestamp: str
    problem_summary: str
    sections: List[ReportSection]
    conclusions: List[str]
    next_steps: List[str]
    metadata: Dict[str, Any]

class ReportBuilder:
    """Builds comprehensive TRIZ analysis reports from pipeline results."""

    def __init__(self):
        """Initialize the report builder."""
        self.report_templates = self._load_report_templates()

    def _load_report_templates(self) -> Dict[str, str]:
        """Load templates for different report sections."""
        return {
            "header": """# Heinrich TRIZ Analysis Report

**Report ID:** {report_id}
**Generated:** {timestamp}
**Analysis Method:** Systematic TRIZ Methodology

---

""",

            "problem_summary": """## Problem Analysis

**Original Problem:**
{problem_text}

**Technical System:** {system}
**Desired Improvement:** {improvement}
**Constraints:** {constraints}

""",

            "contradiction_analysis": """## Technical Contradiction Analysis

**Primary Contradiction:**
- **Improving Parameter:** {improving_param} ({improving_name})
- **Worsening Parameter:** {worsening_param} ({worsening_name})
- **Confidence Score:** {confidence:.2f}

**Contradiction Reasoning:**
{reasoning}

""",

            "principles_section": """## Recommended TRIZ Principles

### Primary Principles

{primary_principles}

### Supporting Principles

{supporting_principles}

""",

            "effects_section": """## Scientific Effects Integration

{effects_list}

""",

            "concepts_section": """## Solution Concepts

{concepts_list}

""",

            "adaptation_section": """## Context-Adapted Solutions

**Adaptation Context:**
- Industry: {industry}
- Company Size: {company_size}
- Budget Level: {budget_level}
- Timeline: {timeline}
- Technical Expertise: {expertise}

{adapted_concepts}

""",

            "conclusions": """## Conclusions and Recommendations

{conclusions_list}

""",

            "next_steps": """## Recommended Next Steps

{next_steps_list}

---

*This report was generated using the Heinrich TRIZ Engine, combining systematic TRIZ methodology with AI-powered analysis.*
*Report ID: {report_id} | Generated: {timestamp}*
"""
        }

    def build_report(self,
                    problem_text: str,
                    contradiction_result: Dict,
                    principle_results: List[Dict],
                    effects: List[Dict],
                    concepts: List[Dict],
                    adaptation_result: Dict) -> TRIZReport:
        """
        Build a comprehensive TRIZ analysis report.

        Args:
            problem_text: Original problem description
            contradiction_result: Results from contradiction identification
            principle_results: Results from principle selection
            effects: Scientific effects used
            concepts: Generated solution concepts
            adaptation_result: Context adaptation results

        Returns:
            Complete TRIZ report
        """
        report_id = f"HEINRICH_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Build report sections
        sections = []

        # Problem summary section
        problem_summary = self._build_problem_summary_section(problem_text, contradiction_result)
        sections.append(problem_summary)

        # Contradiction analysis section
        contradiction_section = self._build_contradiction_section(contradiction_result)
        sections.append(contradiction_section)

        # Principles section
        principles_section = self._build_principles_section(principle_results)
        sections.append(principles_section)

        # Effects section
        effects_section = self._build_effects_section(effects)
        sections.append(effects_section)

        # Concepts section
        concepts_section = self._build_concepts_section(concepts)
        sections.append(concepts_section)

        # Adaptation section
        adaptation_section = self._build_adaptation_section(adaptation_result)
        sections.append(adaptation_section)

        # Generate conclusions
        conclusions = self._generate_conclusions(contradiction_result, concepts, adaptation_result)

        # Generate next steps
        next_steps = self._generate_next_steps(adaptation_result)

        # Report metadata
        metadata = {
            "analysis_version": "1.0",
            "pipeline_steps": ["contradiction_id", "principle_selection", "effects_lookup", "concept_generation", "adaptation"],
            "total_principles_considered": len(principle_results),
            "total_effects_considered": len(effects),
            "total_concepts_generated": len(concepts),
            "adaptation_context": adaptation_result.get("context", {})
        }

        return TRIZReport(
            report_id=report_id,
            timestamp=timestamp,
            problem_summary=problem_text[:200] + "..." if len(problem_text) > 200 else problem_text,
            sections=sections,
            conclusions=conclusions,
            next_steps=next_steps,
            metadata=metadata
        )

    def _build_problem_summary_section(self, problem_text: str, contradiction_result: Dict) -> ReportSection:
        """Build the problem summary section."""
        # Extract context from contradiction result if available
        system = "Not specified"
        improvement = "Not specified"
        constraints = "Not specified"

        if "context" in contradiction_result:
            ctx = contradiction_result["context"]
            system = ctx.get("technical_system", system)
            improvement = ctx.get("desired_improvement", improvement)
            constraints = ctx.get("constraints", constraints)

        content = f"""**Original Problem:**
{problem_text}

**Technical System:** {system}
**Desired Improvement:** {improvement}
**Key Constraints:** {constraints}

**Problem Classification:** Technical contradiction identified and analyzed using TRIZ methodology."""

        return ReportSection(
            title="Problem Analysis",
            content=content,
            section_type="analysis",
            importance="high"
        )

    def _build_contradiction_section(self, contradiction_result: Dict) -> ReportSection:
        """Build the contradiction analysis section."""
        primary = contradiction_result.get("primary_contradiction", {})

        if not primary:
            content = "No clear technical contradiction identified."
        else:
            content = f"""**Primary Contradiction:**
- **Improving Parameter:** {primary.get('improving_parameter_name', 'Unknown')}
- **Worsening Parameter:** {primary.get('worsening_parameter_name', 'Unknown')}
- **Confidence Score:** {primary.get('confidence_score', 0):.2f}

**Analysis Reasoning:**
{primary.get('reasoning', 'Systematic TRIZ analysis performed.')}

**Alternative Contradictions:**
{len(contradiction_result.get('alternative_contradictions', []))} additional contradictions identified for consideration."""

        return ReportSection(
            title="Technical Contradiction Analysis",
            content=content,
            section_type="analysis",
            importance="high"
        )

    def _build_principles_section(self, principle_results: List[Dict]) -> ReportSection:
        """Build the TRIZ principles section."""
        if not principle_results:
            content = "No principle recommendations generated."
        else:
            content = ""

            for i, result in enumerate(principle_results):
                content += f"""### Principle Set {i+1}

**Primary Principles:**
{self._format_principles(result.get('primary_principles', []))}

**Supporting Principles:**
{self._format_principles(result.get('supporting_principles', []))}

**Source:** {result.get('matrix_source', 'TRIZ methodology')}

"""

        return ReportSection(
            title="Recommended TRIZ Principles",
            content=content,
            section_type="recommendation",
            importance="high"
        )

    def _build_effects_section(self, effects: List[Dict]) -> ReportSection:
        """Build the scientific effects section."""
        if not effects:
            content = "No scientific effects identified for this solution."
        else:
            content = ""

            for i, effect in enumerate(effects[:5]):  # Limit to top 5 effects
                content += f"""**{effect['name']}**
- **Category:** {effect['category']}
- **Relevance:** {effect.get('relevance_score', 0):.2f}
- **Applications:** {', '.join(effect['applications'][:2])}
- **Related Principles:** {', '.join([f'#{pid}' for pid in effect.get('related_principles', [])[:3]])}

"""

        return ReportSection(
            title="Scientific Effects Integration",
            content=content,
            section_type="analysis",
            importance="medium"
        )

    def _build_concepts_section(self, concepts: List[Dict]) -> ReportSection:
        """Build the solution concepts section."""
        if not concepts:
            content = "No solution concepts generated."
        else:
            content = ""

            for i, concept in enumerate(concepts[:3]):  # Limit to top 3 concepts
                content += f"""### {concept['title']}

**Concept ID:** {concept['concept_id']}
**Innovation Level:** {concept.get('innovation_level', 'Not assessed')}
**Complexity:** {concept.get('estimated_complexity', 'Not assessed')}

**Description:**
{concept['description']}

**Key Advantages:**
{self._format_list(concept.get('advantages', []))}

**Implementation Steps:**
{self._format_list(concept.get('implementation_steps', []))}

**Applicable Domains:** {', '.join(concept.get('domain_applications', []))}

"""

        return ReportSection(
            title="Solution Concepts",
            content=content,
            section_type="recommendation",
            importance="high"
        )

    def _build_adaptation_section(self, adaptation_result: Dict) -> ReportSection:
        """Build the adaptation section."""
        context = adaptation_result.get("context", {})
        adapted_concepts = adaptation_result.get("adapted_concepts", [])

        content = f"""**Adaptation Context:**
- **Industry:** {context.get('industry', 'Not specified')}
- **Company Size:** {context.get('company_size', 'Not specified')}
- **Budget Level:** {context.get('budget_level', 'Not specified')}
- **Timeline:** {context.get('timeline', 'Not specified')}
- **Technical Expertise:** {context.get('technical_expertise', 'Not specified')}

"""

        if adapted_concepts:
            content += "**Adapted Concepts:**
"
            for concept in adapted_concepts:
                content += f"""**{concept['adapted_title']}**
- **Confidence:** {concept.get('adaptation_confidence', 0):.2f}
- **Key Modifications:** {', '.join(concept.get('contextual_modifications', [])[:3])}
- **Resource Requirements:** {concept.get('resource_requirements', {}).get('financial', 'Not assessed')}

"""

        return ReportSection(
            title="Context-Adapted Solutions",
            content=content,
            section_type="implementation",
            importance="medium"
        )

    def _format_principles(self, principles: List[Dict]) -> str:
        """Format principles list for display."""
        if not principles:
            return "None identified"

        formatted = []
        for principle in principles:
            formatted.append(f"• **Principle {principle['principle_id']}**: {principle['principle_name']} (Score: {principle.get('relevance_score', 0):.2f})")

        return "\n".join(formatted)

    def _format_list(self, items: List[str]) -> str:
        """Format a list for display."""
        if not items:
            return "Not specified"

        formatted = []
        for item in items:
            formatted.append(f"• {item}")

        return "\n".join(formatted)

    def _generate_conclusions(self, contradiction_result: Dict, concepts: List[Dict], adaptation_result: Dict) -> List[str]:
        """Generate report conclusions."""
        conclusions = []

        # Contradiction-based conclusions
        primary = contradiction_result.get("primary_contradiction")
        if primary:
            conclusions.append(
                f"The primary technical contradiction between {primary.get('improving_parameter_name', 'improvement')} "
                f"and {primary.get('worsening_parameter_name', 'constraint')} has been systematically addressed."
            )

        # Concept-based conclusions
        if concepts:
            innovation_levels = [c.get('innovation_level', 'Incremental') for c in concepts]
            breakthrough_count = sum(1 for level in innovation_levels if level == 'Breakthrough')

            if breakthrough_count > 0:
                conclusions.append(
                    f"Generated {breakthrough_count} breakthrough concepts with high innovation potential."
                )
            else:
                conclusions.append(
                    "Generated practical solution concepts with immediate applicability."
                )

        # Adaptation-based conclusions
        recommended = adaptation_result.get("recommended_concept")
        if recommended:
            conclusions.append(
                f"Recommended concept '{recommended.get('adapted_title', 'N/A')}' "
                f"with {recommended.get('adaptation_confidence', 0):.1%} adaptation confidence."
            )

        # General conclusions
        conclusions.extend([
            "TRIZ methodology provides systematic approach to inventive problem solving.",
            "Scientific effects integration enhances solution creativity and feasibility.",
            "Context adaptation ensures practical implementation within constraints."
        ])

        return conclusions

    def _generate_next_steps(self, adaptation_result: Dict) -> List[str]:
        """Generate recommended next steps."""
        next_steps = [
            "1. Review the recommended solution concept in detail",
            "2. Assess resource requirements and timeline feasibility",
            "3. Develop detailed implementation plan with milestones",
            "4. Create prototype or pilot program",
            "5. Test and validate the solution in real-world conditions",
            "6. Monitor performance and iterate as needed"
        ]

        # Context-specific next steps
        context = adaptation_result.get("context", {})
        if context.get("timeline") == "short":
            next_steps.insert(1, "• Prioritize quick wins and immediate benefits")
        if context.get("budget_level") == "low":
            next_steps.insert(1, "• Focus on cost-effective implementation options")

        return next_steps

    def export_report(self, report: TRIZReport, format_type: str = "markdown") -> str:
        """
        Export report in specified format.

        Args:
            report: TRIZ report to export
            format_type: Export format ("markdown", "json", "html")

        Returns:
            Formatted report string
        """
        if format_type == "json":
            return self._export_json(report)
        elif format_type == "html":
            return self._export_html(report)
        else:
            return self._export_markdown(report)

    def _export_markdown(self, report: TRIZReport) -> str:
        """Export report in Markdown format."""
        content = self.report_templates["header"].format(
            report_id=report.report_id,
            timestamp=report.timestamp
        )

        content += self.report_templates["problem_summary"].format(
            problem_text=report.problem_summary,
            system="Not specified",
            improvement="Not specified",
            constraints="Not specified"
        )

        # Add all sections
        for section in report.sections:
            content += f"## {section.title}\n\n{section.content}\n\n"

        content += self.report_templates["conclusions"].format(
            conclusions_list="\n".join(f"• {c}" for c in report.conclusions)
        )

        content += self.report_templates["next_steps"].format(
            next_steps_list="\n".join(report.next_steps),
            report_id=report.report_id,
            timestamp=report.timestamp
        )

        return content

    def _export_json(self, report: TRIZReport) -> str:
        """Export report in JSON format."""
        report_dict = asdict(report)
        report_dict["export_format"] = "json"
        report_dict["export_timestamp"] = datetime.now().isoformat()

        return json.dumps(report_dict, indent=2, ensure_ascii=False)

    def _export_html(self, report: TRIZReport) -> str:
        """Export report in HTML format."""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heinrich TRIZ Report - {report.report_id}</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 40px; }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; }}
        .section {{ margin-bottom: 30px; padding: 20px; background: #f9f9f9; border-radius: 8px; }}
        .section-high {{ border-left: 5px solid #ff6b6b; }}
        .section-medium {{ border-left: 5px solid #ffd93d; }}
        .section-low {{ border-left: 5px solid #6bcf7f; }}
        h1 {{ margin: 0; font-size: 2.5em; }}
        h2 {{ color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px; }}
        .metadata {{ background: #e3f2fd; padding: 15px; border-radius: 5px; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Heinrich TRIZ Analysis Report</h1>
        <p><strong>Report ID:</strong> {report.report_id}</p>
        <p><strong>Generated:</strong> {report.timestamp}</p>
    </div>

"""

        # Add sections
        for section in report.sections:
            importance_class = f"section-{section.importance}"
            html += f"""    <div class="section {importance_class}">
        <h2>{section.title}</h2>
        <div>{section.content.replace(chr(10), '<br>')}</div>
    </div>

"""

        html += """    <div class="metadata">
        <h3>Report Metadata</h3>
        <pre>{json.dumps(report.metadata, indent=2)}</pre>
    </div>
</body>
</html>"""

        return html
