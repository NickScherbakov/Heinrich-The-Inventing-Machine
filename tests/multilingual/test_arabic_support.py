"""
Tests for Arabic language support (NEW).
"""
import pytest
import yaml
from pathlib import Path


def test_arabic_glossary_exists(glossary_files):
    """Test that Arabic glossary file exists."""
    assert glossary_files["ar"].exists(), "Arabic glossary file not found"


def test_arabic_glossary_valid_yaml(glossary_files):
    """Test that Arabic glossary is valid YAML."""
    with open(glossary_files["ar"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    assert data is not None, "Arabic glossary is empty"
    assert isinstance(data, dict), "Arabic glossary is not a dictionary"


def test_arabic_glossary_has_metadata(glossary_files):
    """Test that Arabic glossary has required metadata."""
    with open(glossary_files["ar"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    assert "metadata" in data, "Arabic glossary missing metadata"
    metadata = data["metadata"]
    
    assert metadata["language"] == "ar", "Language not set to ar"
    assert "version" in metadata, "Missing version"
    assert "last_updated" in metadata, "Missing last_updated"
    assert metadata.get("rtl") == True, "RTL flag should be true for Arabic"


def test_arabic_glossary_has_core_terms(glossary_files):
    """Test that Arabic glossary has core TRIZ terms."""
    with open(glossary_files["ar"], 'r', encoding='utf-8') as f:
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


def test_arabic_translations_present(glossary_files):
    """Test that Arabic translations are present for terms."""
    with open(glossary_files["ar"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check a few key terms have Arabic translations
    assert "ar" in data["triz"], "TRIZ term missing Arabic translation"
    assert "ar" in data["contradiction"], "Contradiction missing Arabic translation"
    
    # Verify Arabic text is actually present (not just en)
    assert data["contradiction"]["ar"] != data["contradiction"]["en"], \
        "Arabic translation is same as English"


def test_arabic_docs_directory_exists(docs_dirs):
    """Test that Arabic documentation directory exists."""
    assert docs_dirs["ar"].exists(), "Arabic docs directory not found"
    assert docs_dirs["ar"].is_dir(), "Arabic docs path is not a directory"


def test_arabic_docs_have_readme(docs_dirs):
    """Test that Arabic docs have README."""
    readme = docs_dirs["ar"] / "README.md"
    assert readme.exists(), "Arabic README.md not found"


def test_arabic_docs_utf8_encoding(docs_dirs):
    """Test that Arabic documentation files are UTF-8 encoded."""
    for md_file in docs_dirs["ar"].glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        assert content, f"File {md_file.name} is empty"
        # Verify Arabic characters are present
        has_arabic = any('\u0600' <= char <= '\u06FF' for char in content)
        assert has_arabic, f"File {md_file.name} has no Arabic characters"


def test_arabic_glossary_consistency(glossary_files):
    """Test that Arabic glossary is consistent with English."""
    with open(glossary_files["en"], 'r', encoding='utf-8') as f:
        en_data = yaml.safe_load(f)
    
    with open(glossary_files["ar"], 'r', encoding='utf-8') as f:
        ar_data = yaml.safe_load(f)
    
    # Get term keys (excluding metadata)
    en_terms = {k for k in en_data.keys() if k != "metadata"}
    ar_terms = {k for k in ar_data.keys() if k != "metadata"}
    
    # Check for missing terms
    missing_terms = en_terms - ar_terms
    assert len(missing_terms) == 0, \
        f"Arabic glossary missing terms: {', '.join(list(missing_terms)[:5])}"


def test_arabic_principle_translations(glossary_files):
    """Test that Arabic has principle translations."""
    with open(glossary_files["ar"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check at least a few principles have translations
    principles = [k for k in data.keys() if k.startswith("principle_")]
    assert len(principles) >= 10, "Not enough principle translations"
    
    for principle_key in principles[:5]:  # Check first 5
        principle = data[principle_key]
        assert "ar" in principle, f"{principle_key} missing Arabic translation"


def test_arabic_parameter_translations(glossary_files):
    """Test that Arabic has parameter translations."""
    with open(glossary_files["ar"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check at least a few parameters have translations
    parameters = [k for k in data.keys() if k.startswith("parameter_")]
    assert len(parameters) >= 10, "Not enough parameter translations"
    
    for param_key in parameters[:5]:  # Check first 5
        param = data[param_key]
        assert "ar" in param, f"{param_key} missing Arabic translation"


def test_arabic_rtl_support(glossary_files):
    """Test that Arabic glossary is marked for RTL support."""
    with open(glossary_files["ar"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check metadata has RTL flag
    assert "metadata" in data, "Missing metadata"
    assert data["metadata"].get("rtl") == True, \
        "Arabic glossary should have rtl: true in metadata"


def test_arabic_text_direction(glossary_files):
    """Test that Arabic translations use proper text."""
    with open(glossary_files["ar"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check that Arabic translations contain Arabic script
    for key in ["triz", "contradiction", "inventive_principles"]:
        if key in data and "ar" in data[key]:
            ar_text = data[key]["ar"]
            # Verify it's not empty and contains Arabic characters
            assert ar_text, f"{key} has empty Arabic translation"
            has_arabic = any('\u0600' <= char <= '\u06FF' for char in ar_text)
            assert has_arabic, f"{key} Arabic translation has no Arabic script"
