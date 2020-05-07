# New Tooling

## Dependency Management via `pip-tools`

Dependencies should be specified within the `setup.py` file.

The `INSTALL_REQUIRES` list contains the dependencies required to run the project's code.

The `TESTS_REQUIRES` list contains the dependencies required to run the project's test suite.

The `DEV_REQUIRES` list contains the dependencies required for project development, and is the combination of the `INSTALL_REQUIRES` and `TESTS_REQUIRES` lists.

These packages can be specified by name alone, or by name and version.

```python
INSTALL_REQUIRES = [
    'foo',
    'bar>3.0',
    'baz==4.0',
]
```

These dependencies are written to a `requirements.in` file, which is used by `pip-compile` to automatically create the `requirements.txt` file.

## Code checking with Pre-Commit Hooks

Pre-commit hooks offer an automated way to identify code issues prior to commit and push.

On commit, these hooks run only on the staged files.

_The developer must recommit any files fixed by a pre-commit hook_.

### isort and seed-isort-config

The isort config file is automatically updated with first and third party packages via the `seed-isort-config` hook.

Python imports are automatically sorted via the `isort` hook.

### Black

Python autoformatting is performed with `black`.

