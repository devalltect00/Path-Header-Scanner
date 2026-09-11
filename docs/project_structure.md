# Project Structure

# Repository Overview

This repository follows a modular structure commonly used in modern projects.

Common directories include:

- `app/` — Main application source code.
- `.config/` — Project configuration files.
- `.github/` — GitHub-related configuration.
- `.vscode/` — Visual Studio Code workspace settings.
- `docs/` — Project documentation and technical references.
- `tests/` — Automated tests.
- `data/` — Input datasets or static data.
- `output/` — Generated outputs from the application.
- `scripts/` — Utility scripts for development or automation.
- `tools/` — Development tools and automation utilities.
- `templates/` — Reusable templates used by the project.

---

# Repository Structure

(project type: ProjectType.PYTHON)

```text
.
├── .agents
│   └── skills
│       └── follow-path-header-scanner-guidelines
│           └── SKILL.md
├── .config
│   ├── custy
│   │   ├── templates
│   │   │   ├── backups
│   │   │   │   ├── commit
│   │   │   │   └── tag
│   │   │   ├── changelog
│   │   │   │   └── changelog.j2
│   │   │   ├── examples
│   │   │   │   ├── commit_message
│   │   │   │   └── tag_message
│   │   │   ├── commit-message.txt
│   │   │   └── tag-message.txt
│   │   └── config.toml
│   ├── doc_gen
│   │   └── config.toml
│   ├── path_header_scanner
│   │   └── config.toml
│   └── reflow
│       └── config.toml
├── .gitlab
│   ├── ci.yml
│   ├── docker-dev.yml
│   ├── docker-prod.yml
│   ├── python-package.yml
│   └── release.yml
├── .ruff_cache/ ... (collapsed)
├── app
│   ├── cli
│   │   ├── commands
│   │   │   ├── init
│   │   │   │   ├── command.py
│   │   │   │   ├── models.py
│   │   │   │   ├── options.py
│   │   │   │   └── resolver.py
│   │   │   ├── main
│   │   │   │   ├── command.py
│   │   │   │   ├── models.py
│   │   │   │   ├── options.py
│   │   │   │   └── resolver.py
│   │   │   ├── scan
│   │   │   │   ├── command.py
│   │   │   │   ├── models.py
│   │   │   │   ├── options.py
│   │   │   │   └── resolver.py
│   │   │   └── __init__.py
│   │   ├── constants
│   │   │   ├── args.py
│   │   │   ├── completions.py
│   │   │   └── enums.py
│   │   ├── utils
│   │   │   ├── __init__.py
│   │   │   └── versions.py
│   │   ├── errors.py
│   │   └── main.py
│   ├── config
│   │   ├── __init__.py
│   │   └── config_loader.py
│   ├── constants
│   │   ├── docker.py
│   │   └── path.py
│   ├── core
│   │   ├── build/ ... (collapsed)
│   │   ├── initialize
│   │   │   ├── builder
│   │   │   │   └── init_builder.py
│   │   │   ├── models
│   │   │   │   ├── init_config.py
│   │   │   │   ├── init_spec.py
│   │   │   │   ├── initialization_result.py
│   │   │   │   ├── template_dir.py
│   │   │   │   └── template_file.py
│   │   │   ├── presenters
│   │   │   │   └── initialization_presenter.py
│   │   │   ├── services
│   │   │   │   └── scaffold_generator.py
│   │   │   ├── loader.py
│   │   │   ├── main.py
│   │   │   └── registry.py
│   │   ├── scan
│   │   │   ├── processor.py
│   │   │   ├── scanner.py
│   │   │   └── updater.py
│   │   └── shared
│   │       ├── __init__.py
│   │       ├── exceptions.py
│   │       └── result.py
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
│   ├── services
│   │   ├── __init__.py
│   │   └── banner_service.py
│   ├── templates
│   │   ├── __init__.py
│   │   ├── __version__.py
│   │   └── config.toml
│   ├── theme
│   │   ├── __init__.py
│   │   └── theme.py
│   ├── ui
│   │   ├── __init__.py
│   │   ├── console.py
│   │   ├── exceptions.py
│   │   ├── panels.py
│   │   ├── progress.py
│   │   └── tables.py
│   ├── utils
│   │   ├── logging.py
│   │   ├── parsing.py
│   │   ├── paths.py
│   │   └── resolver.py
│   ├── __init__.py
│   ├── __main__.py
│   └── __version__.py
├── docs
│   ├── architecture
│   │   ├── design-patterns.md
│   │   ├── diagrams.md
│   │   └── workflow.md
│   ├── assets
│   │   └── path-header-scanner.png
│   ├── developer-guide
│   │   ├── blackbox
│   │   │   └── ai-development-workflow.md
│   │   ├── tooling
│   │   │   └── ruff
│   │   │       ├── ruff-ignore.md
│   │   │       └── ruff-select.md
│   │   ├── developer-guide.md
│   │   ├── docker-workflow.md
│   │   ├── getting-started.md
│   │   └── make-workflow.md
│   ├── diagrams
│   │   ├── generated
│   │   │   ├── activity-scan.png
│   │   │   ├── architecture-overview.png
│   │   │   ├── cli-menu-design.png
│   │   │   ├── flowchart-error-handling.png
│   │   │   ├── init-workflow.png
│   │   │   ├── models-structure.png
│   │   │   ├── scan-algorithm-flow.png
│   │   │   └── use-case.png
│   │   ├── activity-scan.mmd
│   │   ├── architecture-overview.mmd
│   │   ├── cli-menu-design.mmd
│   │   ├── flowchart-error-handling.mmd
│   │   ├── init-workflow.mmd
│   │   ├── models-structure.mmd
│   │   ├── README.md
│   │   ├── scan-algorithm-flow.mmd
│   │   └── use-case.mmd
│   ├── project
│   │   ├── languages
│   │   │   ├── markdown-language-strategy.md
│   │   │   └── supported-languages.md
│   │   └── project-structure.md
│   ├── reads
│   │   ├── documentation-audit-report.md
│   │   ├── linting-vs-formatting.md
│   │   └── ruff.md
│   ├── testing
│   │   └── testing-guide.md
│   ├── user-guide
│   │   ├── commands.md
│   │   ├── installation-methods.md
│   │   ├── legacy-overview.md
│   │   ├── legacy-user-guide.md
│   │   ├── lifecycle.md
│   │   ├── overview.md
│   │   └── quickstart.md
│   ├── badges.md
│   ├── ci-cd.md
│   ├── configuration.md
│   ├── dry-run.md
│   ├── example_command.txt
│   ├── how-to-use.md
│   ├── index.md
│   ├── infrastructure.md
│   ├── installation.md
│   ├── project_structure.md
│   ├── TODO_tracking_history.md
│   └── usage.md
├── logs/ ... (collapsed)
├── make
│   ├── backups
│   │   └── Full_Makefile - 25082026
│   └── core
│       ├── build_publish
│       │   ├── command.mk
│       │   └── help.mk
│       ├── ci
│       │   ├── command.mk
│       │   └── help.mk
│       ├── cleanup
│       │   ├── command.mk
│       │   └── help.mk
│       ├── compose
│       │   ├── command
│       │   │   ├── common.mk
│       │   │   └── core.mk
│       │   └── help.mk
│       ├── docker
│       │   ├── command
│       │   │   ├── common.mk
│       │   │   └── core.mk
│       │   └── help.mk
│       ├── documentation
│       │   ├── command.mk
│       │   └── help.mk
│       ├── examples
│       │   └── help.mk
│       ├── git
│       │   ├── command.mk
│       │   └── help.mk
│       ├── help
│       │   ├── command.mk
│       │   ├── helper.mk
│       │   └── variable.mk
│       ├── helpers
│       │   ├── common.mk
│       │   └── registry.mk
│       ├── lint_format
│       │   ├── command.mk
│       │   └── help.mk
│       ├── local
│       │   ├── command.mk
│       │   └── help.mk
│       ├── qa
│       │   ├── command.mk
│       │   └── help.mk
│       ├── remote
│       │   ├── command
│       │   │   ├── registry.mk
│       │   │   └── runtime.mk
│       │   └── help.mk
│       ├── setup_install
│       │   ├── command.mk
│       │   └── help.mk
│       ├── testing
│       │   ├── command.mk
│       │   └── help.mk
│       └── variables
│           ├── help.mk
│           └── variable.mk
├── other_venv
│   ├── Include
│   ├── Lib
│   │   └── site-packages
│   │       ├── annotated_doc
│   │       │   ├── __init__.py
│   │       │   ├── main.py
│   │       │   └── py.typed
│   │       ├── annotated_doc-0.0.5.dist-info
│   │       │   ├── licenses
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── annotated_types
│   │       │   ├── __init__.py
│   │       │   ├── py.typed
│   │       │   └── test_cases.py
│   │       ├── annotated_types-0.8.0.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── app
│   │       │   ├── builders
│   │       │   ├── cli
│   │       │   ├── config
│   │       │   ├── constants
│   │       │   ├── core
│   │       │   ├── errors
│   │       │   ├── services
│   │       │   ├── templates
│   │       │   ├── theme
│   │       │   ├── ui
│   │       │   ├── utils
│   │       │   ├── __init__.py
│   │       │   ├── __main__.deprecated.py
│   │       │   ├── __main__.py
│   │       │   └── __version__.py
│   │       ├── colorama
│   │       │   ├── tests
│   │       │   ├── __init__.py
│   │       │   ├── ansi.py
│   │       │   ├── ansitowin32.py
│   │       │   ├── initialise.py
│   │       │   ├── win32.py
│   │       │   └── winterm.py
│   │       ├── colorama-0.4.6.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── custy-2.1.1.dist-info
│   │       │   ├── licenses
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── REQUESTED
│   │       │   ├── top_level.txt
│   │       │   └── WHEEL
│   │       ├── jinja2
│   │       │   ├── __init__.py
│   │       │   ├── _identifier.py
│   │       │   ├── async_utils.py
│   │       │   ├── bccache.py
│   │       │   ├── compiler.py
│   │       │   ├── constants.py
│   │       │   ├── debug.py
│   │       │   ├── defaults.py
│   │       │   ├── environment.py
│   │       │   ├── exceptions.py
│   │       │   ├── ext.py
│   │       │   ├── filters.py
│   │       │   ├── idtracking.py
│   │       │   ├── lexer.py
│   │       │   ├── loaders.py
│   │       │   ├── meta.py
│   │       │   ├── nativetypes.py
│   │       │   ├── nodes.py
│   │       │   ├── optimizer.py
│   │       │   ├── parser.py
│   │       │   ├── py.typed
│   │       │   ├── runtime.py
│   │       │   ├── sandbox.py
│   │       │   ├── tests.py
│   │       │   ├── utils.py
│   │       │   └── visitor.py
│   │       ├── jinja2-3.1.6.dist-info
│   │       │   ├── licenses
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── markdown_it
│   │       │   ├── cli
│   │       │   ├── common
│   │       │   ├── helpers
│   │       │   ├── presets
│   │       │   ├── rules_block
│   │       │   ├── rules_core
│   │       │   ├── rules_inline
│   │       │   ├── __init__.py
│   │       │   ├── _compat.py
│   │       │   ├── _punycode.py
│   │       │   ├── main.py
│   │       │   ├── parser_block.py
│   │       │   ├── parser_core.py
│   │       │   ├── parser_inline.py
│   │       │   ├── port.yaml
│   │       │   ├── py.typed
│   │       │   ├── renderer.py
│   │       │   ├── ruler.py
│   │       │   ├── token.py
│   │       │   ├── tree.py
│   │       │   └── utils.py
│   │       ├── markdown_it_py-4.2.0.dist-info
│   │       │   ├── licenses
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── markupsafe
│   │       │   ├── __init__.py
│   │       │   ├── _native.py
│   │       │   ├── _speedups.c
│   │       │   ├── _speedups.pyi
│   │       │   └── py.typed
│   │       ├── markupsafe-3.0.3.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── top_level.txt
│   │       │   └── WHEEL
│   │       ├── mdurl
│   │       │   ├── __init__.py
│   │       │   ├── _decode.py
│   │       │   ├── _encode.py
│   │       │   ├── _format.py
│   │       │   ├── _parse.py
│   │       │   ├── _url.py
│   │       │   └── py.typed
│   │       ├── mdurl-0.1.2.dist-info
│   │       │   ├── INSTALLER
│   │       │   ├── LICENSE
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── packaging
│   │       │   ├── licenses
│   │       │   ├── __init__.py
│   │       │   ├── _elffile.py
│   │       │   ├── _manylinux.py
│   │       │   ├── _musllinux.py
│   │       │   ├── _parser.py
│   │       │   ├── _ranges.py
│   │       │   ├── _structures.py
│   │       │   ├── _tokenizer.py
│   │       │   ├── dependency_groups.py
│   │       │   ├── direct_url.py
│   │       │   ├── errors.py
│   │       │   ├── markers.py
│   │       │   ├── metadata.py
│   │       │   ├── py.typed
│   │       │   ├── pylock.py
│   │       │   ├── ranges.py
│   │       │   ├── requirements.py
│   │       │   ├── specifiers.py
│   │       │   ├── tags.py
│   │       │   ├── utils.py
│   │       │   └── version.py
│   │       ├── packaging-26.3.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── pip
│   │       │   ├── _internal
│   │       │   ├── _vendor
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── __pip-runner__.py
│   │       │   └── py.typed
│   │       ├── pip-25.2.dist-info
│   │       │   ├── licenses
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── REQUESTED
│   │       │   ├── top_level.txt
│   │       │   └── WHEEL
│   │       ├── pydantic
│   │       │   ├── _internal
│   │       │   ├── deprecated
│   │       │   ├── experimental
│   │       │   ├── plugin
│   │       │   ├── v1
│   │       │   ├── __init__.py
│   │       │   ├── _migration.py
│   │       │   ├── alias_generators.py
│   │       │   ├── aliases.py
│   │       │   ├── annotated_handlers.py
│   │       │   ├── class_validators.py
│   │       │   ├── color.py
│   │       │   ├── config.py
│   │       │   ├── dataclasses.py
│   │       │   ├── datetime_parse.py
│   │       │   ├── decorator.py
│   │       │   ├── env_settings.py
│   │       │   ├── error_wrappers.py
│   │       │   ├── errors.py
│   │       │   ├── fields.py
│   │       │   ├── functional_serializers.py
│   │       │   ├── functional_validators.py
│   │       │   ├── generics.py
│   │       │   ├── json.py
│   │       │   ├── json_schema.py
│   │       │   ├── main.py
│   │       │   ├── mypy.py
│   │       │   ├── networks.py
│   │       │   ├── parse.py
│   │       │   ├── py.typed
│   │       │   ├── root_model.py
│   │       │   ├── schema.py
│   │       │   ├── tools.py
│   │       │   ├── type_adapter.py
│   │       │   ├── types.py
│   │       │   ├── typing.py
│   │       │   ├── utils.py
│   │       │   ├── validate_call_decorator.py
│   │       │   ├── validators.py
│   │       │   ├── version.py
│   │       │   └── warnings.py
│   │       ├── pydantic-2.13.5.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── pydantic_core
│   │       │   ├── __init__.py
│   │       │   ├── _pydantic_core.pyi
│   │       │   ├── core_schema.py
│   │       │   └── py.typed
│   │       ├── pydantic_core-2.46.5.dist-info
│   │       │   ├── licenses
│   │       │   ├── sboms
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── pyfiglet
│   │       │   ├── fonts
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── py.typed
│   │       │   ├── test.py
│   │       │   └── version.py
│   │       ├── pyfiglet-1.0.4.dist-info
│   │       │   ├── licenses
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── top_level.txt
│   │       │   └── WHEEL
│   │       ├── pygments
│   │       │   ├── filters
│   │       │   ├── formatters
│   │       │   ├── lexers
│   │       │   ├── styles
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── cmdline.py
│   │       │   ├── console.py
│   │       │   ├── filter.py
│   │       │   ├── formatter.py
│   │       │   ├── lexer.py
│   │       │   ├── modeline.py
│   │       │   ├── plugin.py
│   │       │   ├── regexopt.py
│   │       │   ├── scanner.py
│   │       │   ├── sphinxext.py
│   │       │   ├── style.py
│   │       │   ├── token.py
│   │       │   ├── unistring.py
│   │       │   └── util.py
│   │       ├── pygments-2.21.0.dist-info
│   │       │   ├── licenses
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── rich
│   │       │   ├── _unicode_data
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── _emoji_codes.py
│   │       │   ├── _emoji_replace.py
│   │       │   ├── _export_format.py
│   │       │   ├── _extension.py
│   │       │   ├── _fileno.py
│   │       │   ├── _inspect.py
│   │       │   ├── _log_render.py
│   │       │   ├── _loop.py
│   │       │   ├── _null_file.py
│   │       │   ├── _palettes.py
│   │       │   ├── _pick.py
│   │       │   ├── _ratio.py
│   │       │   ├── _spinners.py
│   │       │   ├── _stack.py
│   │       │   ├── _timer.py
│   │       │   ├── _win32_console.py
│   │       │   ├── _windows.py
│   │       │   ├── _windows_renderer.py
│   │       │   ├── _wrap.py
│   │       │   ├── abc.py
│   │       │   ├── align.py
│   │       │   ├── ansi.py
│   │       │   ├── bar.py
│   │       │   ├── box.py
│   │       │   ├── cells.py
│   │       │   ├── color.py
│   │       │   ├── color_triplet.py
│   │       │   ├── columns.py
│   │       │   ├── console.py
│   │       │   ├── constrain.py
│   │       │   ├── containers.py
│   │       │   ├── control.py
│   │       │   ├── default_styles.py
│   │       │   ├── diagnose.py
│   │       │   ├── emoji.py
│   │       │   ├── errors.py
│   │       │   ├── file_proxy.py
│   │       │   ├── filesize.py
│   │       │   ├── highlighter.py
│   │       │   ├── json.py
│   │       │   ├── jupyter.py
│   │       │   ├── layout.py
│   │       │   ├── live.py
│   │       │   ├── live_render.py
│   │       │   ├── logging.py
│   │       │   ├── markdown.py
│   │       │   ├── markup.py
│   │       │   ├── measure.py
│   │       │   ├── padding.py
│   │       │   ├── pager.py
│   │       │   ├── palette.py
│   │       │   ├── panel.py
│   │       │   ├── pretty.py
│   │       │   ├── progress.py
│   │       │   ├── progress_bar.py
│   │       │   ├── prompt.py
│   │       │   ├── protocol.py
│   │       │   ├── py.typed
│   │       │   ├── region.py
│   │       │   ├── repr.py
│   │       │   ├── rule.py
│   │       │   ├── scope.py
│   │       │   ├── screen.py
│   │       │   ├── segment.py
│   │       │   ├── spinner.py
│   │       │   ├── status.py
│   │       │   ├── style.py
│   │       │   ├── styled.py
│   │       │   ├── syntax.py
│   │       │   ├── table.py
│   │       │   ├── terminal_theme.py
│   │       │   ├── text.py
│   │       │   ├── theme.py
│   │       │   ├── themes.py
│   │       │   ├── traceback.py
│   │       │   └── tree.py
│   │       ├── rich-15.0.0.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── shellingham
│   │       │   ├── posix
│   │       │   ├── __init__.py
│   │       │   ├── _core.py
│   │       │   └── nt.py
│   │       ├── shellingham-1.5.4.dist-info
│   │       │   ├── INSTALLER
│   │       │   ├── LICENSE
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── top_level.txt
│   │       │   ├── WHEEL
│   │       │   └── zip-safe
│   │       ├── termcolor
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── py.typed
│   │       │   └── termcolor.py
│   │       ├── termcolor-3.3.0.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── toml
│   │       │   ├── __init__.py
│   │       │   ├── decoder.py
│   │       │   ├── encoder.py
│   │       │   ├── ordered.py
│   │       │   └── tz.py
│   │       ├── toml-0.10.2.dist-info
│   │       │   ├── INSTALLER
│   │       │   ├── LICENSE
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   ├── top_level.txt
│   │       │   └── WHEEL
│   │       ├── tomlkit
│   │       │   ├── __init__.py
│   │       │   ├── _compat.py
│   │       │   ├── _types.py
│   │       │   ├── _utils.py
│   │       │   ├── api.py
│   │       │   ├── container.py
│   │       │   ├── exceptions.py
│   │       │   ├── items.py
│   │       │   ├── parser.py
│   │       │   ├── py.typed
│   │       │   ├── source.py
│   │       │   ├── toml_document.py
│   │       │   └── toml_file.py
│   │       ├── tomlkit-0.15.1.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── typer
│   │       │   ├── .agents
│   │       │   ├── _click
│   │       │   ├── __init__.py
│   │       │   ├── __main__.py
│   │       │   ├── _completion_classes.py
│   │       │   ├── _completion_shared.py
│   │       │   ├── _types.py
│   │       │   ├── _typing.py
│   │       │   ├── cli.py
│   │       │   ├── colors.py
│   │       │   ├── completion.py
│   │       │   ├── core.py
│   │       │   ├── exceptions.py
│   │       │   ├── main.py
│   │       │   ├── models.py
│   │       │   ├── params.py
│   │       │   ├── py.typed
│   │       │   ├── rich_utils.py
│   │       │   ├── testing.py
│   │       │   └── utils.py
│   │       ├── typer-0.27.2.dist-info
│   │       │   ├── licenses
│   │       │   ├── entry_points.txt
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── typing_extensions-4.16.0.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       ├── typing_inspection
│   │       │   ├── __init__.py
│   │       │   ├── introspection.py
│   │       │   ├── py.typed
│   │       │   ├── typing_objects.py
│   │       │   └── typing_objects.pyi
│   │       ├── typing_inspection-0.4.4.dist-info
│   │       │   ├── licenses
│   │       │   ├── INSTALLER
│   │       │   ├── METADATA
│   │       │   ├── RECORD
│   │       │   └── WHEEL
│   │       └── typing_extensions.py
│   ├── Scripts
│   │   ├── activate
│   │   ├── activate.bat
│   │   ├── activate.fish
│   │   ├── Activate.ps1
│   │   ├── custy.exe
│   │   ├── deactivate.bat
│   │   ├── git-credential-custy.exe
│   │   ├── markdown-it.exe
│   │   ├── pip.exe
│   │   ├── pip3.14.exe
│   │   ├── pip3.exe
│   │   ├── pyfiglet.exe
│   │   ├── pygmentize.exe
│   │   ├── python.exe
│   │   ├── pythonw.exe
│   │   └── typer.exe
│   ├── .gitignore
│   └── pyvenv.cfg
├── scripts
│   ├── ci
│   │   ├── __init__.py
│   │   └── package_version.py
│   ├── docker
│   │   ├── docker-remove-images.ps1
│   │   └── docker-remove-images.sh
│   ├── docs
│   │   ├── docs
│   │   │   └── render_mermaid_examples.md
│   │   ├── venv/ ... (collapsed)
│   │   ├── check_docs_links.py
│   │   └── render_mermaid.py
│   ├── repository
│   │   └── src
│   │       └── sync_metadata.py
│   └── __init__.py
├── site/ ... (collapsed)
├── tests
│   ├── cli
│   │   ├── test_init_command.py
│   │   ├── test_main.py
│   │   └── test_versions.py
│   ├── config
│   │   └── test_config_loader.py
│   ├── core
│   │   ├── build/ ... (collapsed)
│   │   ├── initialize
│   │   │   ├── test_init_builder.py
│   │   │   └── test_init_main.py
│   │   └── scan
│   │       ├── test_processor.py
│   │       ├── test_scanner.py
│   │       └── test_updater.py
│   ├── integration
│   │   └── test_full_scan.py
│   ├── languages
│   │   ├── test_html_strategy.py
│   │   ├── test_javascript_strategy.py
│   │   ├── test_php_strategy.py
│   │   ├── test_python_strategy.py
│   │   └── test_shell_strategy.py
│   ├── services
│   │   └── test_banner_service.py
│   ├── theme
│   │   └── test_theme.py
│   ├── unit
│   │   └── config
│   │       ├── test_precommit_config.py
│   │       └── test_pyproject_toml.py
│   ├── utils
│   │   ├── test_logging.py
│   │   ├── test_parsing.py
│   │   ├── test_paths.py
│   │   └── test_resolver.py
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_developer_workflows.py
│   └── test_dry_run.py
├── venv/ ... (collapsed)
├── .coverage
├── .dockerignore
├── .gitignore
├── .gitlab-ci.yml
├── .pre-commit-config.yaml
├── .prettierignore
├── .prettierrc.json
├── AGENTS.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── docker-compose.yml
├── Dockerfile
├── ENGINEERING_EXECUTION_POLICY.md
├── LICENSE
├── Makefile
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── requirements.txt
├── SECURITY.md
└── TODO.md
```

---

## Root Files

| File | Description |
|------|-------------|
| `README.md` | Project overview and introduction. |
| `CHANGELOG.md` | History of notable changes between releases. |
| `LICENSE` | Project license information. |
| `CONTRIBUTING.md` | Guidelines for contributing to the project. |
| `SECURITY.md` | Security policy and vulnerability reporting instructions. |
| `TODO.md` | Pending tasks and future improvements. |
| `AGENTS.md` | Instructions and guidance for AI agents and automation tools. |
| `ENGINEERING_EXECUTION_POLICY.md` | Engineering execution standards and policies. |
| `pyproject.toml` | Main Python project configuration file. |
| `requirements.txt` | Python package dependencies. |
| `mkdocs.yml` | MkDocs documentation site configuration. |
| `Makefile` | Defines common development, testing, and build commands. |
| `Dockerfile` | Container image build instructions. |
| `docker-compose.yml` | Default multi-container Docker configuration. |
| `docker-compose.dev.yml` | Development Docker Compose configuration. |
| `docker-compose.prod.yml` | Production Docker Compose configuration. |
| `.gitignore` | Specifies files and directories ignored by Git. |
| `.dockerignore` | Specifies files excluded from Docker build context. |
| `.prettierrc.json` | Prettier code formatting configuration. |
| `.prettierignore` | Files ignored by Prettier. |
| `.pre-commit-config.yaml` | Pre-commit hooks configuration. |
| `.gitlab-ci.yml` | GitLab CI/CD pipeline configuration. |

---

## Directory Details

### `.config/`
Project configuration files.

Stores reusable configuration files used by the project.
Helps keep the repository root clean and organized.

Common examples:
- .config/tool-config/
- .config/templates/
- .config/settings/

### `app/`
Main application source code.

Contains the core implementation of the project.
May include business logic, services, modules, and utilities.

### `docs/`
Project documentation and technical references.

The documentation folder usually contains structured knowledge about the project.

Common documentation sections:
- docs/architecture        → system design and architecture diagrams
- docs/development         → development guides and workflows
- docs/system              → detailed technical documentation
- docs/reference           → command references and APIs
- docs/user-guide          → instructions for end users
- docs/diagrams            → visual architecture diagrams
- docs/phases              → project phases and planning
- docs/Q&A                 → common questions and explanations

Common files:
- PROJECT_STRUCTURE.md
- DEVELOPMENT_GUIDE.md
- HOW_TO_USE.md
- TODO.md
- CLI_COMMAND.md
- references.md
- badges.md

### `scripts/`
Utility scripts for development or automation.

May include deployment scripts, maintenance tools, or helpers.

### `tests/`
Automated tests.

Contains unit tests and integration tests.
Ensures code reliability and correctness.


---

## Notes

- Temporary files, caches, and environment directories are excluded.
- Structure is generated automatically using DocGen.
