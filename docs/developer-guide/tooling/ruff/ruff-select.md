# Ruff `select`

```
select = [
    "E",
    "F",
    "I",
    "UP",
    "B",
    "W"
]
```

These enable rule groups.

Think of Ruff as combining MANY older Python tools into one.

---

# Meaning of Each

## `"E"` → pycodestyle Errors

Style errors.

Examples:

- indentation problems
- whitespace problems
- syntax-style violations

Example:

`x=1`

becomes:

`x = 1`

---

# `"W"` → pycodestyle Warnings

```toml id="pw1jlwm"
"W"
```

Warnings from pycodestyle.

Examples:

- trailing whitespace
- blank line issues
- line wrapping warnings

---

## Difference Between E and W

Historically:

| Type | Meaning  |
| ---- | -------- |
| E    | Errors   |
| W    | Warnings |

But in practice many teams enable both.

---

# `"F"` → Pyflakes

```toml id="8jlwmz"
"F"
```

Detects logical problems.

VERY important.

Examples:

- unused imports
- undefined variables
- duplicate variables

Example:

`import os`

Unused import → warning.

---

# `"I"` → Import Sorting (isort)

```toml id="jlwmzw"
"I"
```

Automatically sorts imports.

Example:

Before:

```import sysimport os

```

After:

```import osimport sys

```

VERY useful.

---

# `"UP"` → pyupgrade

```toml id="jlwmzs"
"UP"
```

Modernizes Python syntax.

Example:

Old:

`list()`

Modern:

`[]`

Or:

- old typing syntax
- outdated patterns
- modern Python upgrades

VERY nice rule group.

---

# `"B"` → flake8-bugbear

```toml id="jlwmzv"
"B"
```

Detects suspicious/bug-prone code.

VERY valuable professionally.

Examples:

- mutable default arguments
- incorrect exception handling
- risky patterns

Example BAD:

```def func(data=[]):    pass

```

Bugbear warns this is dangerous.

---
