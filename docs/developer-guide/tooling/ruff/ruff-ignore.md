These are not really “errors” in the crashing sense.

Most are:

- style improvements
- modernization suggestions
- formatting warnings
- lint quality checks

from Ruff.

This is normal for first-time Ruff adoption.

---

# Important Understanding

Ruff combines MANY older Python tools into one.

So these codes come from:

- pyflakes
- pyupgrade
- pycodestyle
- isort
- flake8-bugbear
- etc.

---

# Main Codes Explained

| Code  | Meaning               | Source      |
| ----- | --------------------- | ----------- |
| I001  | import sorting        | isort       |
| F401  | unused import         | pyflakes    |
| W292  | no newline EOF        | pycodestyle |
| W293  | whitespace blank line | pycodestyle |
| UP045 | modern type syntax    | pyupgrade   |
| UP042 | modern enum syntax    | pyupgrade   |

---

# 1. I001 → Import Sorting

```text id="jlwm4a"
I001 Import block is un-sorted or un-formatted
```

Means:

- imports not organized properly

Example:

BAD:

```python id="jlwm4b"
import sys
import os
```

GOOD:

```python id="jlwm4c"
import os
import sys
```

---

# Auto Fix

Ruff can fix automatically:

```bash id="jlwm4d"
ruff check . --fix
```

VERY convenient.

---

# 2. F401 → Unused Import

```text id="jlwm4e"
F401 `pathlib.Path` imported but unused
```

Means:

```python id="jlwm4f"
from pathlib import Path
```

exists but never used.

---

# Fix

Either:

- remove import
- or actually use it

---

# 3. W293 → Blank Line Contains Whitespace

```text id="jlwm4g"
W293 Blank line contains whitespace
```

Means:

- empty line still contains spaces/tabs

BAD:

```python id="jlwm4h"
x = 1
<spaces here>
y = 2
```

---

# Fix

Delete spaces on empty line.

Most formatters fix automatically.

---

# 4. W292 → No Newline at End of File

```text id="jlwm4i"
W292 No newline at end of file
```

Means:

- file should end with blank newline

VERY old UNIX convention.

---

# Why It Matters

Some tools:

- Git
- diff
- shells
- editors

behave better with final newline.

VERY common rule.

---

# Auto Fix

Usually formatter fixes automatically.

---

# 5. UP042 → Use `StrEnum`

This:

```python id="jlwm4j"
class FileStatus(str, Enum):
```

can become:

```python id="jlwm4k"
from enum import StrEnum

class FileStatus(StrEnum):
```

Modern Python improvement.

---

# Why?

`StrEnum` was added to Python.

Cleaner and more explicit.

---

# 6. UP045 → `Optional[str]`

This is the one you asked about.

---

# What `Optional[str]` Means

This:

```python id="jlwm4l"
Optional[str]
```

means:

```python id="jlwm4m"
str | None
```

Exactly the same thing.

---
