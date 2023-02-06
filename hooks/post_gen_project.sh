#!/usr/bin/env bash

poetry install

# create the first git commit
git init
git add .
git commit -m "Generate project with Cookiecutter"


source $(poetry env info --path)/bin/activate
maturin develop
pytest
