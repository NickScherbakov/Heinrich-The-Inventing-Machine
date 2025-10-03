# Contributing to Heinrich: The Inventing Machine

Thank you for your interest in contributing to Heinrich! This guide will help you get started with contributing to our open-source TRIZ AI engine.

## 🌍 Multilingual Project

Heinrich supports three languages with full documentation parity:
- **English** (primary/canonical)
- **中文 (Chinese)**
- **Русский (Russian)**

All contributions should consider multilingual impact and maintain consistency across languages.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Multilingual Workflow](#multilingual-workflow)
- [Testing](#testing)
- [Documentation](#documentation)
- [Issue Templates](#issue-templates)
- [Pull Request Process](#pull-request-process)

## 📜 Code of Conduct

This project adheres to a Code of Conduct that we expect all contributors to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before participating.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/heinrich.git
   cd heinrich
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install development dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

## 🛠 Development Setup

### Prerequisites

- Python 3.8+
- Git
- Pre-commit (for code quality)

### Setting up pre-commit hooks

```bash
pre-commit install
```

This ensures code quality checks run automatically before each commit.

### Environment Variables

Create a `.env` file in the project root:

```bash
# LLM Configuration
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here

# Development Settings
HEINRICH_DEBUG=true
HEINRICH_LOG_LEVEL=DEBUG
```

## 📝 Contributing Guidelines

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**
- **Feature implementations**
- **Documentation improvements**
- **Test additions**
- **Translation updates**
- **TRIZ knowledge base enhancements**
- **Performance optimizations**

### Branch Naming Convention

- `feature/description-of-feature`
- `bugfix/issue-number-short-description`
- `docs/documentation-update`
- `i18n/language-code-translation-update`

### Commit Message Format

Follow conventional commit format:

```
type(scope): short description

Longer description if necessary

Closes #issue-number
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `i18n`

**Examples**:
- `feat(pipeline): add contradiction identifier module`
- `fix(triz): correct parameter 23 definition in knowledge base`
- `docs(zh): update Chinese README with new examples`
- `i18n(ru): sync Russian glossary with new TRIZ terms`

## 🌐 Multilingual Workflow

### Language Priority

1. **English** is the canonical source
2. **Changes in English** trigger translation tasks
3. **Translations** should maintain technical accuracy and cultural appropriateness

### Translation Process

1. **Update English content** first
2. **Create translation issues** automatically via GitHub Actions
3. **Use terminology glossaries** (`/i18n/glossary_*.yaml`)
4. **Maintain consistency** in technical terms across languages

### Glossary Management

Each language has a terminology glossary:

```yaml
# i18n/glossary_ru.yaml
triz:
  en: "TRIZ"
  ru: "ТРИЗ"
  definition: "Theory of Inventive Problem Solving"

contradiction:
  en: "contradiction"
  ru: "противоречие"
  definition: "Conflict between system parameters"
```

### Translation Guidelines

- **Technical terms**: Use established TRIZ terminology
- **Consistency**: Follow glossary definitions
- **Cultural adaptation**: Adapt examples for local context while maintaining technical accuracy
- **Review process**: All translations require native speaker review

## 🧪 Testing

### Test Structure

```
tests/
├── unit/           # Unit tests for individual modules
├── integration/    # Integration tests for pipelines  
├── evaluation/     # TRIZ case-based evaluation tests
└── multilingual/   # Language-specific tests
```

### Running Tests

```bash
# All tests
pytest

# Specific test categories
pytest tests/unit/
pytest tests/integration/
pytest tests/evaluation/

# With coverage
pytest --cov=heinrich

# Multilingual tests
pytest tests/multilingual/ -k "chinese"
```

### Test Requirements

- **Unit tests** for all new modules
- **Integration tests** for pipeline changes
- **Case-based tests** for TRIZ accuracy
- **Multilingual tests** for i18n features

### TRIZ Evaluation Tests

We maintain a curated case base for testing TRIZ accuracy:

```python
# Example evaluation test
def test_contradiction_identification():
    case = load_case("automotive_speed_vs_fuel")
    result = heinrich.solve(case.problem)
    
    assert result.contradictions[0].improving_parameter == 9  # Speed
    assert result.contradictions[0].worsening_parameter == 19  # Energy use
    assert 15 in result.selected_principles  # Dynamics
```

## 📚 Documentation

### Documentation Structure

```
docs/
├── en/             # English (canonical)
├── zh/             # Chinese
├── ru/             # Russian
└── shared/         # Language-agnostic assets
```

### Documentation Standards

- **Clear headings** and navigation
- **Code examples** with explanations
- **TRIZ methodology** accuracy
- **Consistent terminology** across languages
- **Regular updates** with code changes

### API Documentation

Use Google-style docstrings:

```python
def identify_contradiction(problem: str) -> Contradiction:
    """Identify technical contradictions in a problem statement.
    
    Args:
        problem: Natural language problem description
        
    Returns:
        Contradiction object with improving/worsening parameters
        
    Raises:
        ValidationError: If problem format is invalid
        
    Example:
        >>> problem = "Make car faster without using more fuel"
        >>> contradiction = identify_contradiction(problem)
        >>> print(contradiction.improving_parameter)  # 9 (Speed)
    """
```

## 📋 Issue Templates

### Bug Report Template

```markdown
**Describe the bug**
Clear description of the bug

**TRIZ Context**
- Problem type: [contradiction/effects/principles]
- Expected TRIZ result: 
- Actual result:

**To Reproduce**
Steps to reproduce the behavior

**Environment**
- Heinrich version:
- Python version:
- LLM provider:
- Language: [en/zh/ru]

**Additional context**
Screenshots, logs, or other context
```

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature

**TRIZ Methodology Alignment**
How does this feature align with TRIZ principles?

**Use Cases**
Specific scenarios where this feature would be useful

**Implementation Ideas**
Technical approach or references

**Multilingual Impact**
How will this feature affect documentation/translations?
```

## 🔄 Pull Request Process

### Before Submitting

1. **Run tests**: `pytest`
2. **Check code quality**: `pre-commit run --all-files`
3. **Update documentation** if needed
4. **Consider multilingual impact**
5. **Add tests** for new functionality

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature  
- [ ] Documentation update
- [ ] Translation update
- [ ] TRIZ knowledge base update

## TRIZ Impact
How do these changes affect TRIZ methodology accuracy?

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] TRIZ evaluation tests pass
- [ ] Multilingual tests pass

## Multilingual Checklist
- [ ] English documentation updated
- [ ] Translation tasks created (if applicable)
- [ ] Glossary terms updated (if applicable)
- [ ] Cultural appropriateness considered

## Screenshots/Examples
If applicable, add screenshots or example outputs
```

### Review Process

1. **Automated checks** must pass
2. **Code review** by maintainers
3. **TRIZ accuracy review** for methodology changes
4. **Translation review** for multilingual changes
5. **Final approval** and merge

### Merge Requirements

- ✅ All tests passing
- ✅ Code review approved
- ✅ Documentation updated
- ✅ No merge conflicts
- ✅ Multilingual consistency maintained

## 🏆 Recognition

Contributors will be recognized:

- **Contributors file** with all contributors
- **Release notes** acknowledging significant contributions
- **Special recognition** for major features or extensive translations

## 📞 Getting Help

- **GitHub Discussions**: General questions and ideas
- **Issues**: Bug reports and feature requests
- **Email**: heinrich-dev@example.com for sensitive matters

## 🎯 Project Vision

Remember our core principles:
- **TRIZ methodology accuracy** above all
- **Interpretable reasoning** for trust and learning
- **Multilingual accessibility** for global TRIZ community
- **Open source collaboration** for innovation democratization

Thank you for contributing to Heinrich! Your efforts help make systematic invention accessible to innovators worldwide. 🚀

---

*"Innovation happens when diverse minds collaborate with systematic methods."*