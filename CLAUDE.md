# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Project overview

`highspot` is an unofficial Python SDK for the Highspot API (published on PyPI). The primary entry point is the
`Highspot` class in `src/highspot/core.py`, which is re-exported from `highspot/__init__.py`.

Layout (`src/highspot/`):
- `core.py` - the `Highspot` object (authentication and the public methods)
- `api.py`, `request.py` - API request/response handling built on `requests`
- `users.py`, `groups.py`, `items.py`, `spots.py`, `pitches.py` - resource-specific helpers
- `domain.py` - Highspot domain/URL helpers
- `errors/` - custom exceptions and handlers
- `utils/` - logging (`log_utils.py`) and the package version (`version.py`)

Docs are Sphinx (`docs/`, hosted on Read the Docs); the change log is `docs/changelog.rst`.

## Environment and commands

- Packaging and dependencies use **Poetry** (`pyproject.toml`, `poetry.lock`); `setup.py`/`setuptools` are gone.
- Supported Python is `>=3.10,<3.14.0`. Use a supported interpreter (e.g. `poetry env use python3.13`).
- Install: `poetry install --with dev`
- Build: `poetry build` then `twine check dist/*`
- Docs: `poetry run sphinx-build -b html docs docs/_build`
- Add dependencies with `poetry add ...` / `poetry add --group dev ...`, not by hand-editing `poetry.lock`.
- There are currently **no tests, linter config or CI**. Verify changes with an import/smoke test and the docs build.

## Versioning

- The version is defined in two places that must be kept in sync: `pyproject.toml` and
  `src/highspot/utils/version.py` (`__version__`, read by `docs/conf.py`).
- Git tags use the bare version with no prefix (e.g. `2.0.0`), matching the author's other projects.
- Releases are uploaded to PyPI by the maintainer. Do not publish to PyPI.

## Dependencies and security

- Runtime dependencies are minimum-floor pins in `pyproject.toml`, mirrored in `requirements.txt`; the floors
  exist to address Dependabot advisories, so do not lower them. Do not add `setuptools` as a runtime dependency.
- Keep `requirements.txt` and `docs/requirements.txt` (used by Read the Docs) consistent with `pyproject.toml`.

## Code and docs conventions

- Follow the existing style: module header blocks (`:Module:`, `:Synopsis:`, `:Last Modified:`, `:Modified Date:`;
  update the modifier/date on files you change), Sphinx/reST docstrings, and existing naming.
- Record user-visible changes in `docs/changelog.rst`.
- Keep changes small and localized; don't refactor unrelated code.

## Git

- Work on a branch, not directly on `master`. Do not commit or push unless asked.
- Commit messages use past tense ("Added ...", "Fixed ..."), are focused, and mention the file name where natural.
