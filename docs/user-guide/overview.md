<!-- docs/user-guide/overview.md -->

# User Guide Overview

This section explains Path Header Scanner from an end-user perspective.

## What the tool does

Path Header Scanner helps developers/devops/programmers keep file path headers consistent in source files.

It can:

- scan supported files
- detect whether file path headers are valid
- insert missing path headers
- update invalid headers

## Typical usage model

You usually run the tool inside **your own project** directory.

Example user scenario:

- user has `projectA`
- user installs Path Header Scanner
- user runs initialization (`init`)
- user scans project files (`scan`)
- user applies changes if output is correct (`--apply`)

## Core command groups

- `init`: initialize local configuration/template assets for the tool
- `scan`: scan target directories and optionally write changes

## Important behavior

- without `--apply`, scan runs in non-mutating preview mode
- with `--apply`, changes are written to files
- headers can include or exclude the scan target directory
- special lines are preserved for supported languages (e.g., shebang, `<?php`)

## Where to continue

- Start quickly: `docs/user-guide/quickstart.md`
- Full command details: `docs/user-guide/commands.md`
- Install options (pip, docker, artifacts): `docs/user-guide/installation-methods.md`
- Start/stop/cleanup lifecycle: `docs/user-guide/lifecycle.md`
