#!/usr/bin/env bash

poetry install

# create the first git commit
git init
git add .
git commit -m "Generate project with Cookiecutter"


poetry run maturin develop
poetry run pytest --cov
