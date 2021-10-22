# About `pre-commit`

[pre-commit hooks](https://pre-commit.com/) are a subset of Git hooks. Git-hooks are scripts that run automatically every time a particular event occurs in a Git repository. A “pre-commit hook” runs before a commit takes place.

---

## What problems `pre-commit` solve?

pre-commit hooks are very useful in identifying simple issues before submission to code review - mostly at the time of commit.
These hooks are run on every commit to automatically point out issues in the code, such as code linting, trailing whitespace in the file, running test cases and type checking, etc
Pointing out these issues before code review allows a code reviewer to focus more on the application logic & architecture rather than petty issues.

So you can fix these issues before committing the changes and sending them for code review.

---

## `pre-commit` hooks used at PM

- Following are the pre-commit hooks used in PM, and a few projects may have additional hooks.
  - [Basic pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks): Some out-of-the-box hooks for pre-commit.
    - [trailing-whitespace](https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace)
    - [end-of-file-fixer](https://github.com/pre-commit/pre-commit-hooks#end-of-file-fixer)
    - [requirements-txt-fixer](https://github.com/pre-commit/pre-commit-hooks#requirements-txt-fixer)
    - [detect-private-key](https://github.com/pre-commit/pre-commit-hooks#detect-private-key)
    - [detect-aws-credentials](https://github.com/pre-commit/pre-commit-hooks#detect-aws-credentials)
    - [check-ast](https://github.com/pre-commit/pre-commit-hooks#check-ast)
    - [check-merge-conflict](https://github.com/pre-commit/pre-commit-hooks#check-toml)
    - [check-toml](https://github.com/pre-commit/pre-commit-hooks#check-toml)
    - [check-yaml](https://github.com/pre-commit/pre-commit-hooks#check-yaml)
    - [check-added-large-files](https://github.com/pre-commit/pre-commit-hooks#check-added-large-files)
    - [no-commit-to-branch](https://github.com/pre-commit/pre-commit-hooks#no-commit-to-branch)

  - [autoflake](https://github.com/myint/autoflake): Removes unused imports and unused variables.

  - [Black](https://github.com/psf/black): PEP 8 compliant opinionated Python code formatter. It reformats entire files in place.

  - [black_nbconvert](https://github.com/dfm/black_nbconvert): Black formatter for `ipynb` files or [Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/stable/).

  - [docker-compose-check](https://github.com/IamTheFij/docker-pre-commit#docker-compose-check): Verifies that docker-compose files are valid.

  - [flake8](https://github.com/pycqa/flake8): Python code linter that wraps [PyFlakes](https://github.com/PyCQA/pyflakes), [pycodestyle](https://github.com/PyCQA/pycodestyle) and Ned Batchelder's [McCabe](https://github.com/PyCQA/mccabe) script.
    - [flake8-copyright](https://github.com/savoirfairelinux/flake8-copyright): Checks for copyright notices in all python files

  - [Interrogate](https://github.com/econchick/interrogate): Checks code base for missing docstrings.

  - [isort](https://github.com/pre-commit/mirrors-isort): Sort Python imports.

  - [Mypy](https://github.com/pre-commit/mirrors-mypy): [mypy](https://github.com/python/mypy) type checks for Python.

  - [pytest-check](https://github.com/predictionmachine/pm-coding-template/blob/8a538d6dc35a0559bdf92fda02d118e1608a7d93/.pre-commit-config.yaml#L113): Running pytest locally.

---

## installation & usage

- Using [`pip`](https://pip.pypa.io/en/stable/) :

```shell
pip install pre-commit
```

- Using [homebrew](https://brew.sh/)

```shell
brew install pre-commit
```

- Using conda (via conda-forge):
