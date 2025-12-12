# System Architecture

## Overview

Heinrich implements a modular, interpretable TRIZ reasoning pipeline that combines classical methodology with modern AI capabilities.

## Architecture Principles

1. **Modularity**: Each TRIZ step is an independent, testable module
2. **Interpretability**: Every decision is logged and traceable
3. **Extensibility**: Easy to add new knowledge or customize behavior
4. **Multilingual**: First-class support for multiple languages

## System Components

### 1. Core Pipeline (heinrich/pipelines/)

Seven sequential modules implementing TRIZ methodology:

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

#### Problem Parser
- **Input**: Natural language problem description
- **Output**: Structured problem with technical system, improvement goal, harmful effect
- **Method**: NLP + pattern matching + LLM assistance

#### Contradiction Identifier
- **Input**: Structured problem
- **Output**: Technical and/or physical contradictions mapped to 39 parameters
- **Method**: Parameter matching + semantic similarity

#### Principle Selector
- **Input**: Contradictions with parameters
- **Output**: Recommended principles from 40 inventive principles
- **Method**: Contradiction matrix lookup + relevance ranking

#### Effects Lookup
- **Input**: Selected principles + problem context
- **Output**: Applicable scientific effects and evolution patterns
- **Method**: Effects database search + analogical reasoning

#### Concept Generator
- **Input**: Principles + effects + problem
- **Output**: Multiple solution concepts with TRIZ traceability
- **Method**: Template-based generation + LLM creativity

#### Adaptation Planner
- **Input**: Solution concepts + context constraints
- **Output**: Practical implementation recommendations
- **Method**: Constraint analysis + resource planning

#### Report Builder
- **Input**: All pipeline outputs
- **Output**: Structured, human-readable solution report
- **Method**: Template rendering + formatting

### 2. Knowledge Base (heinrich/knowledge/)

TRIZ knowledge organized in structured files:

```
knowledge/
├── 39_parameters.yaml       # Complete parameter definitions
├── 40_principles.yaml        # Complete principle definitions
├── contradiction_matrix.csv  # 39×39 contradiction matrix
├── effects_database.json     # Scientific effects catalog
└── knowledge_loader.py       # Access layer
```

**Design**:
- YAML/CSV/JSON formats for human-readability
- Versioned and validated
- Multilingual support via i18n glossaries

### 3. LLM Integration (heinrich/llm/)

Flexible integration layer for multiple LLM providers:

```
llm/
├── base_adapter.py           # Abstract adapter interface
├── adapters/
│   ├── ollama.py            # Local models via Ollama
│   ├── openai.py            # OpenAI API
│   ├── anthropic.py         # Claude API
│   └── vllm.py              # vLLM deployment
└── prompts/                 # Structured prompts
    ├── system_prompts/      # Persona definitions
    └── step_prompts/        # Module-specific prompts
```

**Features**:
- Provider abstraction
- Prompt versioning
- Safety guards
- Ethical boundaries

### 4. Agent System (heinrich/agents/)

Orchestrates multi-step reasoning:

```
agents/
├── orchestrator.py          # FSM/workflow coordinator
├── persona_manager.py       # Heinrich persona
├── tool_registry.py         # Available tools/services
└── conversation_manager.py  # Multi-turn dialogue
```

**Capabilities**:
- State management
- Multi-turn conversations
- Tool invocation
- Persona consistency

### 5. Utilities (heinrich/utils/)

Shared infrastructure:

```
utils/
├── config_loader.py         # Configuration management
├── logging_config.py        # Structured logging
├── data_validation.py       # Input/output validation
└── file_utils.py            # File operations
```

## Data Flow

```
User Input (Natural Language)
         ↓
   [Configuration Load]
         ↓
   [Problem Parser]
         ↓
   {ProblemStatement}
         ↓
[Contradiction Identifier]
         ↓
   {Contradictions}
         ↓
 [Principle Selector]
    ↓         ↓
{Principles} [Knowledge Base]
    ↓              ↓
[Effects Lookup] ←┘
         ↓
    {Effects}
         ↓
[Concept Generator]
         ↓
    {Concepts}
         ↓
[Adaptation Planner]
         ↓
  {Recommendations}
         ↓
  [Report Builder]
         ↓
 Solution Report (Markdown/JSON/HTML)
```

## Multilingual Support

### I18n Architecture

```
i18n/
├── glossary_*.yaml          # Terminology per language
├── sync_translations.py     # Synchronization
└── crowdin-config.yaml      # Translation workflow

docs/
├── en/                      # English (canonical)
├── zh/                      # Chinese
├── ru/                      # Russian
└── ar/                      # Arabic
```

**Process**:
1. English content is canonical source
2. Changes trigger sync_translations.py
3. Crowdin manages translation workflow
4. Automated PRs for translation updates

### Language Selection

```python
# Via configuration
config = ConfigLoader()
config.set("language", "zh")

# Via environment variable
export LANGUAGE=ru

# Via CLI
heinrich_cli.py --language ar
```

## Configuration System

### Hierarchy

1. **Defaults** (in code)
2. **Config file** (YAML)
3. **Environment variables**
4. **CLI arguments**

Later sources override earlier ones.

### Example Configuration

```yaml
# heinrich_config.yaml
llm_provider: ollama
llm_model: llama2
language: en
log_level: INFO
output_format: markdown

# Knowledge base
knowledge_path: ./heinrich/knowledge/
cache_enabled: true
cache_ttl: 3600

# Pipeline
enable_all_modules: true
max_concepts: 10
min_principle_confidence: 0.5
```

## Extension Points

### Adding New Modules

1. Implement module interface:
```python
class NewModule:
    def process(self, input_data):
        # Your logic
        return output_data
```

2. Register in orchestrator
3. Add prompts if using LLM
4. Write tests
5. Document behavior

### Adding New LLM Provider

1. Implement `BaseLLMAdapter`:
```python
class NewProviderAdapter(BaseLLMAdapter):
    def generate(self, prompt, **kwargs):
        # Provider-specific API call
        return response
```

2. Add configuration
3. Update documentation

### Adding New Language

1. Create `glossary_{lang}.yaml`
2. Create `docs/{lang}/` directory
3. Update configuration
4. Add tests
5. Update Crowdin config

## Performance Considerations

- **Caching**: LLM responses cached by default
- **Parallel Processing**: Concept generation parallelized
- **Lazy Loading**: Knowledge base loaded on demand
- **Batch Processing**: Support for multiple problems

## Security & Privacy

- **No data retention**: Problems not stored by default
- **Local execution**: Ollama for on-premise deployment
- **Content filtering**: Safety checks on input/output
- **API key protection**: Secure credential management

---

**Architecture Version**: 1.0.0  
**Last Updated**: 2025-12-12
