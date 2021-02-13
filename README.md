# pm-coding-template
Documents and Illustrates Coding Standards used at Prediction Machine

As you ramp up on contributing code to Prediction Machine, 
please review the basics:

## Dev Environment
* Mac/Linux preferred. For Windows, use [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* use `python3.8` for compatibility, eg if we deploy your code as AWS Lambda
* If you are a long term contributor we prefer that you use the
  [PyCharm](https://www.jetbrains.com/pycharm/) IDE (if you are already
  using IntelliJ, IntelliJ with Python plugin may work)
* (beta) We are evaluating [Code With Me](https://plugins.jetbrains.com/plugin/14896-code-with-me)
as a way to pair on code, a surprisingly fruitful technique
* do use separate [virtual env](https://docs.python.org/3/library/venv.html) for each repo
* do pin dependency versions in requirements.txt with ~= [TODO: need a example]
* when file names must have multiple words, use _ not -

## Code Contents
* 🛑 Do not put passwords, API keys or other credentials, in source files or
  jupyter notebooks. Load them from environment variables. This makes your code
  less brittle and keeps the credentials secure. Winning! 🙌
* 🛑 Do not hardcode your local paths to data files etc. Again, env variables
  are your friend
* Do put a disclaimer at the top of each file
  * See [projectname/example.py](projectname/example.py) for an example
* Organize code in namespace and files. `tests` dir inside the namespace
* Use `pytest` as the default testing library (and more if you need)
* Use type hints and [mypy](https://mypy.readthedocs.io/en/stable/).
   * See [projectname/example.py](projectname/example.py) for an example
   * We recommend [mypy plugin](https://plugins.jetbrains.com/plugin/11086-mypy)
     for the IDE

## Github commits
* Create a branch with a descriptive name, eg `tchklovski/document-practices`
  Or even `tchklovski/docs/document-practices`. The IDE uses `/` in branch
  name to group changes, which can be helpful
  Push your changes to the branch and then submit a pull request to merge to
  master. Assign the pull request reviewing duties to the person you are
  reporting to. You can do this in the IDE or on github.
* Write a descriptive message summarizing your commit, and even state what
  you are trying to accomplish/larger task you are working on
* Use [GitHub Actions](https://docs.github.com/en/actions) to catch problems for
  you. Actions should run the test suite, black formatting check, mypy type
  checking, notebook cleaning check, and fail if any of these fail (so that you
  can fix the pull request rather than break master)
  
  Over time feel free to propose enhancements to actions, eg adding files ending
  in `.zip` or `.parquet` should cause a pull request to fail. The best
  proposal is one you are ready to implement yourself.
