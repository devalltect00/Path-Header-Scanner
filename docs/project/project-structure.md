```
=====
/root (project type: python)
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Makefile
├── Makefile.deprecated
├── app
│   ├── __main__.py
│   ├── cli
│   │   └── main.py
│   ├── constants
│   │   └── docker.py
│   ├── core
│   │   ├── processor.py
│   │   ├── scanner.py
│   │   └── updater.py
│   ├── languages
│   │   ├── base.py
│   │   ├── html.py
│   │   ├── javascript.py
│   │   ├── markdown.py
│   │   ├── php.py
│   │   ├── python.py
│   │   └── shell.py
│   ├── models
│   │   ├── enums.py
│   │   └── result.py
│   └── utils
│       ├── logging.py
│       ├── paths.py
│       └── resolver.py
├── app_test
│   ├── __main__.py
│   ├── cli
│   │   └── main.py
│   ├── core
│   │   ├── processor.py
│   │   ├── scanner.py
│   │   └── updater.py
│   ├── languages
│   │   ├── base.py
│   │   ├── html.py
│   │   ├── javascript.py
│   │   ├── php.py
│   │   ├── python.py
│   │   └── shell.py
│   ├── models
│   │   ├── enums.py
│   │   └── result.py
│   └── utils
│       ├── logging.py
│       └── paths.py
├── docker-compose.yml
├── docs
│   └── path-header
│       ├── README.md
│       ├── design_patterns.md
│       ├── developer_guide.md
│       ├── diagrams.md
│       ├── docker.md
│       ├── languages
│       │   ├── markdown_language_strategy.md
│       │   └── supported_languages.md
│       ├── testing.md
│       ├── user_guide.md
│       └── workflow.md
├── example_command.txt
├── pyproject.toml
├── requirements.txt
├── tests
│   ├── __init__.py
│   ├── cli
│   │   └── test_main.py
│   ├── conftest.py
│   ├── core
│   │   ├── test_processor.py
│   │   ├── test_scanner.py
│   │   └── test_updater.py
│   ├── integration
│   │   └── test_full_scan.py
│   └── languages
│       ├── test_html_strategy.py
│       ├── test_javascript_strategy.py
│       ├── test_php_strategy.py
│       ├── test_python_strategy.py
│       └── test_shell_strategy.py
└── tools
    ├── __init__.py
    ├── generate_ignore
    │   ├── __init__.py
    │   ├── __version__.py
    │   └── generate_ignore_files.py
    └── project_structure
        ├── __init__.py
        ├── __version__.py
        └── print_project_structure.py
```
