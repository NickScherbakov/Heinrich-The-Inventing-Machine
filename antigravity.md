# Project Analysis: Heinrich - The Inventing Machine

## 1. Project Overview
**Heinrich** is an open-source AI engine designed to automate the **Theory of Inventive Problem Solving (TRIZ)**. 
- **Goal**: To systematize innovation by guiding users through the classic TRIZ methodology (contradiction identification, principle selection, solution generation) using modern LLM agents.
- **Current Version**: 0.1.0 (Alpha).
- **License**: Apache-2.0.

## 2. Core Architecture
The project follows a modular, "interpretable pipeline" architecture, located primarily in the `heinrich/` package:

### 2.1. Pipelines (`heinrich/pipelines/`)
The core reasoning logic is broken down into distinct steps, mimicking the manual TRIZ process:
1.  `problem_parser.py`: Extracts the core problem from natural language.
2.  `contradiction_identifier.py`: Maps the problem to the standard **39 Engineering Parameters**.
3.  `principle_selector.py`: Uses the Contradiction Matrix to find relevant **40 Inventive Principles**.
4.  `effects_lookup.py`: Consults scientific effects databases.
5.  `concept_generator.py` & `adaptation_planner.py`: Generates and refines solutions using LLMs.

### 2.2. Knowledge Base (`heinrich/knowledge/`)
Heinrich does not hallucinate TRIZ data; it relies on structured ground truth:
- `39_parameters.yaml` & `40_principles.yaml`: Definitions of TRIZ fundamentals.
- `contradiction_matrix.csv`: The classic lookup table for resolving contradictions.
- `effects_database.json`: Database of scientific effects.

### 2.3. LLM Integration (`heinrich/llm/`)
- **Adapters**: The system is agnostic to the LLM provider, with adapters for **OpenAI**, **Anthropic**, **Ollama**, and **vLLM**.
- **Prompts**: structured templates for different "personas" and tasks (e.g., `analyst_mode`, `evaluator_mode`).
- **No Heavy Frameworks**: Interestingly, the project appears to use direct API integration (likely via `requests`) rather than heavy abstractions like LangChain in its core dependencies.

### 2.4. Agents & Orchestration (`heinrich/agents/`)
- Includes an `orchestrator.py` to manage the workflow state machine.
- Supports multi-turn conversations and tool usage.

## 3. Technology Stack
- **Language**: Python (>=3.8).
- **Core Dependencies**:
    - `PyYAML`: For configuration and knowledge files.
    - `numpy`: Likely for matrix operations (contradiction matrix).
    - `dataclasses-json`: For strict data modeling and serialization.
    - `requests`: For API communication.
- **Optional**: `FastAPI` (web server) and `Rich` (CLI UI).

## 4. Key Features
- **Multilingual Native**: Designed from the start to support **English, Chinese, Russian, and Arabic**.
- **Evaluation-Driven**: Contains a robust `evaluation/` module with benchmarks and curated test cases (`automotive`, `software`, etc.).
- **Interpretable**: Emphasizes "showing work" by logging reasoning at every step of the pipeline.

## 5. Directory Highlights
- `docs/`: Extensive documentation in 4 languages.
- `examples/`: Jupyter notebooks and scripts demonstrating usage.
- `.github/workflows/`: CI/CD setup for testing, docs, and i18n synchronization.
