# Repo or Project name

[![PM CI workflow](https://github.com/predictionmachine/pm-coding-template/actions/workflows/pm-gh-actions.yml/badge.svg)](https://github.com/predictionmachine/pm-coding-template/actions/workflows/pm-gh-actions.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e4cab5c6472ba0512bd0/maintainability)](https://codeclimate.com/repos/602750680b442f4c8d007eb0/maintainability)
<!-- see https://app.codecov.io/gh/predictionmachine/pm-coding-template/settings/badge -->
[![codecov](https://codecov.io/gh/predictionmachine/pm-coding-template/branch/main/graph/badge.svg?token=W1bAJ3l546)](https://codecov.io/gh/predictionmachine/pm-coding-template)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

(If forking this template repo, please update this readme accordingly)

* Update the status badges: (once updated, remove this section)
  <!-- see https://github.com/psf/black#show-your-style -->
  * [code style - black](https://github.com/psf/black)
  <!-- see https://app.codecov.io/gh/predictionmachine/event-tools/settings/badge -->
  * [codecov](https://about.codecov.io/product/feature/badges/)
  <!-- see https://codeclimate.com/repos/602750680b442f4c8d007eb0/badges-->
  * [maintainability - codeclimate](https://codeclimate.com/github/codeclimate/codeclimate/badges)
  <!-- see https://docs.github.com/en/actions/managing-workflow-runs/adding-a-workflow-status-badge -->
  * [PM CI Workflow](https://github.com/predictionmachine/pm-coding-template/actions/workflows/pm-gh-actions.yml)

[ Write about this repository/project here.]

## Pre-Commit

You can run pre-commit explicitly, which can be useful if you want
to examine its changes:

```shell
pre-commit run --all-files
```

**Updating pre-commit hooks automatically**

You can update your hooks to the latest version automatically by running `pre-commit autoupdate`. By default, this will bring the hooks to the latest tag on the default branch.

***Note:*** After updating hooks, make sure to commit the changes.

**Skipping pre-commit hooks**

You can run `git commit --no-verify` to bypass the pre-commit hooks.

***Follow the coding standards as per the [docs](docs/coding-standard.md).***
