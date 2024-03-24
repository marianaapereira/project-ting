import sys
from pathlib import Path


def txt_importer(path_file):
    pf = Path(path_file)

    if not pf.exists():
        error = f"Arquivo {path_file} não encontrado"
        return print(error, file=sys.stderr)
    elif pf.suffix != ".txt":
        error = "Formato inválido"
        return print(error, file=sys.stderr)

    with open(path_file, "r") as file:
        content = file.read().split("\n")
    return content
