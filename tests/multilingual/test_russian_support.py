"""
Tests for Russian language support.
"""
import pytest
import yaml
from pathlib import Path


def test_russian_glossary_exists(glossary_files):
    """Test that Russian glossary file exists."""
    assert glossary_files["ru"].exists(), "Russian glossary file not found"


def test_russian_glossary_valid_yaml(glossary_files):
    """Test that Russian glossary is valid YAML."""
    with open(glossary_files["ru"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    assert data is not None, "Russian glossary is empty"
    assert isinstance(data, dict), "Russian glossary is not a dictionary"


def test_russian_glossary_has_metadata(glossary_files):
    """Test that Russian glossary has required metadata."""
    with open(glossary_files["ru"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    assert "metadata" in data, "Russian glossary missing metadata"
    metadata = data["metadata"]
    
    assert metadata["language"] == "ru", "Language not set to ru"
    assert "version" in metadata, "Missing version"
    assert "last_updated" in metadata, "Missing last_updated"


def test_russian_glossary_has_core_terms(glossary_files):
    """Test that Russian glossary has core TRIZ terms."""
    with open(glossary_files["ru"], 'r', encoding='utf-8') as f:
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


def test_russian_translations_present(glossary_files):
    """Test that Russian translations are present for terms."""
    with open(glossary_files["ru"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check TRIZ - should be ТРИЗ in Russian
    assert "ru" in data["triz"], "TRIZ term missing Russian translation"
    assert data["triz"]["ru"] == "ТРИЗ", "TRIZ translation should be ТРИЗ"
    
    # Check contradiction
    assert "ru" in data["contradiction"], "Contradiction missing Russian translation"
    assert data["contradiction"]["ru"] != data["contradiction"]["en"], \
        "Russian translation is same as English"


def test_russian_docs_directory_exists(docs_dirs):
    """Test that Russian documentation directory exists."""
    assert docs_dirs["ru"].exists(), "Russian docs directory not found"
    assert docs_dirs["ru"].is_dir(), "Russian docs path is not a directory"


def test_russian_docs_have_readme(docs_dirs):
    """Test that Russian docs have README."""
    readme = docs_dirs["ru"] / "README.md"
    assert readme.exists(), "Russian README.md not found"


def test_russian_docs_utf8_encoding(docs_dirs):
    """Test that Russian documentation files are UTF-8 encoded."""
    for md_file in docs_dirs["ru"].glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        assert content, f"File {md_file.name} is empty"
        # Verify Cyrillic characters are present
        has_cyrillic = any('\u0400' <= char <= '\u04FF' for char in content)
        assert has_cyrillic, f"File {md_file.name} has no Cyrillic characters"


def test_russian_glossary_consistency(glossary_files):
    """Test that Russian glossary is consistent with English."""
    with open(glossary_files["en"], 'r', encoding='utf-8') as f:
        en_data = yaml.safe_load(f)
    
    with open(glossary_files["ru"], 'r', encoding='utf-8') as f:
        ru_data = yaml.safe_load(f)
    
    # Get term keys (excluding metadata)
    en_terms = {k for k in en_data.keys() if k != "metadata"}
    ru_terms = {k for k in ru_data.keys() if k != "metadata"}
    
    # Check for missing terms
    missing_terms = en_terms - ru_terms
    assert len(missing_terms) == 0, \
        f"Russian glossary missing terms: {', '.join(list(missing_terms)[:5])}"


def test_russian_principle_translations(glossary_files):
    """Test that Russian has principle translations."""
    with open(glossary_files["ru"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check at least a few principles have translations
    principles = [k for k in data.keys() if k.startswith("principle_")]
    assert len(principles) >= 10, "Not enough principle translations"
    
    for principle_key in principles[:5]:  # Check first 5
        principle = data[principle_key]
        assert "ru" in principle, f"{principle_key} missing Russian translation"


def test_russian_parameter_translations(glossary_files):
    """Test that Russian has parameter translations."""
    with open(glossary_files["ru"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Check at least a few parameters have translations
    parameters = [k for k in data.keys() if k.startswith("parameter_")]
    assert len(parameters) >= 10, "Not enough parameter translations"
    
    for param_key in parameters[:5]:  # Check first 5
        param = data[param_key]
        assert "ru" in param, f"{param_key} missing Russian translation"


def test_russian_ariz_terminology(glossary_files):
    """Test that Russian has ARIZ terminology (original language)."""
    with open(glossary_files["ru"], 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # ARIZ should be in Russian glossary
    assert "ariz" in data, "Missing ARIZ term"
    assert "ru" in data["ariz"], "ARIZ missing Russian translation"
    
    # IFR (Ideal Final Result) should be ИКР in Russian
    assert "ideal_final_result" in data, "Missing Ideal Final Result term"
    if "ru" in data["ideal_final_result"]:
        # Should contain ИКР abbreviation
        assert "ИКР" in data["ideal_final_result"]["abbreviation"], \
            "IFR abbreviation should be ИКР in Russian"
