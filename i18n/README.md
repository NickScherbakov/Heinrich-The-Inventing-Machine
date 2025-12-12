# Internationalization (i18n) Directory

This directory contains all internationalization resources for the Heinrich project, supporting **4 languages**:
- 🇬🇧 **English (en)** - Canonical source
- 🇨🇳 **Chinese (zh)** - 中文
- 🇷🇺 **Russian (ru)** - Русский  
- 🇸🇦 **Arabic (ar)** - العربية (NEW)

## Directory Structure

```
i18n/
├── glossary_en.yaml         # English TRIZ terminology (canonical)
├── glossary_zh.yaml         # Chinese TRIZ terminology
├── glossary_ru.yaml         # Russian TRIZ terminology
├── glossary_ar.yaml         # Arabic TRIZ terminology (NEW)
├── templates/               # Translation templates
│   ├── README_template.md
│   ├── docs_template.md
│   └── help_template.md
├── crowdin-config.yaml      # Translation management configuration
├── sync_translations.py     # Translation synchronization script
├── .sync_state.json         # Synchronization state (auto-generated)
└── README.md               # This file
```

## TRIZ Glossary Files

Each glossary file contains core TRIZ terminology with translations. The format is YAML with the following structure:

```yaml
metadata:
  language: en
  version: "1.0.0"
  last_updated: "2025-12-12"
  description: "Description"

term_key:
  en: "English term"
  zh: "中文术语"     # Chinese (if applicable)
  ru: "русский термин"  # Russian (if applicable)
  ar: "المصطلح العربي"  # Arabic (if applicable)
  definition: "Definition in English"
  note: "Optional notes"
  examples: ["example1", "example2"]
```

### Glossary Coverage

Each glossary contains **30+ core TRIZ terms** covering:
- **Core concepts**: TRIZ, contradiction, principles, parameters
- **40 Inventive Principles**: Key selections with examples
- **39 Engineering Parameters**: Key selections with definitions
- **ARIZ methodology**: IFR, resources, operators
- **Technical system evolution**: S-curve, ideality, patterns
- **Problem-solving terms**: Mini-problem, trimming, Su-Field analysis
- **Scientific effects**: Physics, chemistry, geometry, biology
- **Standards**: 76 standard solutions patterns

### Language-Specific Notes

#### Chinese (zh)
- Uses simplified Chinese characters
- Technical terms follow established TRIZ literature in Chinese
- Examples adapted for Chinese engineering context

#### Russian (ru)
- Original language of TRIZ - authoritative terminology
- Preserves Altshuller's original terminology
- Uses Cyrillic script exclusively

#### Arabic (ar)
- **NEW ADDITION** for Arabic-speaking innovators
- Right-to-left (RTL) text direction
- Technical Arabic for engineering/innovation terms
- `rtl: true` metadata flag in glossary

## Translation Synchronization

### Using sync_translations.py

The `sync_translations.py` script manages translation workflows:

```bash
# Detect changes in English content
python i18n/sync_translations.py detect

# Validate glossary consistency
python i18n/sync_translations.py validate

# Generate translation report
python i18n/sync_translations.py report --output translation_report.md

# Full synchronization
python i18n/sync_translations.py sync
```

### Features

- ✅ Detects changes in English (canonical) content
- ✅ Marks translations as outdated when English changes
- ✅ Generates translation tasks/reports
- ✅ Validates glossary consistency across languages
- ✅ CLI support for CI/CD integration
- ✅ Maintains synchronization state

### CI/CD Integration

The script is integrated into GitHub Actions workflow (`.github/workflows/i18n-sync.yml`) to:
- Run on changes to English documentation
- Create issues for translation updates needed
- Validate glossary consistency
- Post summary comments on PRs affecting i18n

## Crowdin Integration

### Setup

1. Create account at [crowdin.com](https://crowdin.com)
2. Create new project for Heinrich
3. Set `CROWDIN_API_TOKEN` environment variable
4. Update `project_id` in `crowdin-config.yaml`

### Workflow

1. **Source files** (English) are uploaded to Crowdin
2. **Translators** work in Crowdin interface
3. **Translations** are reviewed and approved
4. **Pull requests** are automatically created with updates
5. **Merge** approved translations into main branch

### Configuration

See `crowdin-config.yaml` for detailed configuration including:
- File mappings
- Language codes
- Translation workflows
- Quality checks
- GitHub integration

## Translation Templates

The `templates/` directory contains reusable templates for common documents:

- **README_template.md**: Project README template with placeholders
- **docs_template.md**: Generic documentation template
- **help_template.md**: Help/FAQ template

Templates use `{PLACEHOLDER}` syntax for variable substitution.

## Translation Guidelines

### Terminology Consistency

1. **Always use glossary**: Refer to `glossary_*.yaml` for standard translations
2. **Technical accuracy**: Preserve TRIZ methodology accuracy
3. **Cultural adaptation**: Adapt examples while maintaining technical correctness
4. **Cross-references**: Maintain consistency across all documents

### Quality Standards

- ✅ **UTF-8 encoding**: All files must use UTF-8
- ✅ **YAML syntax**: Validate YAML files before committing
- ✅ **RTL support**: Arabic content properly formatted for right-to-left
- ✅ **No machine translation**: Human review required for all translations
- ✅ **Native speaker review**: Final review by native speaker

### Adding New Terms

1. Add term to `glossary_en.yaml` first (canonical source)
2. Run `sync_translations.py validate` to detect missing translations
3. Add translations to other glossaries (`glossary_zh.yaml`, `glossary_ru.yaml`, `glossary_ar.yaml`)
4. Ensure consistent structure across all files
5. Validate with `sync_translations.py validate`

### Updating Existing Terms

1. Update English definition in `glossary_en.yaml`
2. Run `sync_translations.py sync` to detect changes
3. Review and update translations in other languages
4. Ensure examples and notes are synchronized

## Testing Translations

Multilingual tests are located in `tests/multilingual/`:

```bash
# Run all multilingual tests
pytest tests/multilingual/

# Test specific language
pytest tests/multilingual/test_chinese_support.py
pytest tests/multilingual/test_russian_support.py
pytest tests/multilingual/test_arabic_support.py

# Test terminology consistency
pytest tests/multilingual/test_terminology_consistency.py
```

## Contributing Translations

We welcome translation contributions! Please see:

1. **CONTRIBUTING.md**: General contribution guidelines
2. **Multilingual Workflow** section in CONTRIBUTING.md
3. **Translation Guidelines** above

### Translation Workflow for Contributors

1. Fork the repository
2. Create branch: `i18n/{language}-translation-update`
3. Update glossary or documentation files
4. Run `sync_translations.py validate`
5. Submit pull request with translation updates
6. Wait for native speaker review

## Language Support Status

| Language | Glossary | Docs | Landing Page | Tests | Status |
|----------|----------|------|--------------|-------|--------|
| 🇬🇧 English (en) | ✅ | ✅ | ✅ | ✅ | Canonical |
| 🇨🇳 Chinese (zh) | ✅ | 🚧 | ✅ | ✅ | Active |
| 🇷🇺 Russian (ru) | ✅ | 🚧 | ✅ | ✅ | Active |
| 🇸🇦 Arabic (ar) | ✅ | 🚧 | ✅ | ✅ | NEW |

**Legend**:
- ✅ Complete
- 🚧 In Progress
- ❌ Not Started

## Resources

### TRIZ Terminology Sources

- **English**: Altshuller Foundation, Technical Innovation Center
- **Russian**: Original Altshuller publications (authoritative)
- **Chinese**: Chinese TRIZ literature and academic publications
- **Arabic**: Technical Arabic engineering terminology standards

### Translation Tools

- **Crowdin**: Translation management platform
- **sync_translations.py**: Custom synchronization script
- **GitHub Actions**: Automated workflows

## Contact

For translation questions or issues:

- **GitHub Issues**: [Translation Update Template](https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine/issues/new?template=translation_update.yml)
- **Discussions**: [GitHub Discussions](https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine/discussions)

---

**Heinrich: Making TRIZ accessible to innovators worldwide** 🌍🚀
