import sys
from ting_file_management import file_management


def process(path_file, instance):
    file_exists = any(
        (
            existent_file["nome_do_arquivo"] == path_file
        ) for existent_file in instance.queue
    )

    if not file_exists:
        file_lines = file_management.txt_importer(path_file)
        file_length = len(file_lines)
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": file_length,
            "linhas_do_arquivo": file_lines
        }

        instance.enqueue(data)
        print(data)


def remove(instance):
    response = instance.dequeue()

    if response is None:
        return print("Não há elementos")

    else:
        path_file = response["nome_do_arquivo"]
        return print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        response = instance.search(position)
        return print(response)
    except IndexError:
        error = "Posição inválida"
        return print(error, file=sys.stderr)
