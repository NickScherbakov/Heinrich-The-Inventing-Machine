# Heinrich: The Inventing Machine - Project Structure

This document outlines the complete project structure for Heinrich, the open-source TRIZ AI engine.

## Repository Structure

```
heinrich/
├── README.md                           # Main project README (English)
├── LICENSE                            # Apache 2.0 License
├── CONTRIBUTING.md                    # Contribution guidelines
├── CODE_OF_CONDUCT.md                # Code of conduct
├── SECURITY.md                       # Security policy
├── .gitignore                        # Git ignore rules
├── .pre-commit-config.yaml           # Code quality hooks
├── setup.py                          # Package setup
├── requirements.txt                  # Core dependencies
├── requirements-dev.txt              # Development dependencies
├── pyproject.toml                    # Modern Python project config
│
├── docs/                             # Documentation
│   ├── en/                          # English documentation (canonical)
│   │   ├── README.md
│   │   ├── triz-basics.md
│   │   ├── architecture.md
│   │   ├── ariz-flow.md
│   │   ├── evaluation.md
│   │   └── ethics.md
│   ├── zh/                          # Chinese documentation
│   │   ├── README.md
│   │   ├── triz-basics.md
│   │   └── ...
│   ├── ru/                          # Russian documentation
│   │   ├── README.md
│   │   ├── triz-basics.md
│   │   └── ...
│   └── shared/                      # Language-agnostic assets
│       ├── images/
│       ├── diagrams/
│       └── examples/
│
├── heinrich/                        # Main Python package
│   ├── __init__.py
│   ├── version.py
│   │
│   ├── pipelines/                   # TRIZ reasoning pipeline modules
│   │   ├── __init__.py
│   │   ├── problem_parser.py        # Step 1: Problem extraction & normalization
│   │   ├── contradiction_identifier.py  # Step 2: Map to 39 parameters
│   │   ├── principle_selector.py    # Step 3: Select from 40 principles
│   │   ├── effects_lookup.py        # Step 4: Scientific effects database
│   │   ├── concept_generator.py     # Step 5: Solution concept generation
│   │   ├── adaptation_planner.py    # Step 6: Context adaptation
│   │   └── report_builder.py        # Step 7: Structured output
│   │
│   ├── knowledge/                   # TRIZ knowledge base
│   │   ├── __init__.py
│   │   ├── 39_parameters.yaml       # Complete parameter definitions
│   │   ├── contradiction_matrix.csv # 39x39 contradiction matrix
│   │   ├── 40_principles.yaml       # Complete principle definitions
│   │   ├── effects_database.json    # Scientific effects & patterns
│   │   ├── evolution_patterns.yaml  # 8 evolution patterns
│   │   └── knowledge_loader.py      # Knowledge base access layer
│   │
│   ├── agents/                      # Agent orchestration system
│   │   ├── __init__.py
│   │   ├── orchestrator.py         # FSM/workflow coordinator
│   │   ├── tool_registry.py        # Tool/service registry
│   │   ├── conversation_manager.py # Multi-turn conversation handling
│   │   └── persona_manager.py      # Heinrich persona implementation
│   │
│   ├── llm/                        # LLM integration layer
│   │   ├── __init__.py
│   │   ├── prompts/                # Prompt templates
│   │   │   ├── system_prompts/     # System-level prompts
│   │   │   │   ├── heinrich_persona.txt
│   │   │   │   ├── analyst_mode.txt
│   │   │   │   └── evaluator_mode.txt
│   │   │   └── step_prompts/       # Module-specific prompts
│   │   │       ├── problem_parsing.txt
│   │   │       ├── contradiction_id.txt
│   │   │       ├── principle_selection.txt
│   │   │       └── ...
│   │   ├── adapters/               # LLM provider adapters
│   │   │   ├── __init__.py
│   │   │   ├── openai.py
│   │   │   ├── anthropic.py
│   │   │   ├── ollama.py
│   │   │   └── vllm.py
│   │   └── guards/                 # Safety and policy filters
│   │       ├── __init__.py
│   │       ├── policy_filters.py
│   │       ├── safety_checker.py
│   │       └── ethics_validator.py
│   │
│   ├── evaluation/                 # Evaluation and testing framework
│   │   ├── __init__.py
│   │   ├── case_base/             # Curated TRIZ test cases
│   │   │   ├── automotive/
│   │   │   ├── manufacturing/
│   │   │   ├── software/
│   │   │   └── general/
│   │   ├── scripts/               # Evaluation scripts
│   │   │   ├── run_benchmarks.py
│   │   │   ├── case_validator.py
│   │   │   └── metrics_calculator.py
│   │   ├── results/               # Benchmark results
│   │   └── metrics/               # Evaluation metrics
│   │       ├── contradiction_accuracy.py
│   │       ├── principle_relevance.py
│   │       └── solution_quality.py
│   │
│   ├── cli/                       # Command-line interface
│   │   ├── __init__.py
│   │   ├── heinrich_cli.py        # Main CLI entry point
│   │   ├── commands/              # CLI command modules
│   │   │   ├── solve.py
│   │   │   ├── interactive.py
│   │   │   ├── batch.py
│   │   │   └── evaluate.py
│   │   └── utils/
│   │       ├── output_formatter.py
│   │       └── config_manager.py
│   │
│   ├── api/                       # REST API (optional)
│   │   ├── __init__.py
│   │   ├── server.py
│   │   ├── routes/
│   │   │   ├── solve.py
│   │   │   ├── knowledge.py
│   │   │   └── health.py
│   │   └── models/
│   │       ├── requests.py
│   │       └── responses.py
│   │
│   └── utils/                     # Shared utilities
│       ├── __init__.py
│       ├── logging_config.py
│       ├── config_loader.py
│       ├── data_validation.py
│       └── file_utils.py
│
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── conftest.py               # Pytest configuration
│   ├── unit/                     # Unit tests
│   │   ├── test_pipelines/
│   │   ├── test_knowledge/
│   │   ├── test_agents/
│   │   └── test_llm/
│   ├── integration/              # Integration tests
│   │   ├── test_full_pipeline.py
│   │   ├── test_knowledge_integration.py
│   │   └── test_llm_integration.py
│   ├── evaluation/               # TRIZ accuracy tests
│   │   ├── test_case_validation.py
│   │   ├── test_contradiction_accuracy.py
│   │   └── test_principle_relevance.py
│   └── multilingual/             # Language-specific tests
│       ├── test_chinese_support.py
│       ├── test_russian_support.py
│       └── test_terminology_consistency.py
│
├── examples/                     # Usage examples
│   ├── notebooks/               # Jupyter notebooks
│   │   ├── basic_usage.ipynb
│   │   ├── advanced_pipeline.ipynb
│   │   ├── custom_knowledge.ipynb
│   │   └── evaluation_demo.ipynb
│   ├── api_usage/               # API usage examples
│   │   ├── simple_solve.py
│   │   ├── batch_processing.py
│   │   └── custom_pipeline.py
│   ├── case_studies/            # Real-world case studies
│   │   ├── automotive_innovation/
│   │   ├── software_architecture/
│   │   └── manufacturing_optimization/
│   └── educational/             # Educational materials
│       ├── triz_basics_tutorial.py
│       ├── contradiction_workshop.py
│       └── principle_exploration.py
│
├── i18n/                        # Internationalization
│   ├── glossary_en.yaml         # English terminology (canonical)
│   ├── glossary_zh.yaml         # Chinese terminology
│   ├── glossary_ru.yaml         # Russian terminology
│   ├── templates/               # Translation templates
│   │   ├── README_template.md
│   │   ├── docs_template.md
│   │   └── help_template.md
│   ├── crowdin-config.yaml      # Translation management config
│   └── sync_translations.py     # Translation synchronization script
│
├── scripts/                     # Utility scripts
│   ├── setup_dev_environment.sh # Development environment setup
│   ├── run_all_tests.sh        # Complete test suite runner
│   ├── generate_docs.py        # Documentation generation
│   ├── validate_knowledge.py   # Knowledge base validation
│   ├── benchmark_performance.py # Performance benchmarking
│   └── release_preparation.py  # Release preparation automation
│
├── docker/                     # Containerization
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose.dev.yml
│   └── requirements-docker.txt
│
├── .github/                    # GitHub-specific files
│   ├── workflows/              # GitHub Actions
│   │   ├── ci.yml             # Continuous integration
│   │   ├── docs.yml           # Documentation deployment
│   │   ├── i18n-sync.yml      # Translation synchronization
│   │   ├── security-scan.yml  # Security scanning
│   │   └── release.yml        # Release automation
│   ├── ISSUE_TEMPLATE/        # Issue templates
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   ├── translation_update.yml
│   │   └── triz_accuracy.yml
│   ├── PULL_REQUEST_TEMPLATE/ # PR templates
│   │   ├── code_change.md
│   │   ├── documentation.md
│   │   └── translation.md
│   └── CODEOWNERS            # Code ownership rules
│
└── assets/                   # Static assets
    ├── logos/               # Heinrich branding
    │   ├── heinrich_logo.svg
    │   ├── heinrich_logo.png
    │   └── favicon.ico
    ├── diagrams/            # Architecture diagrams
    │   ├── pipeline_flow.svg
    │   ├── knowledge_structure.svg
    │   └── agent_architecture.svg
    └── screenshots/         # Application screenshots
        ├── cli_demo.png
        ├── interactive_mode.png
        └── output_example.png
```

## Key Design Principles

### 1. Modular Architecture
- Each TRIZ step is an independent, testable module
- Clear interfaces between components
- Easy to extend and customize

### 2. Interpretable Pipeline  
- Every step logs its reasoning
- Traceable from problem to solution
- Human-readable intermediate outputs

### 3. Multilingual First
- Three-language parity from day one
- Consistent terminology across languages
- Cultural adaptation where appropriate

### 4. TRIZ Methodology Fidelity
- Accurate implementation of classical TRIZ
- Reference to authoritative TRIZ sources
- Expert validation of methodology

### 5. Evaluation-Driven Development
- Comprehensive test case coverage
- Quantitative quality metrics
- Continuous benchmarking

### 6. Ethical AI Implementation
- Transparent persona boundaries
- Safety filters and policies  
- Educational focus over commercial claims

This structure provides a solid foundation for the Heinrich project, supporting both immediate development needs and long-term scalability across languages and use cases.