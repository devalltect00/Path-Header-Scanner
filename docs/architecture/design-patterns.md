<!-- docs/path-header/design_patterns.md -->

# docs/path-header/design_patterns.md

# Design Patterns

This document explains design patterns used in the project.

---

# Strategy Pattern

The most important pattern used in this project.

Language-specific behavior is isolated into strategies.

Example:

```python
PythonLanguageStrategy
JavaScriptLanguageStrategy
PhpLanguageStrategy
```

Benefits:

- scalability
- cleaner code
- easier testing
- extension support

---

# Service Layer Pattern

Core services isolate responsibilities.

Examples:

- FileScanner
- FileUpdater
- FileProcessor

Benefits:

- maintainability
- separation of concerns
- reusable logic

---

# DTO / Data Model Pattern

Structured result objects are implemented using dataclasses.

Example:

```python
FileProcessResult
```

Benefits:

- predictable structure
- easier testing
- cleaner APIs

---

# Composition Over Inheritance

The project prefers composition where possible.

Example:

```python
FileProcessor
    -> FileUpdater
```

instead of deep inheritance trees.

---

# Why These Patterns?

The project is designed to remain:

- easy to extend
- easy to test
- easy to maintain
- language-independent
