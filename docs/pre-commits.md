# About `pre-commit`

[pre-commit hooks](https://pre-commit.com/) are a subset of git hooks. git hooks are scripts that run automatically every time a particular event occurs in a git repository. A “pre-commit hook” runs before a commit takes place.

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
    - [flake8-copyright](https://github.com/savoirfairelinux/flake8-copyright): Additional dependency for flake8 that checks for copyright notices in all python files.

  - [Interrogate](https://github.com/econchick/interrogate): Checks code base for missing docstrings.

  - [isort](https://github.com/pre-commit/mirrors-isort): Sort Python imports.

  - [Mypy](https://github.com/pre-commit/mirrors-mypy): [mypy](https://github.com/python/mypy) type checks for Python with additional dependencies.

  - [pytest-check](https://github.com/predictionmachine/pm-coding-template/blob/8a538d6dc35a0559bdf92fda02d118e1608a7d93/.pre-commit-config.yaml#L113): Running pytest locally.

---

## Installation & usage

### 1. Install `pre-commit`:

- Using [`pip`](https://pip.pypa.io/en/stable/) :

  ```shell
  $ pip install pre-commit
  ```

- Using [homebrew](https://brew.sh/)

  ```shell
  $ brew install pre-commit
  ```

- Using [conda](https://conda.io/) (via [conda-forge](https://conda-forge.org/)):

### 2. Install `pre-commit` hooks:

- The pre-commit hook configurations are defined in [`.pre-commit-config.yaml`](https://github.com/predictionmachine/pm-coding-template/blob/main/.pre-commit-config.yaml) file.
- To install the hooks, run:

  ```shell
  $ pre-commit install
  ```

### 3. Update hook version:

- To update hook version, periodically run:

  ```shell
  $ pre-commit autoupdate
  ```

### 4. Running `pre-commit` hooks on files:

- To run hooks on all the files, run:

  ```shell
  $ pre-commit run --all-files
  ```

- To run hooks on specifc file (single file), run:

  ```shell
  $ pre-commit run --files /path_of_the_file
  ```

- To skip `pre-commit` hook on commit, run:

  ```shell
  $ git commit -m "change_type: your message" --no-verify
  ```

- Skipping a hook:

  - To skip a specific hook (or set of hook) temporarily, use `SKIP` environment variable with hook id when doing a commit.
  - The `SKIP` environment variable is a comma separated list of hook ids. This allows you to skip a single hook instead of `--no-verify` ing the entire commit.
  - Syntax:

    ```shell
    $ SKIP=hook_id,hook_id_2 git commit -m "commit message"
    ```

  - Example:

    ```shell
    $ SKIP=flake8 git commit -m "doc: update readme"
    ```

- `mypy` hook needs the typing dependencies installed, which mirrors `requirement-dev.txt`, for example:

  ```shell
  - repo: https://github.com/pre-commit/mirrors-mypy
      rev: 'v0.910'
      hooks:
        - id: mypy
          # verbose: true
          # args: [--ignore-missing-imports]
          additional_dependencies:
            # - boto3-stubs[s3]>=1.18
            # - mypy-boto3-s3>=1.18
            # - types-orjson>=0.1.1
            - types-pytz>=2021.1.0
            # - types-requests>=2.25.0
  ```

- `flake8` hook needs an additional dependency ([flake8-copyright](https://github.com/savoirfairelinux/flake8-copyright)) that checks for copyright notices in all python files.
- Other hooks that need the dependencies should be configured in `.pre-commit-config.yaml` config file.
