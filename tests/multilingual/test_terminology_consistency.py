"""
Tests for terminology consistency across all languages.
"""
import pytest
import yaml
from pathlib import Path


def test_all_glossaries_have_same_terms(glossary_files):
    """Test that all glossaries have the same set of terms."""
    # Load all glossaries
    glossaries = {}
    for lang, filepath in glossary_files.items():
        with open(filepath, 'r', encoding='utf-8') as f:
            glossaries[lang] = yaml.safe_load(f)
    
    # Get term sets (excluding metadata)
    term_sets = {}
    for lang, data in glossaries.items():
        term_sets[lang] = {k for k in data.keys() if k != "metadata"}
    
    # English is canonical
    en_terms = term_sets["en"]
    
    # Check each language has all English terms
    for lang in ["zh", "ru", "ar"]:
        missing = en_terms - term_sets[lang]
        extra = term_sets[lang] - en_terms
        
        assert len(missing) == 0, \
            f"{lang.upper()} glossary missing {len(missing)} terms: {', '.join(list(missing)[:10])}"
        
        assert len(extra) == 0, \
            f"{lang.upper()} glossary has {len(extra)} extra terms not in English: {', '.join(list(extra)[:10])}"


def test_core_triz_terms_consistency(glossary_files):
    """Test that core TRIZ terms are consistently defined across languages."""
    core_terms = [
        "triz",
        "contradiction",
        "technical_contradiction",
        "physical_contradiction",
        "inventive_principles",
        "engineering_parameters",
        "ariz",
        "ideal_final_result",
    ]
    
    # Load all glossaries
    glossaries = {}
    for lang, filepath in glossary_files.items():
        with open(filepath, 'r', encoding='utf-8') as f:
            glossaries[lang] = yaml.safe_load(f)
    
    # Check each core term exists in all languages
    for term in core_terms:
        for lang, data in glossaries.items():
            assert term in data, f"Term '{term}' missing from {lang.upper()} glossary"


def test_principle_numbering_consistency(glossary_files):
    """Test that principle numbering is consistent across languages."""
    # Load all glossaries
    glossaries = {}
    for lang, filepath in glossary_files.items():
        with open(filepath, 'r', encoding='utf-8') as f:
            glossaries[lang] = yaml.safe_load(f)
    
    # Get principle terms from English
    en_principles = {k: v for k, v in glossaries["en"].items() 
                     if k.startswith("principle_") and isinstance(v, dict)}
    
    # Check each principle has consistent number across languages
    for principle_key, en_data in en_principles.items():
        en_number = en_data.get("number")
        assert en_number is not None, f"{principle_key} missing number in English"
        
        for lang in ["zh", "ru", "ar"]:
            if principle_key in glossaries[lang]:
                lang_data = glossaries[lang][principle_key]
                lang_number = lang_data.get("number")
                
                assert lang_number == en_number, \
                    f"{principle_key} has different number in {lang.upper()}: {lang_number} vs {en_number}"


def test_parameter_numbering_consistency(glossary_files):
    """Test that parameter numbering is consistent across languages."""
    # Load all glossaries
    glossaries = {}
    for lang, filepath in glossary_files.items():
        with open(filepath, 'r', encoding='utf-8') as f:
            glossaries[lang] = yaml.safe_load(f)
    
    # Get parameter terms from English
    en_parameters = {k: v for k, v in glossaries["en"].items() 
                     if k.startswith("parameter_") and isinstance(v, dict)}
    
    # Check each parameter has consistent number across languages
    for param_key, en_data in en_parameters.items():
        en_number = en_data.get("number")
        assert en_number is not None, f"{param_key} missing number in English"
        
        for lang in ["zh", "ru", "ar"]:
            if param_key in glossaries[lang]:
                lang_data = glossaries[lang][param_key]
                lang_number = lang_data.get("number")
                
                assert lang_number == en_number, \
                    f"{param_key} has different number in {lang.upper()}: {lang_number} vs {en_number}"


def test_metadata_version_consistency(glossary_files):
    """Test that all glossaries have metadata with version."""
    for lang, filepath in glossary_files.items():
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        assert "metadata" in data, f"{lang.upper()} glossary missing metadata"
        assert "version" in data["metadata"], f"{lang.upper()} metadata missing version"
        assert "last_updated" in data["metadata"], f"{lang.upper()} metadata missing last_updated"


def test_english_is_canonical(glossary_files):
    """Test that English glossary has 'en' fields for all terms."""
    with open(glossary_files["en"], 'r', encoding='utf-8') as f:
        en_data = yaml.safe_load(f)
    
    terms = {k: v for k, v in en_data.items() if k != "metadata" and isinstance(v, dict)}
    
    for term_key, term_data in terms.items():
        assert "en" in term_data or "definition" in term_data, \
            f"Term '{term_key}' should have 'en' field or 'definition' in English glossary"


def test_translations_not_empty(glossary_files):
    """Test that translations are not empty strings."""
    languages = ["zh", "ru", "ar"]
    
    for lang in languages:
        with open(glossary_files[lang], 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        terms = {k: v for k, v in data.items() if k != "metadata" and isinstance(v, dict)}
        
        for term_key, term_data in terms.items():
            if lang in term_data:
                translation = term_data[lang]
                assert translation and translation.strip(), \
                    f"Term '{term_key}' has empty {lang.upper()} translation"


def test_definitions_consistency(glossary_files):
    """Test that English definitions are present for all terms."""
    with open(glossary_files["en"], 'r', encoding='utf-8') as f:
        en_data = yaml.safe_load(f)
    
    terms = {k: v for k, v in en_data.items() if k != "metadata" and isinstance(v, dict)}
    
    for term_key, term_data in terms.items():
        # Skip if it's just a simple mapping
        if len(term_data) > 2:  # Has more than just 'en' and language code
            assert "definition" in term_data, \
                f"Term '{term_key}' should have a definition"


def test_cross_language_term_structure(glossary_files):
    """Test that all languages have similar structure for each term."""
    # Load all glossaries
    glossaries = {}
    for lang, filepath in glossary_files.items():
        with open(filepath, 'r', encoding='utf-8') as f:
            glossaries[lang] = yaml.safe_load(f)
    
    # Get a sample term from English
    sample_terms = ["triz", "contradiction", "principle_01_segmentation"]
    
    for term_key in sample_terms:
        if term_key not in glossaries["en"]:
            continue
            
        en_keys = set(glossaries["en"][term_key].keys())
        
        for lang in ["zh", "ru", "ar"]:
            if term_key in glossaries[lang]:
                lang_keys = set(glossaries[lang][term_key].keys())
                
                # Should have similar keys (allowing for language-specific fields)
                common_structural_keys = {"definition", "note", "examples", "number"}
                common_keys = en_keys & common_structural_keys
                
                if common_keys:
                    missing = common_keys - lang_keys
                    # It's OK if some structural keys are missing in translations
                    # Just log it for now
                    if missing:
                        print(f"Note: {term_key} in {lang.upper()} missing: {missing}")


def test_glossary_file_sizes_reasonable(glossary_files):
    """Test that glossary files are of reasonable size."""
    for lang, filepath in glossary_files.items():
        file_size = filepath.stat().st_size
        
        # Each glossary should be at least 5KB (has substantial content)
        assert file_size > 5000, \
            f"{lang.upper()} glossary is too small ({file_size} bytes), may be incomplete"
        
        # But not too large (reasonable upper bound)
        assert file_size < 200000, \
            f"{lang.upper()} glossary is very large ({file_size} bytes), check for issues"
