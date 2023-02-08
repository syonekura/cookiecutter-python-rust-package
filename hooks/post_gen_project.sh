#!/usr/bin/env bash

poetry install

# Linting and formatting
poetry run black python
poetry run isort python
poetry run ruff python
poetry run mypy python

# create the first git commit
git init
git add .
git commit -m "Generate project with Cookiecutter"


poetry run maturin develop --release
poetry run pytest --cov
