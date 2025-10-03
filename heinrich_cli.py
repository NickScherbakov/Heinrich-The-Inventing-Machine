#!/usr/bin/env python3
"""
Heinrich TRIZ Engine - Command Line Interface
Interactive CLI for TRIZ-based inventive problem solving.
"""

import argparse
import sys
import json
from pathlib import Path
from typing import Dict, Any

# Import Heinrich modules
from heinrich.pipelines.problem_parser import ProblemParser, ParsedProblem
from heinrich.pipelines.contradiction_identifier import ContradictionIdentifier, ContradictionResult
from heinrich.pipelines.principle_selector import PrincipleSelector, PrincipleSelectionResult
from heinrich.pipelines.effects_lookup import EffectsLookup, EffectRecommendation
from heinrich.pipelines.concept_generator import ConceptGenerator, ConceptGenerationResult
from heinrich.pipelines.adaptation_planner import AdaptationPlanner, AdaptationContext, AdaptationResult
from heinrich.pipelines.report_builder import ReportBuilder, TRIZReport
from heinrich.agents.persona_manager import PersonaManager

class HeinrichCLI:
    """Command-line interface for the Heinrich TRIZ Engine."""

    def __init__(self):
        """Initialize the CLI with all necessary components."""
        self.persona_manager = PersonaManager()
        self.problem_parser = ProblemParser()
        self.contradiction_identifier = ContradictionIdentifier()
        self.principle_selector = PrincipleSelector()
        self.effects_lookup = EffectsLookup()
        self.concept_generator = ConceptGenerator()
        self.adaptation_planner = AdaptationPlanner()
        self.report_builder = ReportBuilder()

        # Interactive mode state
        self.current_problem: str = ""
        self.parsed_problem: Optional[ParsedProblem] = None
        self.contradiction_result: Optional[ContradictionResult] = None
        self.principle_results: List[PrincipleSelectionResult] = []
        self.effects: List[EffectRecommendation] = []
        self.concepts: List[Dict] = []
        self.adaptation_result: Optional[AdaptationResult] = None

    def print_header(self):
        """Print the Heinrich CLI header."""
        print("🚀" + "="*70 + "🚀")
        print("           Heinrich: The Inventing Machine")
        print("   AI-Powered TRIZ Methodology for Systematic Innovation")
        print("="*72)
        print(f"Version 0.1.0 | Inspired by Genrich Altshuller's TRIZ")
        print("="*72 + "\n")

    def print_persona_greeting(self):
        """Print Heinrich's greeting."""
        print("🤖 " + self.persona_manager.get_greeting())
        print()

    def get_user_input(self, prompt: str) -> str:
        """Get input from user with prompt."""
        try:
            return input(prompt).strip()
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Remember: systematic thinking leads to breakthrough innovations.")
            sys.exit(0)

    def run_interactive_mode(self):
        """Run the interactive problem-solving mode."""
        self.print_header()
        self.print_persona_greeting()

        print("🎯 Interactive TRIZ Problem-Solving Session")
        print("="*50)

        # Step 1: Problem Input
        self.step_problem_input()

        # Step 2: Problem Analysis
        self.step_problem_analysis()

        # Step 3: Contradiction Identification
        self.step_contradiction_identification()

        # Step 4: Principle Selection
        self.step_principle_selection()

        # Step 5: Effects Integration
        self.step_effects_integration()

        # Step 6: Concept Generation
        self.step_concept_generation()

        # Step 7: Context Adaptation
        self.step_context_adaptation()

        # Step 8: Report Generation
        self.step_report_generation()

        print("\n🎉 Analysis complete! Check your generated report for detailed results.")
        print("💡 Remember: The best solutions come from systematic thinking, not random ideas.")

    def step_problem_input(self):
        """Step 1: Get problem description from user."""
        print("\n📝 STEP 1: Problem Description")
        print("-" * 40)

        print("Please describe your technical problem or challenge.")
        print("Be specific about:")
        print("• What system or product you're working with")
        print("• What you want to improve")
        print("• What constraints or limitations you're facing")
        print()

        while True:
            problem_text = self.get_user_input("Your problem: ")

            if len(problem_text.strip()) < 20:
                print("❌ Please provide a more detailed problem description (at least 20 characters).")
                continue

            if not any(keyword in problem_text.lower() for keyword in
                      ["improve", "increase", "decrease", "better", "faster", "problem", "issue", "challenge"]):
                print("❌ Please describe a technical problem or improvement goal.")
                continue

            break

        self.current_problem = problem_text
        print(f"\n✅ Problem received: {len(problem_text)} characters")
        print(f"📋 Summary: {problem_text[:100]}{'...' if len(problem_text) > 100 else ''}")

    def step_problem_analysis(self):
        """Step 2: Analyze and parse the problem."""
        print("\n🔍 STEP 2: Problem Analysis")
        print("-" * 40)

        print("🤖 Analyzing your problem using TRIZ methodology...")
        self.parsed_problem = self.problem_parser.parse(self.current_problem)

        print("✅ Analysis complete!")
        print(f"📊 Technical System: {self.parsed_problem.technical_system or 'Not identified'}")
        print(f"🎯 Desired Improvement: {self.parsed_problem.desired_improvement or 'Not identified'}")
        print(f"⚠️  Constraints: {len(self.parsed_problem.constraints)} identified")

    def step_contradiction_identification(self):
        """Step 3: Identify technical contradictions."""
        print("\n🎭 STEP 3: Contradiction Identification")
        print("-" * 40)

        print("🤖 Identifying technical contradictions using 39 TRIZ parameters...")
        self.contradiction_result = self.contradiction_identifier.identify_contradiction(self.current_problem)

        print("✅ Contradiction analysis complete!")

        if self.contradiction_result.primary_contradiction:
            primary = self.contradiction_result.primary_contradiction
            print(f"🎯 Primary Contradiction: {primary.improving_parameter_name} vs {primary.worsening_parameter_name}")
            print(f"📊 Confidence: {primary.confidence_score:.1%}")
            print(f"💡 Reasoning: {primary.reasoning}")

            if self.contradiction_result.alternative_contradictions:
                print(f"🔄 {len(self.contradiction_result.alternative_contradictions)} alternative contradictions identified")
        else:
            print("⚠️  No clear technical contradiction identified. Proceeding with general analysis.")

    def step_principle_selection(self):
        """Step 4: Select relevant TRIZ principles."""
        print("\n⚡ STEP 4: TRIZ Principle Selection")
        print("-" * 40)

        if self.contradiction_result.primary_contradiction:
            print("🤖 Selecting principles from the 40 TRIZ inventive principles...")
            primary = self.contradiction_result.primary_contradiction

            result = self.principle_selector.select_principles(
                primary.improving_parameter,
                primary.worsening_parameter
            )
            self.principle_results = [result]

            print("✅ Principle selection complete!")
            print(f"📚 Primary Principles: {len(result.primary_principles)}")
            print(f"🔧 Supporting Principles: {len(result.supporting_principles)}")

            # Show top principles
            for principle in result.primary_principles[:3]:
                print(f"  • Principle {principle.principle_id}: {principle.principle_name}")
        else:
            print("⚠️  No primary contradiction available. Using general principle selection.")
            # Could implement fallback logic here

    def step_effects_integration(self):
        """Step 5: Integrate scientific effects."""
        print("\n🔬 STEP 5: Scientific Effects Integration")
        print("-" * 40)

        print("🤖 Finding relevant scientific effects and technical knowledge...")

        # Get domain keywords from problem
        domain_keywords = self._extract_domain_keywords(self.current_problem)

        if self.contradiction_result.primary_contradiction:
            primary = self.contradiction_result.primary_contradiction
            self.effects = self.effects_lookup.find_effects_for_contradiction(
                primary.improving_parameter,
                primary.worsening_parameter,
                domain_keywords
            )

            print("✅ Effects analysis complete!")
            print(f"🔍 Found {len(self.effects)} relevant scientific effects")

            # Show top effects
            for effect in self.effects[:3]:
                print(f"  • {effect.effect.name} (Relevance: {effect.relevance_score:.1%})")
        else:
            print("⚠️  No primary contradiction available. Using general effects lookup.")
            # Could implement fallback logic here

    def step_concept_generation(self):
        """Step 6: Generate solution concepts."""
        print("\n💡 STEP 6: Solution Concept Generation")
        print("-" * 40)

        print("🤖 Generating concrete solution concepts...")

        if self.principle_results and self.effects:
            # Convert principle results to the format expected by concept generator
            principles_data = []
            for result in self.principle_results:
                for principle in result.primary_principles + result.supporting_principles:
                    principles_data.append({
                        'id': principle.principle_id,
                        'name': principle.principle_name,
                        'description': principle.principle_description
                    })

            # Convert effects to the format expected by concept generator
            effects_data = []
            for effect in self.effects[:5]:  # Limit to top 5 effects
                effects_data.append({
                    'id': effect.effect.id,
                    'name': effect.effect.name,
                    'category': effect.effect.category,
                    'technical_domains': effect.effect.technical_domains,
                    'applications': effect.effect.applications
                })

            # Generate concepts
            generation_result = self.concept_generator.generate_concepts(
                principles_data,
                effects_data,
                {"technical_system": self.parsed_problem.technical_system if self.parsed_problem else "Unknown"}
            )

            self.concepts = []
            for concept in generation_result.concepts:
                self.concepts.append({
                    'concept_id': concept.concept_id,
                    'title': concept.title,
                    'description': concept.description,
                    'principles_used': concept.principles_used,
                    'effects_used': concept.effects_used,
                    'advantages': concept.advantages,
                    'implementation_steps': concept.implementation_steps,
                    'estimated_complexity': concept.estimated_complexity,
                    'innovation_level': concept.innovation_level,
                    'domain_applications': concept.domain_applications
                })

            print("✅ Concept generation complete!")
            print(f"🚀 Generated {len(self.concepts)} solution concepts")

            # Show top concepts
            for concept in self.concepts[:2]:
                print(f"  • {concept['title']} ({concept['innovation_level']} innovation)")
        else:
            print("⚠️  Insufficient data for concept generation. Need principles and effects.")

    def step_context_adaptation(self):
        """Step 7: Adapt solutions to context."""
        print("\n🎯 STEP 7: Context Adaptation")
        print("-" * 40)

        print("📋 Gathering context information for solution adaptation...")

        # Collect context information
        context = self._collect_adaptation_context()

        if self.concepts:
            print("🤖 Adapting concepts to your specific context...")

            # Convert concepts to format expected by adaptation planner
            concepts_data = []
            for concept in self.concepts:
                concepts_data.append({
                    'concept_id': concept['concept_id'],
                    'title': concept['title'],
                    'description': concept['description'],
                    'estimated_complexity': concept['estimated_complexity'],
                    'innovation_level': concept['innovation_level']
                })

            adaptation_result = self.adaptation_planner.adapt_concepts(
                concepts_data[:3],  # Limit to top 3 concepts
                context,
                num_adaptations=2
            )

            self.adaptation_result = adaptation_result

            print("✅ Context adaptation complete!")
            print(f"📊 {len(adaptation_result.adapted_concepts)} concepts adapted")

            if adaptation_result.recommended_concept:
                rec = adaptation_result.recommended_concept
                print(f"🏆 Recommended: {rec.adapted_title}")
                print(f"   Confidence: {rec.adaptation_confidence:.1%}")
        else:
            print("⚠️  No concepts available for adaptation.")

    def step_report_generation(self):
        """Step 8: Generate comprehensive report."""
        print("\n📄 STEP 8: Report Generation")
        print("-" * 40)

        print("🤖 Generating comprehensive TRIZ analysis report...")

        if (self.contradiction_result and self.principle_results and
            self.effects and self.concepts and self.adaptation_result):

            # Generate the report
            report = self.report_builder.build_report(
                self.current_problem,
                {"primary_contradiction": self.contradiction_result.primary_contradiction},
                [result.__dict__ for result in self.principle_results],
                [effect.__dict__ for effect in self.effects],
                self.concepts,
                self.adaptation_result.__dict__
            )

            # Save report to file
            report_filename = f"heinrich_report_{report.report_id}.md"
            with open(report_filename, 'w', encoding='utf-8') as f:
                f.write(self.report_builder.export_report(report, "markdown"))

            print("✅ Report generated successfully!"            print(f"📄 Saved as: {report_filename}")
            print(f"🆔 Report ID: {report.report_id}")

            # Show report summary
            print("
📋 Report Summary:"            print(f"   • {len(report.sections)} analysis sections")
            print(f"   • {len(report.conclusions)} key conclusions")
            print(f"   • {len(report.next_steps)} recommended next steps")

        else:
            print("⚠️  Insufficient data for report generation.")

    def _extract_domain_keywords(self, problem_text: str) -> List[str]:
        """Extract domain-specific keywords from problem text."""
        keywords = []

        # Common domain keywords
        domain_patterns = {
            "automotive": ["car", "vehicle", "engine", "transmission", "brake", "suspension"],
            "aerospace": ["aircraft", "plane", "wing", "fuselage", "propulsion", "altitude"],
            "medical": ["patient", "treatment", "diagnosis", "surgery", "implant", "therapy"],
            "manufacturing": ["production", "assembly", "quality", "efficiency", "automation"],
            "energy": ["power", "efficiency", "consumption", "renewable", "battery", "solar"],
            "electronics": ["circuit", "signal", "processor", "memory", "display", "sensor"]
        }

        text_lower = problem_text.lower()

        for domain, patterns in domain_patterns.items():
            if any(pattern in text_lower for pattern in patterns):
                keywords.append(domain)
                keywords.extend(patterns[:2])  # Add top 2 matching patterns

        return keywords[:5]  # Limit to 5 keywords

    def _collect_adaptation_context(self) -> AdaptationContext:
        """Collect context information for adaptation."""
        print("\n📋 Please provide some context for solution adaptation:")

        # Industry
        industries = ["automotive", "aerospace", "medical", "manufacturing", "energy", "electronics", "other"]
        print("\n🏭 Industry:")
        for i, industry in enumerate(industries, 1):
            print(f"  {i}. {industry.title()}")

        while True:
            choice = self.get_user_input("Select industry (1-7): ")
            try:
                industry_idx = int(choice) - 1
                if 0 <= industry_idx < len(industries):
                    industry = industries[industry_idx]
                    break
                else:
                    print("❌ Please select a valid option.")
            except ValueError:
                print("❌ Please enter a number.")

        # Company size
        print("\n🏢 Company Size:")
        sizes = ["startup", "small/medium enterprise", "large enterprise"]
        for i, size in enumerate(sizes, 1):
            print(f"  {i}. {size.title()}")

        while True:
            choice = self.get_user_input("Select company size (1-3): ")
            try:
                size_idx = int(choice) - 1
                if 0 <= size_idx < len(sizes):
                    company_size = sizes[size_idx]
                    break
                else:
                    print("❌ Please select a valid option.")
            except ValueError:
                print("❌ Please enter a number.")

        # Budget level
        print("\n💰 Budget Level:")
        budgets = ["low", "medium", "high"]
        for i, budget in enumerate(budgets, 1):
            print(f"  {i}. {budget.title()}")

        while True:
            choice = self.get_user_input("Select budget level (1-3): ")
            try:
                budget_idx = int(choice) - 1
                if 0 <= budget_idx < len(budgets):
                    budget_level = budgets[budget_idx]
                    break
                else:
                    print("❌ Please select a valid option.")
            except ValueError:
                print("❌ Please enter a number.")

        # Timeline
        print("\n⏰ Timeline:")
        timelines = ["short-term (weeks)", "medium-term (months)", "long-term (quarters)"]
        for i, timeline in enumerate(timelines, 1):
            print(f"  {i}. {timeline}")

        while True:
            choice = self.get_user_input("Select timeline (1-3): ")
            try:
                timeline_idx = int(choice) - 1
                if 0 <= timeline_idx < len(timelines):
                    timeline = timelines[timeline_idx].split()[0]  # Extract "short-term", etc.
                    break
                else:
                    print("❌ Please select a valid option.")
            except ValueError:
                print("❌ Please enter a number.")

        # Technical expertise
        print("\n🎓 Technical Expertise:")
        expertises = ["basic", "intermediate", "advanced"]
        for i, expertise in enumerate(expertises, 1):
            print(f"  {i}. {expertise.title()}")

        while True:
            choice = self.get_user_input("Select expertise level (1-3): ")
            try:
                expertise_idx = int(choice) - 1
                if 0 <= expertise_idx < len(expertises):
                    technical_expertise = expertises[expertise_idx]
                    break
                else:
                    print("❌ Please select a valid option.")
            except ValueError:
                print("❌ Please enter a number.")

        return AdaptationContext(
            industry=industry,
            company_size=company_size,
            budget_level=budget_level,
            timeline=timeline,
            technical_expertise=technical_expertise,
            risk_tolerance="moderate",  # Default value
            existing_infrastructure=[],  # Could be expanded
            regulatory_constraints=[],   # Could be expanded
            market_requirements=[]       # Could be expanded
        )

    def run_batch_mode(self, input_file: str, output_dir: str = "."):
        """Run batch processing mode."""
        print("🔄 Batch Processing Mode")
        print(f"📂 Input file: {input_file}")
        print(f"📁 Output directory: {output_dir}")

        # This would implement batch processing logic
        print("⚠️  Batch mode not yet implemented in this version.")

    def run_api_mode(self, host: str = "localhost", port: int = 8000):
        """Run API server mode."""
        print("🌐 API Server Mode")
        print(f"📡 Host: {host}")
        print(f"🔌 Port: {port}")

        # This would implement API server logic
        print("⚠️  API mode not yet implemented in this version.")

    def show_help(self):
        """Show help information."""
        print("Heinrich: The Inventing Machine - Help")
        print("="*50)
        print()
        print("DESCRIPTION:")
        print("    AI-powered TRIZ engine for systematic inventive problem solving")
        print()
        print("MODES:")
        print("    interactive  - Interactive problem-solving session")
        print("    batch       - Process multiple problems from file")
        print("    api         - Start API server for programmatic access")
        print()
        print("TRIZ METHODOLOGY:")
        print("    Uses Genrich Altshuller's 39 parameters and 40 principles")
        print("    Integrates scientific effects for concrete solutions")
        print("    Adapts solutions to specific organizational contexts")
        print()
        print("EXAMPLES:")
        print("    heinrich interactive")
        print("    heinrich batch problems.txt")
        print("    heinrich api --port 8080")

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Heinrich: AI-powered TRIZ engine for inventive problem solving",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  heinrich interactive              # Start interactive session
  heinrich batch problems.txt       # Process problems from file
  heinrich api --port 8080         # Start API server
        """
    )

    parser.add_argument(
        "mode",
        choices=["interactive", "batch", "api"],
        help="Operating mode"
    )

    parser.add_argument(
        "input",
        nargs="?",
        help="Input file (for batch mode) or host (for API mode)"
    )

    parser.add_argument(
        "-p", "--port",
        type=int,
        default=8000,
        help="Port number (for API mode)"
    )

    parser.add_argument(
        "-o", "--output",
        default=".",
        help="Output directory"
    )

    args = parser.parse_args()

    # Create CLI instance
    cli = HeinrichCLI()

    try:
        if args.mode == "interactive":
            cli.run_interactive_mode()
        elif args.mode == "batch":
            if not args.input:
                print("❌ Error: Input file required for batch mode")
                sys.exit(1)
            cli.run_batch_mode(args.input, args.output)
        elif args.mode == "api":
            cli.run_api_mode(args.input or "localhost", args.port)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
