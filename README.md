# playwright-python-setup
Playwright POC using python and pytest

The tests are set to run in parallel.

## Instructions

* Install dependencies: `pipenv install`

* Install playwright dependencies: `pipenv run install-playwright-dependencies`

* Run playwright tests: `pipenv run e2e-tests`

## Features

* CI/CD config: Github Actions

## Test run options:

* Run tests on chrome and firefox: `pipenv run e2e-tests-all-browsers`