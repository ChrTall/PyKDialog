# PyKDialog

This project is WIP and currently in alpha state. (not complete)

Fluent Python API to create KDialog commands

## Developer setup:

### Installing dependencies

The development dependencies are listed in 
`pyproject.toml` [project.optional-dependencies] dev

To install those dependencies execute:

```bash
pip3 install --require-virtualenv --editable .[dev]
```

### Running tests:

To run, all Unit-Tests execute:
```bash
pytest tests/
```

To run all Unit Tests with a coverage, execute:

```bash
pytest --cov=PyKDialog tests/
```

To run all Unit Tests and create a JSON coverage report, execute:

```bash
pytest  --cov-report json:cov.json \
        --cov=PyKDialog tests/
```

To run all Unit Tests and create an Html coverage report, execute:

```bash
pytest --cov-report html:cov_html \
        --cov=PyKDialog tests/
```

### Running integration-tests:

Integration Tests require an OS with KDialog installed and require manual user-input.

```bash
pytest integration_tests/
```
