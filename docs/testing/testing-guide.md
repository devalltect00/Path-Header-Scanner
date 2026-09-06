<!-- docs/path-header/testing.md -->

# docs/path-header/testing.md

# Testing Guide

This document explains testing strategy and test organization.

---

# Testing Philosophy

The project prioritizes testing core logic instead of CLI wrappers.

Most tests focus on:

- updater logic
- scanner behavior
- strategy behavior

---

# Test Structure

```text
tests/
├── cli/
├── core/
├── integration/
└── languages/
```

---

# Test Types

| Type | Purpose |
|---|---|
| Unit Tests | Individual functions/classes |
| Integration Tests | Full workflow validation |
| CLI Tests | Command behavior |

---

# Running Tests

## All Tests

```bash
pytest
```

---

## Coverage

```bash
pytest --cov=app
```

---

## Specific Tests

```bash
pytest tests/core
```

---

# Important Fixtures

The project heavily uses:

```python
tmp_path
```

for isolated filesystem testing.

---

# Coverage Goals

| Area | Goal |
|---|---|
| Updater | 95%+ |
| Strategies | 90%+ |
| Scanner | 85%+ |

---

# Future Improvements

Potential future additions:

- golden file testing
- diff validation
- permission error tests
- encoding edge cases
