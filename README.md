# CI/CD Development for projects #
This repository is used to test changes to the automation used in our standard
python assignments. The example application is a small assignment on functions.

## What is in this repo, anyway? ##
There are lots of files and directories in this repository, what are they all for?

### .github/workflows/standard_python_pbl.yml ###
This yaml file defines the ci/cd pipeline for the repository. Any yaml file in this
directory can define an additional workflow.

### .vscode/settings.json ###
This json file configures the workspace settings for VSCode.

### docs ###
This directory is used for configuration and templates for Sphinx, the tool we use to
generate the html documentation pages.

### tests ###
This directory is used by pytest. The names of files, functions, classes, and methods
dictate what is a test for pytest.

### .coveragerc ###
This configuration file is for coverage.py

### .gitignore ###
This file is a list of patterns that exclude files from git. Temporary files and some
configuration files should be left out of version control.

### .pre-commit-config.yaml ###
This yaml file defines the pre-commit hooks we will install with pre-commit (the Python tool)

### conftest.py ###
This file lets pytest know the root directory of the code. It can have some pytest
configuration, but this one does not.

### README.md ###
This markdown file.

### requirements.txt ###
A list of dependancies for the program. Packages that need to be installed with pip to
import them in the program should all be in this file. 
