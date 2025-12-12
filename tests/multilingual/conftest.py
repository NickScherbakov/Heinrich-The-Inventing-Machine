"""
Pytest configuration for multilingual tests.
"""
import pytest
from pathlib import Path


@pytest.fixture
def repo_root():
    """Return the repository root directory."""
    return Path(__file__).parent.parent.parent


@pytest.fixture
def i18n_dir(repo_root):
    """Return the i18n directory."""
    return repo_root / "i18n"


@pytest.fixture
def docs_dir(repo_root):
    """Return the docs directory."""
    return repo_root / "docs"


@pytest.fixture
def glossary_files(i18n_dir):
    """Return dict of language to glossary file path."""
    return {
        "en": i18n_dir / "glossary_en.yaml",
        "zh": i18n_dir / "glossary_zh.yaml",
        "ru": i18n_dir / "glossary_ru.yaml",
        "ar": i18n_dir / "glossary_ar.yaml",
    }


@pytest.fixture
def docs_dirs(docs_dir):
    """Return dict of language to docs directory path."""
    return {
        "en": docs_dir / "en",
        "zh": docs_dir / "zh",
        "ru": docs_dir / "ru",
        "ar": docs_dir / "ar",
    }
