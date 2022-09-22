import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


# Requisito 12
def return_by_option(index, input_options, function_options):
    if int(index) == 0:
        return function_options[int(index)](int(index))
    elif int(index) == 7:
        print("Encerrando script")
    else:
        if input_options[int(index)] != "":
            response = input(input_options[int(index)])
            return function_options[int(index)](str(response))
        else:
            return function_options[int(index)]()


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
    input_options = [
        "Digite quantas notícias serão buscadas:",
        "Digite o título:",
        "Digite a data no formato aaaa-mm-dd:",
        "Digite a tag:",
        "Digite a categoria:",
        "",
        "",
        "",
    ]
    functions = [
        get_tech_news,
        search_by_title,
        search_by_date,
        search_by_tag,
        search_by_category,
        top_5_news,
        top_5_categories,
    ]
    INPUT_INDEX = input("Enter number: ")

    try:
        if 0 <= int(INPUT_INDEX) <= 7:
            return return_by_option(INPUT_INDEX, input_options, functions)
        else:
            print("Opção inválida", file=sys.stderr)

    except ValueError:
        print("Digite um número válido", file=sys.stderr)
