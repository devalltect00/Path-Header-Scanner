# tests/integration/test_full_scan.py

"""
Full integration tests.

This module validates:
- end-to-end scanning
- multi-language processing
- recursive directory handling
- real filesystem updates
- complete workflow execution
"""

from pathlib import Path

from app.constants.path import (
    THIS_PROJECT_SOURCE,
)
from app.core.scan.processor import FileProcessor
from app.core.scan.scanner import FileScanner
from app.languages.html import HtmlLanguageStrategy
from app.languages.javascript import (
    JavaScriptLanguageStrategy,
)
from app.languages.php import PhpLanguageStrategy
from app.languages.python import (
    PythonLanguageStrategy,
)
from app.languages.shell import ShellLanguageStrategy
from app.models.enums import FileStatus

INCLUDE_TARGET_DIRECTORY = False


def test_full_project_scan_and_update(
    tmp_path: Path,
) -> None:
    """
    Test full multi-language project scan.

    Args:
        tmp_path (Path):
            Temporary pytest directory.

    Returns:
        None
    """

    # =========================
    # Create directories
    # =========================
    app_directory = tmp_path / THIS_PROJECT_SOURCE
    scripts_directory = tmp_path / "scripts"
    templates_directory = tmp_path / "templates"

    app_directory.mkdir()
    scripts_directory.mkdir()
    templates_directory.mkdir()

    # =========================
    # Create Python file
    # =========================
    python_file = app_directory / "main.py"

    python_file.write_text(
        'print("hello")\n',
        encoding="utf-8",
    )

    # =========================
    # Create JavaScript file
    # =========================
    javascript_file = app_directory / "main.js"

    javascript_file.write_text(
        'console.log("hello");\n',
        encoding="utf-8",
    )

    # =========================
    # Create Shell file
    # =========================
    shell_file = scripts_directory / "run.sh"

    shell_file.write_text(
        ("#!/bin/bash\necho hello\n"),
        encoding="utf-8",
    )

    # =========================
    # Create HTML file
    # =========================
    html_file = templates_directory / "index.html"

    html_file.write_text(
        "<html></html>\n",
        encoding="utf-8",
    )

    # =========================
    # Create PHP file
    # =========================
    php_file = app_directory / "index.php"

    php_file.write_text(
        ('<?php\necho "hello";\n'),
        encoding="utf-8",
    )

    strategies = [
        PythonLanguageStrategy(),
        JavaScriptLanguageStrategy(),
        ShellLanguageStrategy(),
        HtmlLanguageStrategy(),
        PhpLanguageStrategy(),
    ]

    scanner = FileScanner(
        root_directory=tmp_path,
        strategies=strategies,
    )

    files = scanner.scan()

    processor = FileProcessor(
        root_directory=tmp_path,
        strategies=strategies,
        include_target_directory=INCLUDE_TARGET_DIRECTORY,
    )

    results = processor.process_files(
        files=files,
        apply_changes=True,
    )

    # =========================
    # Validate results
    # =========================
    assert len(results) == 5

    assert all(result.status == FileStatus.INSERTED for result in results)

    # =========================
    # Validate Python header
    # =========================
    assert "# app/main.py" in python_file.read_text(
        encoding="utf-8",
    )

    # =========================
    # Validate JavaScript header
    # =========================
    assert "// app/main.js" in javascript_file.read_text(
        encoding="utf-8",
    )

    # =========================
    # Validate Shell header
    # =========================
    shell_content = shell_file.read_text(
        encoding="utf-8",
    )

    shell_lines = shell_content.splitlines()

    assert shell_lines[0] == "#!/bin/bash"

    assert shell_lines[1] == "# scripts/run.sh"

    # =========================
    # Validate HTML header
    # =========================
    assert "<!-- templates/index.html -->" in html_file.read_text(
        encoding="utf-8",
    )

    # =========================
    # Validate PHP header
    # =========================
    php_content = php_file.read_text(
        encoding="utf-8",
    )

    php_lines = php_content.splitlines()

    assert php_lines[0] == "<?php"

    assert php_lines[1] == "// app/index.php"
