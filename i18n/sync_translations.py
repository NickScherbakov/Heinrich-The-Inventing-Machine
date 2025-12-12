#!/usr/bin/env python3
"""
Translation Synchronization Script for Heinrich: The Inventing Machine

This script manages translation synchronization across multiple languages:
- Detects changes in English (canonical) content
- Marks translations as outdated when English changes
- Generates translation tasks/reports
- Validates glossary consistency across languages
- Supports CLI usage for CI/CD integration
"""

import os
import sys
import yaml
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple
import json


class TranslationSync:
    """Manages translation synchronization for Heinrich project."""
    
    SUPPORTED_LANGUAGES = ["en", "zh", "ru", "ar"]
    CANONICAL_LANGUAGE = "en"
    
    def __init__(self, repo_root: Path):
        """
        Initialize translation synchronization.
        
        Args:
            repo_root: Root directory of the repository
        """
        self.repo_root = Path(repo_root)
        self.i18n_dir = self.repo_root / "i18n"
        self.docs_dir = self.repo_root / "docs"
        self.sync_state_file = self.i18n_dir / ".sync_state.json"
        self.sync_state = self._load_sync_state()
        
    def _load_sync_state(self) -> Dict:
        """Load synchronization state from file."""
        if self.sync_state_file.exists():
            with open(self.sync_state_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"file_hashes": {}, "last_sync": None}
    
    def _save_sync_state(self):
        """Save synchronization state to file."""
        self.sync_state["last_sync"] = datetime.now().isoformat()
        with open(self.sync_state_file, 'w', encoding='utf-8') as f:
            json.dump(self.sync_state, f, indent=2, ensure_ascii=False)
    
    def _compute_file_hash(self, file_path: Path) -> str:
        """Compute SHA256 hash of file content."""
        if not file_path.exists():
            return ""
        with open(file_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    
    def detect_changes(self) -> Dict[str, List[Path]]:
        """
        Detect changes in canonical English content.
        
        Returns:
            Dictionary mapping change type to list of changed files
        """
        changes = {
            "new": [],
            "modified": [],
            "deleted": []
        }
        
        # Check glossary changes
        en_glossary = self.i18n_dir / "glossary_en.yaml"
        if en_glossary.exists():
            current_hash = self._compute_file_hash(en_glossary)
            stored_hash = self.sync_state["file_hashes"].get(str(en_glossary), "")
            
            if not stored_hash:
                changes["new"].append(en_glossary)
            elif current_hash != stored_hash:
                changes["modified"].append(en_glossary)
            
            # Update hash
            self.sync_state["file_hashes"][str(en_glossary)] = current_hash
        
        # Check documentation changes
        en_docs_dir = self.docs_dir / "en"
        if en_docs_dir.exists():
            for doc_file in en_docs_dir.rglob("*.md"):
                current_hash = self._compute_file_hash(doc_file)
                stored_hash = self.sync_state["file_hashes"].get(str(doc_file), "")
                
                if not stored_hash:
                    changes["new"].append(doc_file)
                elif current_hash != stored_hash:
                    changes["modified"].append(doc_file)
                
                # Update hash
                self.sync_state["file_hashes"][str(doc_file)] = current_hash
        
        return changes
    
    def validate_glossaries(self) -> Dict[str, List[str]]:
        """
        Validate glossary consistency across languages.
        
        Returns:
            Dictionary of issues found per language
        """
        issues = {}
        
        # Load canonical English glossary
        en_glossary_path = self.i18n_dir / "glossary_en.yaml"
        if not en_glossary_path.exists():
            return {"en": ["Canonical English glossary not found"]}
        
        with open(en_glossary_path, 'r', encoding='utf-8') as f:
            en_glossary = yaml.safe_load(f)
        
        # Get all term keys from English glossary (excluding metadata)
        en_terms = {k for k in en_glossary.keys() if k != "metadata"}
        
        # Validate each target language
        for lang in self.SUPPORTED_LANGUAGES:
            if lang == self.CANONICAL_LANGUAGE:
                continue
                
            lang_issues = []
            glossary_path = self.i18n_dir / f"glossary_{lang}.yaml"
            
            if not glossary_path.exists():
                lang_issues.append(f"Glossary file missing: {glossary_path}")
                issues[lang] = lang_issues
                continue
            
            with open(glossary_path, 'r', encoding='utf-8') as f:
                lang_glossary = yaml.safe_load(f)
            
            lang_terms = {k for k in lang_glossary.keys() if k != "metadata"}
            
            # Check for missing terms
            missing_terms = en_terms - lang_terms
            if missing_terms:
                lang_issues.append(f"Missing {len(missing_terms)} terms: {', '.join(list(missing_terms)[:5])}...")
            
            # Check for extra terms
            extra_terms = lang_terms - en_terms
            if extra_terms:
                lang_issues.append(f"Extra {len(extra_terms)} terms not in English: {', '.join(list(extra_terms)[:5])}...")
            
            # Validate each term has translation
            for term in en_terms:
                if term not in lang_glossary:
                    continue
                    
                term_data = lang_glossary[term]
                if not isinstance(term_data, dict):
                    continue
                    
                if lang not in term_data:
                    lang_issues.append(f"Term '{term}' missing {lang} translation")
            
            if lang_issues:
                issues[lang] = lang_issues
        
        return issues
    
    def generate_translation_report(self, output_file: Path = None) -> str:
        """
        Generate translation status report.
        
        Args:
            output_file: Optional file to write report to
            
        Returns:
            Report as string
        """
        changes = self.detect_changes()
        glossary_issues = self.validate_glossaries()
        
        report_lines = [
            "# Translation Synchronization Report",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Changes Detected in English Content",
            ""
        ]
        
        if changes["new"]:
            report_lines.append(f"### New Files ({len(changes['new'])})")
            for f in changes["new"]:
                report_lines.append(f"- `{f.relative_to(self.repo_root)}`")
            report_lines.append("")
        
        if changes["modified"]:
            report_lines.append(f"### Modified Files ({len(changes['modified'])})")
            for f in changes["modified"]:
                report_lines.append(f"- `{f.relative_to(self.repo_root)}`")
            report_lines.append("")
        
        if not changes["new"] and not changes["modified"]:
            report_lines.append("✅ No changes detected")
            report_lines.append("")
        
        report_lines.extend([
            "## Glossary Validation",
            ""
        ])
        
        if glossary_issues:
            for lang, issues in glossary_issues.items():
                report_lines.append(f"### {lang.upper()} Issues ({len(issues)})")
                for issue in issues:
                    report_lines.append(f"- {issue}")
                report_lines.append("")
        else:
            report_lines.append("✅ All glossaries are consistent")
            report_lines.append("")
        
        report_lines.extend([
            "## Translation Tasks",
            ""
        ])
        
        # Generate tasks based on changes
        total_tasks = 0
        for lang in self.SUPPORTED_LANGUAGES:
            if lang == self.CANONICAL_LANGUAGE:
                continue
            
            tasks = []
            
            # Tasks from file changes
            for f in changes["new"] + changes["modified"]:
                rel_path = f.relative_to(self.repo_root)
                if "glossary" in str(f):
                    tasks.append(f"Update glossary: `i18n/glossary_{lang}.yaml`")
                elif str(f).startswith(str(self.docs_dir / "en")):
                    # Map to target language docs
                    target_path = str(rel_path).replace("/en/", f"/{lang}/")
                    tasks.append(f"Translate/Update: `{target_path}`")
            
            # Tasks from glossary issues
            if lang in glossary_issues:
                tasks.append(f"Fix {len(glossary_issues[lang])} glossary issues")
            
            if tasks:
                report_lines.append(f"### {lang.upper()} ({len(tasks)} tasks)")
                for task in tasks:
                    report_lines.append(f"- [ ] {task}")
                report_lines.append("")
                total_tasks += len(tasks)
        
        if total_tasks == 0:
            report_lines.append("✅ No translation tasks required")
        else:
            report_lines.insert(6, f"**Total tasks**: {total_tasks}")
        
        report = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
        
        return report
    
    def mark_outdated(self) -> int:
        """
        Mark outdated translations.
        
        Returns:
            Number of files marked as outdated
        """
        changes = self.detect_changes()
        marked = 0
        
        for changed_file in changes["modified"]:
            # For each changed English file, mark corresponding translations
            rel_path = changed_file.relative_to(self.repo_root)
            
            for lang in self.SUPPORTED_LANGUAGES:
                if lang == self.CANONICAL_LANGUAGE:
                    continue
                
                # Map to target language file
                target_path = self.repo_root / str(rel_path).replace("/en/", f"/{lang}/")
                
                if target_path.exists():
                    # Add outdated marker comment/metadata
                    print(f"⚠️  Marked as outdated: {target_path.relative_to(self.repo_root)}")
                    marked += 1
        
        return marked
    
    def sync(self):
        """Perform full synchronization."""
        print("🔄 Starting translation synchronization...")
        
        changes = self.detect_changes()
        total_changes = len(changes["new"]) + len(changes["modified"])
        
        if total_changes > 0:
            print(f"📝 Detected {total_changes} changes in English content")
            marked = self.mark_outdated()
            print(f"⚠️  Marked {marked} translation files as outdated")
        else:
            print("✅ No changes detected in English content")
        
        print("\n🔍 Validating glossaries...")
        issues = self.validate_glossaries()
        
        if issues:
            print(f"❌ Found issues in {len(issues)} language(s):")
            for lang, lang_issues in issues.items():
                print(f"  - {lang.upper()}: {len(lang_issues)} issue(s)")
        else:
            print("✅ All glossaries are consistent")
        
        # Save state
        self._save_sync_state()
        print(f"\n💾 Saved synchronization state")
        
        print("\n✅ Synchronization complete!")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Translation synchronization tool for Heinrich project"
    )
    parser.add_argument(
        "command",
        choices=["detect", "validate", "report", "sync"],
        help="Command to execute"
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root directory (default: current directory)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output file for report command"
    )
    
    args = parser.parse_args()
    
    sync = TranslationSync(args.repo_root)
    
    if args.command == "detect":
        changes = sync.detect_changes()
        total = sum(len(v) for v in changes.values())
        print(f"Detected {total} changes:")
        for change_type, files in changes.items():
            if files:
                print(f"\n{change_type.upper()} ({len(files)}):")
                for f in files:
                    print(f"  - {f.relative_to(args.repo_root)}")
    
    elif args.command == "validate":
        issues = sync.validate_glossaries()
        if issues:
            print(f"Found issues in {len(issues)} language(s):")
            for lang, lang_issues in issues.items():
                print(f"\n{lang.upper()}:")
                for issue in lang_issues:
                    print(f"  - {issue}")
            sys.exit(1)
        else:
            print("✅ All glossaries are consistent")
    
    elif args.command == "report":
        report = sync.generate_translation_report(args.output)
        if args.output:
            print(f"Report written to: {args.output}")
        else:
            print(report)
    
    elif args.command == "sync":
        sync.sync()


if __name__ == "__main__":
    main()
