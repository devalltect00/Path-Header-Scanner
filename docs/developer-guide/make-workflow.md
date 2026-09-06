# Make workflow

Path Header Scanner uses a modular Make system. The root `Makefile` only defines
module loading order; command implementations and help fragments live under
`make/core/`.

## Help groups

```bash
make help
make help-local
make help-docker
make help-compose
make help-remote
```

The grouped help output reports command counts from the same registration data
used by the command modules.

## Local scanner workflow

```bash
make setup
make l-scan TARGET=app
make l-scan-debug TARGET=app
make l-scan-apply TARGET=app
```

`l-scan` is preview-only. The `l-scan-apply*` targets explicitly pass `--apply`
and may update files in the selected target.

Explicit dry-run can be passed to any workflow through command arguments:

```bash
make l-init PHS_INIT_ARGS="--dry-run"
make l-scan-apply TARGET=app PHS_SCAN_ARGS="--dry-run"
```

The second command does not write because dry-run overrides `--apply`.

## Docker and Compose

```bash
make d-build-all
make d-scan TARGET=app
make c-build-all
make c-scan TARGET=app
make c-check
```

Direct Docker targets use the locally built images. Compose helper services reuse
the development image built by the `app` service.

## Published utility images

Remote targets cover all Devalltect utility images:

```bash
make r-phs-pull
make r-doc-gen-pull
make r-custy-pull
make r-reflow-pull
```

Use `REMOTE_TAG`, `REMOTE_WORKSPACE`, `GHCR_OWNER`, and the corresponding
`REMOTE_*_ARGS` variables to select versions, workspaces, and command options.
Registry push targets are externally visible operations and require explicit
review and authorization.

### Custy credential helpers

The published Custy image supports dedicated GitHub and GitLab credential
helpers:

```bash
make r-custy-credentials-set-github
make r-custy-credentials-set-gitlab
make r-custy-credentials-status
make r-custy-credentials-test CUSTY_CREDENTIALS_REMOTE=origin
```

Provider setup uses a read-write credential mount. Status and remote testing
use a read-only mount, and the test performs only a read-only access check.
`CUSTY_CREDENTIALS_HOST_DIR` selects the external host directory, while
`CUSTY_CREDENTIALS_CONTAINER_DIR` defaults to `/run/secrets/custy`.

Ordinary `r-custy-run*` and `r-custy-workflow` targets preserve their previous
behavior by leaving the directory unmounted. Opt in when a workflow needs the
configured fallback:

```bash
make r-custy-run-push CUSTY_CREDENTIALS_MOUNT=true
```

## Safety

Start with preview commands. Do not run apply, cleanup, registry push, package
publish, or release-related targets without checking their resolved target and
effects.
