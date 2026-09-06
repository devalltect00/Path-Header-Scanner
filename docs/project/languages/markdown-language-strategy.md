<!-- docs/path-header/languages/markdown_language_strategy.md -->

# Markdown Support

Path Header Scanner supports Markdown documentation files.

Supported extensions:

- `.md`
- `.markdown`

Markdown support is implemented using:

```python
MarkdownLanguageStrategy
```

---

# Why Markdown Uses HTML Comments

Markdown files commonly use:

```md
# Title
```

for headings.

Using standard `#`-style headers would conflict with normal Markdown documents.

Example problem:

```md
# Developer Guide
```

could incorrectly be interpreted as a path header.

To avoid this conflict, Markdown files use HTML comments instead.

---

# Markdown Header Format

Generated headers use:

```md
<!-- docs/path-header/user_guide.md -->
```

instead of:

```md
# docs/path-header/user_guide.md
```

Benefits:

- avoids heading conflicts
- GitHub-compatible
- invisible in rendered Markdown
- cleaner documentation rendering
- safer detection logic

---

# Example

Before:

```md
# Developer Guide

This document explains...
```

After:

```md
<!-- docs/path-header/developer_guide.md -->

# Developer Guide

This document explains...
```

---

# Supported Behavior

Markdown support includes:

- missing header insertion
- invalid header replacement
- legacy header migration
- path normalization

---

# Invalid Header Replacement

Incorrect Markdown headers are automatically corrected.

Example:

Before:

```md
<!-- docs/path-header/developer_gu.md -->
```

After:

```md
<!-- docs/path-header/developer_guide.md -->
```

---

# Legacy Header Migration

The scanner also supports migration from old `# path` style Markdown headers.

Example:

Before:

```md
# docs/path-header/developer_gu.md
```

After:

```md
<!-- docs/path-header/developer_guide.md -->
```

This allows older documentation styles to be normalized automatically.

---

# Safe Heading Detection

Normal Markdown headings are NOT treated as path headers.

Example:

```md
# Developer Guide
```

is preserved safely.

The scanner only treats lines as legacy Markdown headers if they match path-like patterns.

Examples of detected legacy headers:

```md
# docs/path-header/user_guide.md
```

```md
# app/core/main.py
```

Examples NOT detected:

```md
# Overview
```

```md
# Installation
```

```md
# Docker Guide
```

---

# Header Detection Logic

Markdown detection supports:

| Format | Supported |
|---|---|
| `<!-- path -->` | Yes |
| `# path/to/file.ext` | Yes (legacy migration) |
| `# Title` | No |

---

# Insertion Behavior

Headers are inserted at the beginning of Markdown files.

A blank line is automatically added after the header.

Example:

```md
<!-- docs/path-header/README.md -->

# Path Header Scanner
```

---

# Include Target Directory

Example:

```bash
path-header-scanner scan docs \
    --include-target-directory
```

Result:

```md
<!-- docs/path-header/user_guide.md -->
```

---

# Exclude Target Directory

Example:

```bash
path-header-scanner scan docs \
    --exclude-target-directory
```

Result:

```md
<!-- path-header/user_guide.md -->
```

---

# Example Markdown Strategy

Example implementation:

```python
class MarkdownLanguageStrategy(
    BaseLanguageStrategy
):
```

Features:

- HTML comment syntax
- legacy migration support
- safe heading detection
- GitHub-compatible formatting

---

# Recommended Usage

Recommended workflow:

1. run dry-run first
2. review documentation updates
3. apply changes afterward

Example:

```bash
path-header-scanner scan docs
```

Then:

```bash
path-header-scanner scan docs --apply
```

---

# Notes

- Markdown headers use HTML comments intentionally.
- Markdown headings remain unaffected.
- Legacy `# path` headers are migrated automatically.
- Markdown rendering remains clean and unchanged.
