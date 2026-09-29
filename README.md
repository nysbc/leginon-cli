# leginon-cli

This repository contains a simple CLI for performing various maintenance operations on the Leginon project database.

## Building the PEX file

Per [here](https://github.com/edaniels/uv-pex-example/blob/main/justfile):

```
# Make a venv for pex with the desired Python interpreter
uv python install cpython-3.9.25-linux-x86_64-gnu
uv venv -p cpython-3.9.25-linux-x86_64-gnu .venv 
source .venv/bin/activate
uv pip install pex
# Export requirements to requirements.txt
uv pip compile pyproject.toml -o requirements.txt --universal
# Create pex file
pex 'leginoncli @ git+https://github.com/nysbc/leginon-cli.git' -r requirements.txt -c leginon-cli -o leginon-cli.pex
```
