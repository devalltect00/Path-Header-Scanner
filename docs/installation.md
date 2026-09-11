# Installation

This guide describes the supported installation methods for Path Header Scanner.

## Requirements

- Python 3.11 or later
- pip
- Git (for repository-based installation)

Verify your installation:

```bash
python --version
pip --version
git --version
```

---

## Install from GitHub

Install the latest version directly from GitHub:

```bash
pip install git+https://github.com/devalltect00/Path-Header-Scanner.git
```

Install a specific tag:

```bash
pip install git+https://github.com/devalltect00/Path-Header-Scanner.git@v1.0.1
```

Install a specific branch:

```bash
pip install git+https://github.com/devalltect00/Path-Header-Scanner.git@main
```

---

## Install from GitLab

Install the latest version directly from GitLab:

```bash
pip install git+https://gitlab.com/devalltects-group/path-header-scanner.git
```

Install a specific tag:

```bash
pip install git+https://gitlab.com/devalltects-group/path-header-scanner.git@v1.0.1
```

Install a specific branch:

```bash
pip install git+https://gitlab.com/devalltects-group/path-header-scanner.git@main
```

---

## Install from Release Artifacts

Download release artifacts from GitHub Releases.

Supported formats:

```text
.whl
.tar.gz
```

### Install from Wheel

```bash
pip install path_header_scanner-x.y.z-py3-none-any.whl
```

### Install from Source Distribution

```bash
pip install path_header_scanner-x.y.z.tar.gz
```

---

## Install Using Docker

Build the Docker image:

```bash
docker build -t path-header-scanner .
```

Run the container:

```bash
docker run --rm path-header-scanner
```

---

## Install Using Docker Compose

Start the application:

```bash
docker compose up
```

Run in detached mode:

```bash
docker compose up -d
```

Stop containers:

```bash
docker compose down
```

---

## Development Installation

Clone the repository:

```bash
git clone https://github.com/devalltect00/Path-Header-Scanner.git
```

Enter the project directory:

```bash
cd Path-Header-Scanner
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install development dependencies:

```bash
pip install -e .[dev]
```

Install documentation dependencies:

```bash
pip install -e .[docs]
```

Install all optional dependencies:

```bash
pip install -e .[dev,docs]
```

---

## Verify Installation

Verify the CLI is available:

```bash
path-header-scanner --help
```

Expected output:

```text
Path Header Scanner CLI
...
```

---

## Troubleshooting

### Command not found

Ensure the virtual environment is activated.

### Git not found

Install Git and ensure it is available on your PATH.

### Permission errors

Consider using a virtual environment rather than a system-wide installation.
