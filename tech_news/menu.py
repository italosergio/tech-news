import sys


# Requisito 12
def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n "
        "0 - Popular o banco com notícias;\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por tag;\n "
        "4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n "
        "6 - Listar top 5 categorias;\n "
        "7 - Sair."
    )
    options = [
        "Digite quantas notícias serão buscadas:",
        "Digite o título:",
        "Digite a data no formato aaaa-mm-dd:",
        "Digite a tag:",
        "Digite a categoria:",
    ]
    INPUT_INDEX = input("Enter number: ")

    try:
        if 0 <= int(INPUT_INDEX) <= 5:
            print(options[int(INPUT_INDEX)])
        else:
            print("Opção inválida", file=sys.stderr)
    except ValueError:
        print("Digite um número válido", file=sys.stderr)
