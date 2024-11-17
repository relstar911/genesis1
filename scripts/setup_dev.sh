#!/bin/bash

# Create necessary directories
mkdir -p logs data models

# Install Poetry (if not installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Initialize pre-commit
poetry run pre-commit install

# Create initial log files
touch logs/api.log

echo "Development environment setup complete!" 