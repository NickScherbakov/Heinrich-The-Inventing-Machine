#!/usr/bin/env python3
"""
Heinrich: Basic Usage Example
Demonstrates how to use the Heinrich TRIZ Engine to solve a simple problem.
"""

from problem_parser import ProblemParser

def main():
    """Run a simple Heinrich TRIZ analysis."""
    
    print("=" * 70)
    print("Heinrich: The Inventing Machine - Basic Usage Example")
    print("=" * 70)
    print()
    
    # Create a problem parser instance
    parser = ProblemParser()
    
    # Example problem: A classic TRIZ challenge
    problem_text = """
    We need to make a car faster, but increasing engine power makes it 
    consume more fuel.
    """
    
    print("Problem:")
    print(problem_text.strip())
    print()
    print("-" * 70)
    print()
    
    # Parse the problem
    print("Analyzing problem using TRIZ methodology...")
    parsed_problem = parser.parse(problem_text)
    
    # Display the analysis results
    print("✅ Analysis Complete!")
    print()
    print("Results:")
    print(f"  • Technical System: {parsed_problem.technical_system or 'Not identified'}")
    print(f"  • Desired Improvement: {parsed_problem.desired_improvement or 'Not identified'}")
    print(f"  • Undesired Consequence: {parsed_problem.undesired_consequence or 'Not identified'}")
    print(f"  • Constraints Found: {len(parsed_problem.constraints)}")
    print(f"  • Domain Context: {parsed_problem.context.get('domain', 'general')}")
    print()
    print("-" * 70)
    print()
    
    # Additional examples
    print("More Examples:")
    print()
    
    examples = [
        "Make the machine stronger but not heavier",
        "Improve product quality without increasing manufacturing time",
        "Increase battery capacity without making it bigger"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"{i}. Problem: {example}")
        result = parser.parse(example)
        print(f"   → System: {result.technical_system or 'general'}, "
              f"Goal: {result.desired_improvement or 'optimize'}")
        print()
    
    print("=" * 70)
    print("💡 Next Steps:")
    print("  • Use heinrich_cli.py for full TRIZ pipeline analysis")
    print("  • Explore contradiction identification and principle selection")
    print("  • Generate concrete solution concepts with scientific effects")
    print("=" * 70)

if __name__ == "__main__":
    main()
