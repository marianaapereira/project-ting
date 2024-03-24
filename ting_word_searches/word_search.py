def exists_word(word, instance):
    data_list = list()

    for existent_file in instance.queue:
        index_list = list()
        file_lines = existent_file["linhas_do_arquivo"]

        for line in file_lines:
            if word.lower() in line.lower():
                index = file_lines.index(line) + 1
                index_list.append({"linha": index})

        if len(index_list) > 0:
            data = {
                "palavra": word,
                "arquivo": existent_file["nome_do_arquivo"],
                "ocorrencias": index_list
            }

            data_list.append(data)

    return data_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
