"""
Tests for Chinese language support.
"""
import pytest
import yaml
from pathlib import Path


def test_chinese_glossary_exists(glossary_files):
    """Test that Chinese glossary file exists."""
    assert glossary_files["zh"].exists(), "Chinese glossary file not found"


def test_chinese_glossary_valid_yaml(glossary_files):
    """Test that Chinese glossary is valid YAML."""
    with open(glossary_files["zh"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    assert data is not None, "Chinese glossary is empty"
    assert isinstance(data, dict), "Chinese glossary is not a dictionary"


def test_chinese_glossary_has_metadata(glossary_files):
    """Test that Chinese glossary has required metadata."""
    with open(glossary_files["zh"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    assert "metadata" in data, "Chinese glossary missing metadata"
    metadata = data["metadata"]
    
    assert metadata["language"] == "zh", "Language not set to zh"
    assert "version" in metadata, "Missing version"
    assert "last_updated" in metadata, "Missing last_updated"


def test_chinese_glossary_has_core_terms(glossary_files):
    """Test that Chinese glossary has core TRIZ terms."""
    with open(glossary_files["zh"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    core_terms = [
        "triz",
        "contradiction",
        "technical_contradiction",
        "physical_contradiction",
        "inventive_principles",
        "engineering_parameters",
    ]
    
    for term in core_terms:
        assert term in data, f"Missing core term: {term}"


def test_chinese_translations_present(glossary_files):
    """Test that Chinese translations are present for terms."""
    with open(glossary_files["zh"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check a few key terms have Chinese translations
    assert "zh" in data["triz"], "TRIZ term missing Chinese translation"
    assert "zh" in data["contradiction"], "Contradiction missing Chinese translation"
    
    # Verify Chinese text is actually present (not just en)
    assert data["contradiction"]["zh"] != data["contradiction"]["en"], \
        "Chinese translation is same as English"


def test_chinese_docs_directory_exists(docs_dirs):
    """Test that Chinese documentation directory exists."""
    assert docs_dirs["zh"].exists(), "Chinese docs directory not found"
    assert docs_dirs["zh"].is_dir(), "Chinese docs path is not a directory"


def test_chinese_docs_have_readme(docs_dirs):
    """Test that Chinese docs have README."""
    readme = docs_dirs["zh"] / "README.md"
    assert readme.exists(), "Chinese README.md not found"


def test_chinese_docs_utf8_encoding(docs_dirs):
    """Test that Chinese documentation files are UTF-8 encoded."""
    for md_file in docs_dirs["zh"].glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        assert content, f"File {md_file.name} is empty"
        # Verify Chinese characters are present
        has_chinese = any('\u4e00' <= char <= '\u9fff' for char in content)
        assert has_chinese, f"File {md_file.name} has no Chinese characters"


def test_chinese_glossary_consistency(glossary_files):
    """Test that Chinese glossary is consistent with English."""
    with open(glossary_files["en"], 'r', encoding='utf-8') as f:
        en_data = yaml.safe_load(f)
    
    with open(glossary_files["zh"], 'r', encoding='utf-8') as f:
        zh_data = yaml.safe_load(f)
    
    # Get term keys (excluding metadata)
    en_terms = {k for k in en_data.keys() if k != "metadata"}
    zh_terms = {k for k in zh_data.keys() if k != "metadata"}
    
    # Check for missing terms
    missing_terms = en_terms - zh_terms
    assert len(missing_terms) == 0, \
        f"Chinese glossary missing terms: {', '.join(list(missing_terms)[:5])}"


def test_chinese_principle_translations(glossary_files):
    """Test that Chinese has principle translations."""
    with open(glossary_files["zh"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check at least a few principles have translations
    principles = [k for k in data.keys() if k.startswith("principle_")]
    assert len(principles) >= 10, "Not enough principle translations"
    
    for principle_key in principles[:5]:  # Check first 5
        principle = data[principle_key]
        assert "zh" in principle, f"{principle_key} missing Chinese translation"


def test_chinese_parameter_translations(glossary_files):
    """Test that Chinese has parameter translations."""
    with open(glossary_files["zh"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check at least a few parameters have translations
    parameters = [k for k in data.keys() if k.startswith("parameter_")]
    assert len(parameters) >= 10, "Not enough parameter translations"
    
    for param_key in parameters[:5]:  # Check first 5
        param = data[param_key]
        assert "zh" in param, f"{param_key} missing Chinese translation"
