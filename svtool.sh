#!/bin/bash

# Ativa o ambiente virtual
source "$(dirname "$0")/venv/bin/activate"

# Executa o script principal
python3 "$(dirname "$0")/src/main.py" "$@"
