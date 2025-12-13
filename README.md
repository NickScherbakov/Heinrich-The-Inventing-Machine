# Heinrich: The Inventing Machine

*An open-source AI system for TRIZ-based inventive problem solving with interpretable, step-by-step reasoning flow*

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TRIZ](https://img.shields.io/badge/methodology-TRIZ-green.svg)](https://en.wikipedia.org/wiki/TRIZ)

🌍 **Languages**: [English](README.md) | [中文](docs/zh/README.md) | [Русский](docs/ru/README.md) | [العربية](docs/ar/README.md)

## Overview

Heinrich is an open-source AI engine that combines classical TRIZ (Theory of Inventive Problem Solving) methodology with modern Large Language Models to provide systematic, interpretable inventive problem-solving capabilities. Named after Genrich Altshuller, the creator of TRIZ, Heinrich embodies the systematic thinking approach of the original methodology while leveraging contemporary AI advances.

### Key Features

- **Systematic TRIZ Pipeline**: 7-module workflow following classical TRIZ methodology
- **Interpretable Reasoning**: Every step is logged and traceable to TRIZ principles
- **Knowledge Base**: Complete 39 parameters, 40 principles, contradiction matrix
- **Multi-modal Support**: Text problems, technical specifications, patent analysis
- **Evaluation Suite**: Curated case base with reference solutions
- **Multilingual**: Full documentation in English, Chinese, Russian, and Arabic
- **Ethical AI**: Transparent persona with safety guidelines

## Getting Started

### Installation

#### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

#### Install from source

1. Clone the repository:
```bash
git clone https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine.git
cd Heinrich-The-Inventing-Machine
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Heinrich in development mode:
```bash
pip install -e .
```

#### Dependencies

Heinrich requires the following Python packages:
- `PyYAML>=6.0` - For TRIZ knowledge base (YAML files)
- `numpy>=1.21.0` - For numerical computations
- `dataclasses-json>=0.5.0` - For data serialization

All dependencies are automatically installed when using `pip install`.

### Usage

#### Quick Example

Here's a simple example to get started with Heinrich:

```python
from problem_parser import ProblemParser

# Create a problem parser
parser = ProblemParser()

# Analyze a problem
problem = "We need to make a car faster, but increasing engine power makes it consume more fuel."
result = parser.parse(problem)

# View the analysis
print(f"Technical System: {result.technical_system}")
print(f"Desired Improvement: {result.desired_improvement}")
print(f"Undesired Consequence: {result.undesired_consequence}")
```

**Output:**
```
Technical System: car
Desired Improvement: faster
Undesired Consequence: increasing engine power makes it consume more fuel
```

#### Run the Basic Example

Try the included basic usage example:

```bash
python3 examples/basic_usage.py
```

This demonstrates problem parsing with multiple examples.

#### Command-Line Interface

For full TRIZ pipeline analysis, use the interactive CLI:

```bash
# Interactive problem-solving session
python3 heinrich_cli.py interactive

# Batch processing (coming soon)
python3 heinrich_cli.py batch problems.txt

# API server mode (coming soon)
python3 heinrich_cli.py api --port 8080
```

The interactive mode guides you through the complete TRIZ methodology:
1. Problem description and parsing
2. Contradiction identification using 39 TRIZ parameters
3. Principle selection from 40 inventive principles
4. Scientific effects integration
5. Solution concept generation
6. Context-aware adaptation
7. Comprehensive report generation

### Example Problem Analysis

**Input**: "We need to make a car faster, but increasing engine power makes it consume more fuel."

**Heinrich Output**:
```
Step 1: Problem Analysis
- Technical system: Automotive propulsion
- Desired improvement: Speed (Parameter 9)
- Harmful consequence: Energy consumption (Parameter 19)

Step 2: Contradiction Identification
- Physical contradiction: Engine must be powerful AND energy-efficient
- Technical contradiction: Speed vs Energy consumption

Step 3: Principle Selection
- Principle 15: Dynamics (variable characteristics)
- Principle 2: Taking out (separate conflicting properties)
- Principle 35: Parameter change (different states/properties)

Step 4: Solution Concepts
1. Variable compression ratio engine (Principle 15)
2. Hybrid powertrain with mode switching (Principle 2)
3. Active aerodynamics adaptation (Principle 35)
...
```

## Architecture

Heinrich implements a modular, interpretable TRIZ reasoning pipeline:

```
Problem Input
     ↓
[Problem Parser] → Normalized problem description
     ↓
[Contradiction Identifier] → Technical/Physical contradictions
     ↓
[Principle Selector] → Relevant TRIZ principles (1-40)
     ↓
[Effects Lookup] → Scientific effects and evolution patterns
     ↓
[Concept Generator] → Solution concepts with reasoning
     ↓
[Adaptation Planner] → Context-aware recommendations
     ↓
[Report Builder] → Structured solution report
```

## Core Modules

- **Problem Parser**: Extracts essence from unstructured problem descriptions
- **Contradiction Identifier**: Maps to 39 TRIZ parameters and identifies contradictions
- **Principle Selector**: Selects relevant principles from contradiction matrix
- **Effects Lookup**: References scientific effects and evolution patterns
- **Concept Generator**: Creates solution concepts with TRIZ traceability
- **Adaptation Planner**: Contextualizes solutions for real-world constraints
- **Report Builder**: Generates structured, traceable solution reports

## The Heinrich Persona

Heinrich operates as an AI mentor inspired by Genrich Altshuller's methodical thinking style. This persona:

- Follows systematic TRIZ methodology rigorously
- Provides educational explanations for each step
- Maintains ethical boundaries and transparency
- **Important**: This is an AI system inspired by TRIZ principles, not a simulation of the real person

## Knowledge Base

Heinrich includes comprehensive TRIZ knowledge:

- **39 Technical Parameters**: Complete parameter definitions and relationships
- **40 Inventive Principles**: Detailed principles with sub-principles and examples
- **Contradiction Matrix**: 39×39 matrix mapping contradictions to principles
- **Scientific Effects Database**: Physics, chemistry, and biological effects
- **Evolution Patterns**: 8 patterns of technical system evolution
- **Case Base**: Curated educational cases with reference solutions

## Evaluation and Quality

Heinrich includes rigorous evaluation capabilities:

- **Case-based Testing**: Validated against classical TRIZ educational cases
- **Consistency Metrics**: Measures contradiction identification accuracy
- **Completeness Metrics**: Evaluates principle coverage and reasoning depth
- **Expert Review**: Structured templates for TRIZ expert evaluation
- **Comparative Analysis**: Benchmarks against other AI problem-solving approaches

## Multilingual Support

Full documentation and interface support for **4 languages**:

- **English (en)**: Primary development language
- **中文 Chinese (zh)**: Complete translation with technical terminology
- **Русский Russian (ru)**: Complete translation honoring TRIZ origins
- **العربية Arabic (ar)**: NEW - Complete translation for Arabic-speaking innovators

All translations include:
- ✅ TRIZ terminology glossaries (30+ terms each)
- ✅ Complete documentation structure
- ✅ RTL (Right-to-Left) support for Arabic
- ✅ Automated translation synchronization workflows

See [i18n/README.md](i18n/README.md) for translation guidelines and contribution workflow.

## AI Integration via MCP

Heinrich supports seamless AI-assisted workflows through the **GitHub MCP (Model Context Protocol) Server**. This integration enables AI assistants to directly interact with the repository, eliminating the need for manual copy-pasting and creating a true bridge between human intention and AI execution.

### What is MCP?

MCP (Model Context Protocol) is an open standard that provides AI assistants with standardized access to external tools and services. With MCP integration, AI can:

- 🤖 Comment on issues and pull requests directly
- 🌿 Create and manage branches
- 🔍 Search code and issues
- 📝 Update repository metadata
- 👥 Manage collaborators and reviews
- And much more!

### Getting Started with MCP

We offer two setup options:

1. **Hosted MCP Server** (Recommended) - Uses GitHub's official endpoint with OAuth authentication
2. **Local Docker MCP Server** - Self-hosted for more control and customization

For detailed setup instructions, see our comprehensive guide:

📖 **[MCP Integration Guide](docs/mcp-integration.md)**

### Quick Setup (Hosted)

1. Create a `.mcp.json` configuration file (see `.mcp.json.example`)
2. Authorize via GitHub OAuth when prompted by your AI assistant
3. Start using AI-assisted workflows immediately!

### Why MCP for Heinrich?

This integration aligns perfectly with Heinrich's mission of automation and improving creative processes. MCP creates a seamless workflow where:

- AI becomes a true collaborator in the development process
- Friction is removed from repetitive tasks
- You focus on creative problem-solving while AI handles execution
- The system learns and adapts to your workflow

*"Heinrich + MCP: Where systematic invention meets seamless AI collaboration"* 🤝

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Code style and testing requirements
- Documentation standards for all three languages
- Translation workflow and terminology management
- Issue templates and PR guidelines

## Research and Citations

If you use Heinrich in your research, please cite:

```bibtex
@software{heinrich_triz_2025,
  title={Heinrich: The Inventing Machine - Open Source TRIZ AI Engine},
  author={Heinrich Development Team},
  year={2025},
  url={https://github.com/your-org/heinrich},
  license={Apache-2.0}
}
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Genrich Altshuller and the TRIZ community for the foundational methodology
- Open source TRIZ databases and educational materials
- Contributors and maintainers of this project
- The broader AI and problem-solving research communities

## Roadmap

- **v0.1** (November 2025): Core pipeline with CLI interface
- **v0.5** (January 2026): Complete knowledge base and evaluation suite
- **v1.0** (March 2026): Production-ready with full multilingual support
- **v1.5** (June 2026): Advanced agent orchestration and plugin system

---

**Heinrich - Where systematic invention meets artificial intelligence** 🚀

*"The best problems are those that seem impossible to solve... until you find the right principle." - Inspired by TRIZ methodology*