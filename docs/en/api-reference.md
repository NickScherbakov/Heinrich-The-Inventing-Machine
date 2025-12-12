# API Reference

## Python API

### Core Classes

#### ProblemParser

Parse natural language problem descriptions into structured format.

```python
from heinrich.pipelines.problem_parser import ProblemParser

parser = ProblemParser()
result = parser.parse("Problem description here")
```

**Methods**:
- `parse(problem: str) -> ProblemStatement`: Parse problem text

**Returns**: `ProblemStatement` with:
- `technical_system`: Identified technical system
- `desired_improvement`: What needs to be improved
- `undesired_consequence`: Harmful side effect

#### ContradictionIdentifier

Identify contradictions and map to TRIZ parameters.

```python
from heinrich.pipelines.contradiction_identifier import ContradictionIdentifier

identifier = ContradictionIdentifier()
contradictions = identifier.identify(problem_statement)
```

**Methods**:
- `identify(problem: ProblemStatement) -> List[Contradiction]`

**Returns**: List of `Contradiction` objects with:
- `type`: "technical" or "physical"
- `improving_parameter`: Parameter number (1-39)
- `worsening_parameter`: Parameter number (1-39)
- `description`: Text description

#### PrincipleSelector

Select relevant TRIZ principles from contradiction matrix.

```python
from heinrich.pipelines.principle_selector import PrincipleSelector

selector = PrincipleSelector()
principles = selector.select(contradictions)
```

**Methods**:
- `select(contradictions: List[Contradiction]) -> List[Principle]`

**Returns**: List of `Principle` objects with:
- `number`: Principle number (1-40)
- `name`: Principle name
- `description`: How it applies
- `confidence`: Relevance score (0-1)

### Configuration

#### ConfigLoader

Manage Heinrich configuration from multiple sources.

```python
from heinrich.utils.config_loader import ConfigLoader

config = ConfigLoader()

# Get configuration value
provider = config.get("llm_provider", default="ollama")

# Set configuration value
config.set("language", "zh")

# Get LLM-specific configuration
llm_config = config.get_llm_config()
```

**Methods**:
- `get(key: str, default: Any = None) -> Any`
- `set(key: str, value: Any) -> None`
- `get_llm_config() -> Dict[str, Any]`

**Configuration Keys**:
- `llm_provider`: LLM provider ("ollama", "openai", "anthropic")
- `language`: UI language ("en", "zh", "ru", "ar")
- `log_level`: Logging level
- `output_format`: Output format ("markdown", "json", "html")

### Data Models

#### ProblemStatement

```python
@dataclass
class ProblemStatement:
    technical_system: str
    desired_improvement: str
    undesired_consequence: str
    raw_text: str
    confidence: float
```

#### Contradiction

```python
@dataclass
class Contradiction:
    type: str  # "technical" or "physical"
    improving_parameter: int  # 1-39
    worsening_parameter: int  # 1-39
    description: str
    confidence: float
```

#### Principle

```python
@dataclass
class Principle:
    number: int  # 1-40
    name: str
    description: str
    sub_principles: List[str]
    examples: List[str]
    confidence: float
```

## Command-Line Interface

### Interactive Mode

```bash
heinrich_cli.py interactive
```

Starts interactive session with step-by-step guidance through TRIZ methodology.

### Batch Processing (Coming Soon)

```bash
heinrich_cli.py batch problems.txt --output solutions/
```

**Options**:
- `--input`: Input file with problems (one per line or JSON)
- `--output`: Output directory for solutions
- `--format`: Output format (markdown, json, html)

### API Server Mode (Coming Soon)

```bash
heinrich_cli.py api --port 8080 --host 0.0.0.0
```

**Options**:
- `--port`: Port number (default: 8080)
- `--host`: Host address (default: 0.0.0.0)
- `--workers`: Number of worker processes

## REST API (Coming Soon)

### Solve Problem

**Endpoint**: `POST /api/v1/solve`

**Request**:
```json
{
    "problem": "Problem description here",
    "language": "en",
    "options": {
        "max_concepts": 10,
        "include_effects": true
    }
}
```

**Response**:
```json
{
    "status": "success",
    "solution": {
        "problem_statement": {...},
        "contradictions": [...],
        "principles": [...],
        "concepts": [...],
        "report": "Markdown formatted report"
    },
    "metadata": {
        "processing_time": 3.45,
        "language": "en"
    }
}
```

### Get Knowledge

**Endpoint**: `GET /api/v1/knowledge/{type}`

**Types**:
- `parameters`: Get all 39 parameters
- `principles`: Get all 40 principles
- `matrix`: Get contradiction matrix

**Example**:
```bash
curl http://localhost:8080/api/v1/knowledge/principles
```

## LLM Adapters

### BaseLLMAdapter

Abstract base class for LLM integrations.

```python
from heinrich.llm.base_adapter import BaseLLMAdapter

class CustomAdapter(BaseLLMAdapter):
    def generate(self, prompt: str, **kwargs) -> str:
        # Your implementation
        return response
```

**Methods to Implement**:
- `generate(prompt: str, **kwargs) -> str`
- `validate_config(config: Dict) -> bool`

### OllamaAdapter

```python
from heinrich.llm.adapters.ollama import OllamaAdapter

adapter = OllamaAdapter(
    base_url="http://localhost:11434",
    model="llama2"
)

response = adapter.generate("Your prompt here")
```

## Translation Synchronization

### sync_translations.py

Command-line tool for managing translations.

**Commands**:

```bash
# Detect changes in English content
python i18n/sync_translations.py detect

# Validate glossary consistency
python i18n/sync_translations.py validate

# Generate translation report
python i18n/sync_translations.py report --output report.md

# Full synchronization
python i18n/sync_translations.py sync
```

**Python API**:

```python
from i18n.sync_translations import TranslationSync
from pathlib import Path

sync = TranslationSync(repo_root=Path.cwd())

# Detect changes
changes = sync.detect_changes()

# Validate glossaries
issues = sync.validate_glossaries()

# Generate report
report = sync.generate_translation_report()
```

## Examples

### Complete Problem Solving

```python
from heinrich.pipelines import (
    ProblemParser,
    ContradictionIdentifier,
    PrincipleSelector,
    ConceptGenerator
)

# Parse problem
parser = ProblemParser()
problem = parser.parse(
    "We need faster delivery without increasing costs"
)

# Identify contradictions
identifier = ContradictionIdentifier()
contradictions = identifier.identify(problem)

# Select principles
selector = PrincipleSelector()
principles = selector.select(contradictions)

# Generate concepts
generator = ConceptGenerator()
concepts = generator.generate(problem, principles)

# Print results
for concept in concepts:
    print(f"Concept: {concept.description}")
    print(f"Based on: Principle {concept.principle_number}")
```

### Custom Configuration

```python
from heinrich.utils.config_loader import ConfigLoader
from pathlib import Path

# Load from custom config file
config = ConfigLoader(config_file=Path("my_config.yaml"))

# Override specific values
config.set("llm_provider", "openai")
config.set("language", "ru")

# Use in pipeline
parser = ProblemParser(config=config)
```

## Error Handling

### Common Exceptions

```python
from heinrich.exceptions import (
    ConfigurationError,
    LLMConnectionError,
    ValidationError,
    KnowledgeBaseError
)

try:
    result = parser.parse(problem_text)
except ValidationError as e:
    print(f"Invalid input: {e}")
except LLMConnectionError as e:
    print(f"LLM error: {e}")
```

---

**API Version**: 1.0.0  
**Last Updated**: 2025-12-12

For more examples, see the `/examples` directory in the repository.
