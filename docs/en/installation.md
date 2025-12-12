# Installation Guide

## System Requirements

### Minimum Requirements

- **Python**: 3.8 or higher
- **pip**: Latest version recommended
- **OS**: Linux, macOS, or Windows
- **RAM**: 4GB minimum (8GB recommended for LLM usage)
- **Disk Space**: 2GB for installation + models

### Recommended for Production

- **Python**: 3.10+
- **RAM**: 16GB (for running local LLMs)
- **CPU**: Multi-core processor
- **GPU**: Optional, for faster LLM inference

## Installation Methods

### Method 1: Install from Source (Recommended for Development)

1. **Clone the repository**:
```bash
git clone https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine.git
cd Heinrich-The-Inventing-Machine
```

2. **Create virtual environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Install Heinrich in development mode**:
```bash
pip install -e .
```

5. **Verify installation**:
```bash
python -c "import heinrich; print(heinrich.__version__)"
```

### Method 2: Install from PyPI (Coming Soon)

```bash
pip install heinrich-triz
```

## Configuration

### 1. Create Configuration File

Copy the example environment file:

```bash
cp .env.example .env
```

### 2. Configure LLM Provider

Edit `.env` file with your preferred settings:

#### Option A: Ollama (Local, Free)

```bash
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2
```

**Setup Ollama**:
1. Install from [ollama.ai](https://ollama.ai)
2. Pull a model: `ollama pull llama2`
3. Start Heinrich

#### Option B: OpenAI API

```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4
```

#### Option C: Anthropic Claude

```bash
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_MODEL=claude-3-opus-20240229
```

### 3. Set Language Preference

```bash
# Language preference: en, zh, ru, ar
LANGUAGE=en
```

### 4. Configure Logging

```bash
# Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL=INFO
```

## Verification

### Run Basic Example

```bash
python examples/basic_usage.py
```

Expected output:
```
Technical System: car
Desired Improvement: faster
Undesired Consequence: increasing engine power makes it consume more fuel
```

### Run Tests (if installed with dev dependencies)

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run with coverage
pytest --cov=heinrich
```

## Troubleshooting

### Issue: ModuleNotFoundError

**Solution**: Ensure you've installed Heinrich and dependencies:
```bash
pip install -e .
```

### Issue: LLM Connection Failed

**Solution for Ollama**:
1. Check Ollama is running: `ollama list`
2. Verify URL in .env matches Ollama server
3. Test connection: `curl http://localhost:11434/api/tags`

**Solution for OpenAI/Anthropic**:
1. Verify API key is correct
2. Check internet connection
3. Verify API quota/billing

### Issue: Import Error for heinrich modules

**Solution**: 
1. Ensure you're in the virtual environment: `which python`
2. Reinstall: `pip install -e .`
3. Check PYTHONPATH includes repository root

### Issue: Missing Dependencies

**Solution**:
```bash
# Update pip
pip install --upgrade pip

# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

## Optional: Docker Installation

### Using Docker (Coming Soon)

```bash
# Build image
docker build -t heinrich:latest .

# Run container
docker run -it -p 8080:8080 heinrich:latest

# With environment file
docker run -it --env-file .env heinrich:latest
```

### Using Docker Compose

```bash
# Start services
docker-compose up

# Stop services
docker-compose down
```

## Development Setup

### Additional Development Tools

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Setup pre-commit hooks
pre-commit install

# Install additional tools
pip install black flake8 mypy pytest-cov
```

### IDE Configuration

#### VS Code

Create `.vscode/settings.json`:
```json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true
}
```

#### PyCharm

1. Set Python interpreter to virtual environment
2. Enable pytest as test runner
3. Configure Black as code formatter

## Next Steps

After installation:

1. **Quick Start**: Read [TRIZ Basics](triz-basics.md)
2. **Architecture**: Understand [System Architecture](architecture.md)
3. **API Reference**: Explore [API Documentation](api-reference.md)
4. **Examples**: Try examples in `/examples` directory

## Getting Help

- **Documentation**: Check other docs in this directory
- **GitHub Issues**: [Report bugs or ask questions](https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine/issues)
- **Discussions**: [Community forum](https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine/discussions)

---

**Ready to start inventing!** 🚀
