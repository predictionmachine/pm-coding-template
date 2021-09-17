# Coding Standard

Documents and Illustrates Coding Standards used at [Prediction Machine](https://predmachine.com).

As you ramp up on contributing code to Prediction Machine,
please review the basics:

## Dev Environment

* Mac/Linux preferred. For Windows, use [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* Do use separate [virtual env](https://docs.python.org/3/library/venv.html) for each repo.
* IDE:
  * For long-term contributors we prefer that you use the
  [PyCharm](https://www.jetbrains.com/pycharm/) IDE (if you are already
  using IntelliJ, IntelliJ with Python plugin may work)
  * [VSCode](https://code.visualstudio.com/) may also be viable if that's your strong preference
* Pair Programming:
  * We use [Duckly](https://duckly.com/tools/pycharm) as a way to pair on code,
    a surprisingly fruitful technique
* Dependencies:
  * Target `python3.8` for compatibility (e.g. with AWS Lambda)
  * Pin dependency versions in requirements.txt with `~=`, e.g. `flake8~=3.8.4`
* file names are normally all lowercase
* when file names must have multiple words, use "_", not "-"
* Organize code in namespace and files. `tests` dir at the top level
* Configure and use [pre-commit hooks](https://pre-commit.com/#plugins). Copy [.pre-commit-config.yaml](https://github.com/predictionmachine/pm-coding-template/blob/main/.pre-commit-config.yaml) to the root directory of your repo and follow the [installation](https://pre-commit.com/#installation) instructions to run it.

## Code Contents

* 🛑 No hardcoded credentials:
  * Do not put passwords, API keys or other credentials in source files or
  jupyter notebooks. Load them from environment variables. This makes your code
  less brittle and keeps the credentials secure. Winning! 🙌
* 🛑 No hardcoded paths:
  * Do not hardcode your local paths to data files etc. Again, env variables
  are your friend
* License:
  * Do put a disclaimer at the top of each file
  * See [projectname/example.py](https://github.com/predictionmachine/pm-coding-template/blob/main/projectname/example.py) for an example
  * You can enter it [in PyCharm](http://prntscr.com/1011gyr) and then [pick it](http://prntscr.com/1011fz5)

* Documentation:
  * We expect all code to have [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google)
  * We use [interrogate](https://interrogate.readthedocs.io/en/latest/) to check missing docstrings in code base.
* Testing:
  * We expect shipped code to have close to 100% test coverage
  * Use [pytest](https://docs.pytest.org/en/stable/) as the default testing library
* Type hints:
  * Use type hints and [mypy](https://mypy.readthedocs.io/en/stable/).
  * See [projectname/example.py](https://github.com/predictionmachine/pm-coding-template/blob/main/projectname/example.py) for an example
  * We recommend the [mypy plugin](https://plugins.jetbrains.com/plugin/11086-mypy) for the IDE

## Github: branches, pull requests

* 🛑 No new repos: do not create a new repository on your own -- Create a task on [ClickUp](https://app.clickup.com/login), assign to @manasRK to request one.
  This keeps us more organized and naming consistent. In your ClickUp task, specify what the code
  in this repository will be responsible for doing. Consider what should be a shared repo.
* Code is considered "shipped" (🎉) when it is accepted as a pull request and merged in `main`.
* To be mergeable, red (failed) checks need to be addressed
* Create a branch with a descriptive name, eg `tchklovski/01-document-practices`
  Or even `tchklovski/docs/01-document-practices`. The IDE uses `/` in branch
  name to group changes, which can be helpful
* Push your changes to the branch and then submit a pull request to merge to
  master. Assign the pull request reviewing duties to the person you are
  reporting to. You can do this in the IDE or on GitHub.
* Write a descriptive message summarizing your commit, and even state what
  you are trying to accomplish/larger task you are working on.
* Use [GitHub Actions](https://docs.github.com/en/actions) to catch problems for
  you. Actions should run the test suite, black formatting check, mypy type
  checking, notebook cleaning check, and fail if any of these fail (so that you
  can fix the pull request rather than break master).

  Feel free to propose enhancements to GitHub actions, e.g. adding files ending
  in `.zip` or `.parquet` should cause a pull request to fail. The best
  proposal is one you are ready to implement yourself.
* Update the status badges:
  <!-- see https://github.com/psf/black#show-your-style -->
  * [code style - black](https://github.com/psf/black)
  <!-- see https://app.codecov.io/gh/predictionmachine/event-tools/settings/badge -->
  * [codecov](https://about.codecov.io/product/feature/badges/)
  <!-- see https://codeclimate.com/repos/602750680b442f4c8d007eb0/badges-->
  * [maintainability - codeclimate](https://codeclimate.com/github/codeclimate/codeclimate/badges)
  <!-- see https://docs.github.com/en/actions/managing-workflow-runs/adding-a-workflow-status-badge -->
  * [PM CI Workflow](https://github.com/predictionmachine/pm-coding-template/actions/workflows/pm-gh-actions.yml)
