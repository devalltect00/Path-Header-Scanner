<!-- docs/path-header/diagrams.md -->

# System Diagrams

This document contains Mermaid diagrams describing the architecture, workflow, and execution flow of Path Header Scanner.

---

# High-Level Architecture

## Mermaid

```mermaid
flowchart TD

    A[CLI Command] --> B[Path Resolution]

    B --> C[FileScanner]

    C --> D[Discovered Files]

    D --> E[FileProcessor]

    E --> F[Resolve Language Strategy]

    F --> G[Language Strategy]

    G --> H[FileUpdater]

    H --> I[Validate Header]

    I --> J{Header State}

    J -->|Valid| K[Return Valid Result]

    J -->|Missing| L[Insert Header]

    J -->|Invalid| M[Replace Header]

    L --> N[Write Updated File]

    M --> N

    N --> O[FileProcessResult]

    K --> O

    O --> P[Summary Output]
```

---

# CLI Flow

## Mermaid

```mermaid
flowchart TD

    A[User Command] --> B[Typer CLI]

    B --> C[Parse Arguments]

    C --> D[Resolve Target Path]

    D --> E[Initialize Strategies]

    E --> F[Create FileScanner]

    F --> G[Scan Files]

    G --> H[Create FileProcessor]

    H --> I[Process Files]

    I --> J[Display Summary]
```

---

# Path Resolution Flow

## Mermaid

```mermaid
flowchart TD

    A[Input Path] --> B{Absolute Path?}

    B -->|Yes| C[Use Absolute Path]

    B -->|No| D{Working Directory Provided?}

    D -->|Yes| E[Resolve Using Workdir]

    D -->|No| F[Use Current Working Directory]

    F --> G{Exists?}

    G -->|No| H{Running in Docker?}

    H -->|Yes| I[Use Docker Workspace]

    H -->|No| J[Use Direct Relative Path]

    G -->|Yes| K[Resolved Path]

    C --> K
    E --> K
    I --> K
    J --> K
```

---

# Scanner Flow

## Mermaid

```mermaid
flowchart TD

    A[Root Directory] --> B[Recursive Scan]

    B --> C{Is File?}

    C -->|No| D[Skip]

    C -->|Yes| E{Ignored Directory?}

    E -->|Yes| D

    E -->|No| F{Supported Extension?}

    F -->|No| D

    F -->|Yes| G[Add to Matched Files]

    G --> H[Return Sorted Files]
```

---

# Strategy Resolution Flow

## Mermaid

```mermaid
flowchart TD

    A[File Extension] --> B{Strategy Match}

    B -->|.py| C[PythonLanguageStrategy]

    B -->|.js/.jsx| D[JavaScriptLanguageStrategy]

    B -->|.ts/.tsx| D

    B -->|.php| E[PhpLanguageStrategy]

    B -->|.html/.htm| F[HtmlLanguageStrategy]

    B -->|.sh/.bash/.zsh| G[ShellLanguageStrategy]

    B -->|.md/.markdown| H[MarkdownLanguageStrategy]
```

---

# File Processing Flow

## Mermaid

```mermaid
flowchart TD

    A[Process File] --> B[Read File Content]

    B --> C[Split Into Lines]

    C --> D[Extract Existing Header]

    D --> E[Generate Expected Header]

    E --> F{Header Match?}

    F -->|Yes| G[Return VALID]

    F -->|No| H{Header Exists?}

    H -->|Yes| I[Replace Header]

    H -->|No| J[Insert Header]

    I --> K{Apply Changes?}

    J --> K

    K -->|Yes| L[Write File]

    K -->|No| M[Dry Run]

    L --> N[Return Result]

    M --> N
```

---

# Header Generation Flow

## Mermaid

```mermaid
flowchart TD

    A[File Path] --> B{Include Target Directory?}

    B -->|Yes| C[Relative to Parent Directory]

    B -->|No| D[Relative to Target Directory]

    C --> E[Build Header]

    D --> E

    E --> F[Formatted Header]
```

---

# Header State Decision Flow

## Mermaid

```mermaid
flowchart TD

    A[Extract Header] --> B{Header Exists?}

    B -->|No| C[INSERTED]

    B -->|Yes| D{Header Matches Expected?}

    D -->|Yes| E[VALID]

    D -->|No| F[UPDATED]
```

---

# Python Header Preservation Flow

## Mermaid

```mermaid
flowchart TD

    A[Read Python File] --> B{Has Shebang?}

    B -->|Yes| C[Preserve Shebang]

    B -->|No| D[Continue]

    C --> E{Has Encoding Declaration?}

    D --> E

    E -->|Yes| F[Preserve Encoding]

    E -->|No| G[Insert Header]

    F --> G
```

---

# PHP Header Preservation Flow

## Mermaid

```mermaid
flowchart TD

    A[Read PHP File] --> B{Has Shebang?}

    B -->|Yes| C[Preserve Shebang]

    B -->|No| D[Continue]

    C --> E{Has PHP Opening Tag?}

    D --> E

    E -->|Yes| F[Preserve <?php]

    E -->|No| G[Insert Header]

    F --> G
```

---

# Logging Flow

## Mermaid

```mermaid
flowchart TD

    A[File Result] --> B{Result Status}

    B -->|VALID| C[DEBUG Log]

    B -->|UPDATED| D[INFO Log]

    B -->|INSERTED| E[INFO Log]

    B -->|FAILED| F[ERROR Log]
```

---

# Docker Workflow

## Mermaid

```mermaid
flowchart TD

    A[Dockerfile] --> B[Docker Image]

    B --> C[Docker Container]

    C --> D[Mounted Workspace]

    D --> E[Run CLI Command]

    E --> F[Scan Files]

    F --> G[Update Mounted Files]
```

---

# Docker Compose Workflow

## Mermaid

```mermaid
flowchart TD

    A[docker-compose.yml] --> B[Compose Service]

    B --> C[Container Startup]

    C --> D[Workspace Mount]

    D --> E[CLI Execution]

    E --> F[Scanner Workflow]
```

---

# Makefile Workflow

## Mermaid

```mermaid
flowchart TD

    A[make docker-debug] --> B[Docker Run Command]

    B --> C[Mount Workspace]

    C --> D[Set Working Directory]

    D --> E[Execute Scanner]

    E --> F[Display Results]
```

---

# Test Architecture

## Mermaid

```mermaid
flowchart TD

    A[Unit Tests] --> B[Language Strategies]

    A --> C[FileUpdater]

    A --> D[FileScanner]

    A --> E[Resolver]

    F[Integration Tests] --> G[Full Processing Flow]

    H[CLI Tests] --> I[Typer Commands]

    J[Docker Tests] --> K[Container Execution]
```

---

# Error Handling Flow

## Mermaid

```mermaid
flowchart TD

    A[Process File] --> B{Exception Raised?}

    B -->|No| C[Return Success Result]

    B -->|Yes| D[Log Exception]

    D --> E[Return FAILED Result]
```

---

# Result Aggregation Flow

## Mermaid

```mermaid
flowchart TD

    A[Process Files] --> B[Collect Results]

    B --> C[Count VALID]

    B --> D[Count UPDATED]

    B --> E[Count INSERTED]

    B --> F[Count FAILED]

    C --> G[Generate Summary]

    D --> G

    E --> G

    F --> G
```

---

# Future Architecture Possibilities

## Mermaid

```mermaid
flowchart TD

    A[Current Scanner] --> B[Parallel Processing]

    A --> C[Configuration File Support]

    A --> D[Template Engine]

    A --> E[Pre-commit Integration]

    A --> F[Git Hook Support]

    A --> G[Progress Bars]

    A --> H[Plugin System]
```

---

# Notes

- Diagrams use Mermaid syntax.
- Diagrams are intended for architecture visualization.
- Flows may evolve as the project grows.
- Diagrams are compatible with GitHub Markdown rendering.
