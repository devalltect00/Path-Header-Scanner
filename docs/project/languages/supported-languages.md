<!-- docs/path-header/languages/supported_languages.md -->

# Supported Languages

This document lists all supported languages and file types handled by Path Header Scanner.

---

# Overview

Path Header Scanner supports multiple source file types using language-specific strategies located in:

```text
app/languages/
```

Each language strategy is responsible for:

- supported extensions
- comment syntax
- header extraction
- insertion behavior
- special-line preservation

---

# Supported Strategies

| Strategy File | Language | Extensions |
|---|---|---|
| `python.py` | Python | `.py` |
| `javascript.py` | JavaScript / TypeScript | `.js`, `.jsx`, `.ts`, `.tsx` |
| `shell.py` | Shell Scripts | `.sh`, `.bash`, `.zsh` |
| `php.py` | PHP | `.php` |
| `html.py` | HTML | `.html`, `.htm` |
| `markdown.py` | Markdown | `.md`, `.markdown` |

---

# Python

Strategy:

```text
app/languages/python.py
```

Supported extensions:

```text
.py
```

Header format:

```python
# app/main.py
```

Features:

- shebang preservation
- encoding declaration preservation

---

# JavaScript / TypeScript

Strategy:

```text
app/languages/javascript.py
```

Supported extensions:

```text
.js
.jsx
.ts
.tsx
```

Header format:

```javascript
// app/main.js
```

Features:

- JavaScript support
- React support
- TypeScript support

---

# Shell Scripts

Strategy:

```text
app/languages/shell.py
```

Supported extensions:

```text
.sh
.bash
.zsh
```

Header format:

```bash
# scripts/build.sh
```

Features:

- shebang preservation

---

# PHP

Strategy:

```text
app/languages/php.py
```

Supported extensions:

```text
.php
```

Header format:

```php
<?php
// app/index.php
```

Features:

- PHP opening tag preservation
- shebang preservation

---

# HTML

Strategy:

```text
app/languages/html.py
```

Supported extensions:

```text
.html
.htm
```

Header format:

```html
<!-- app/templates/index.html -->
```

Features:

- HTML comment support
- safe HTML header detection

---

# Markdown

Strategy:

```text
app/languages/markdown.py
```

Supported extensions:

```text
.md
.markdown
```

Header format:

```md
<!-- docs/path-header/user_guide.md -->
```

Features:

- HTML comment syntax
- safe Markdown heading handling
- legacy `# path` migration support
- GitHub-compatible formatting

---

# Common Strategy Architecture

All strategies inherit from:

```python
BaseLanguageStrategy
```

located in:

```text
app/languages/base.py
```

---

# Base Strategy Responsibilities

Each strategy implements:

| Method | Purpose |
|---|---|
| `extensions` | Supported file extensions |
| `comment_prefix` | Header comment syntax |
| `extract_header()` | Existing header detection |
| `build_header()` | Header generation |
| `get_insertion_index()` | Optional insertion behavior |

---

# Example Strategy

```python
class PythonLanguageStrategy(
    BaseLanguageStrategy
):
```

---

# Header Style Reference

| Language | Header Style |
|---|---|
| Python | `# path/to/file.py` |
| JavaScript | `// path/to/file.js` |
| Shell | `# path/to/script.sh` |
| PHP | `// path/to/file.php` |
| HTML | `<!-- path/to/file.html -->` |
| Markdown | `<!-- path/to/file.md -->` |

---

# Special Handling

| Language | Special Preservation |
|---|---|
| Python | shebang, encoding |
| Shell | shebang |
| PHP | shebang, `<?php` |
| Markdown | heading safety |

---

# Future Language Support

Potential future additions:

- CSS
- SCSS
- YAML
- TOML
- JSONC
- Lua
- Rust
- Go
- Java
- C#
- C/C++
- Vue
- Svelte

---

# Notes

- All generated paths use POSIX separators.
- Strategies are isolated and reusable.
- Markdown uses HTML comments intentionally.
- Each strategy may customize insertion behavior independently.
