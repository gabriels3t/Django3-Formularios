def origem_destino(origem,destino,lista_de_erros):
    """
    Verificando se origem e destino são iguais
    """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo,nome_campo,lista_de_erros):
    """
    Verifica se possui algum numero
    """
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números nessa campo'

def data_ida_maior_data_volta(data_ida,data_volta,lista_de_erros):
    """
    Verifica se a data de ida é maior que a data de volta
    """
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser menor que data de ida'

def data_ida_menor_data_de_hoje(data_id,data_pesquisa,lista_de_erros):
    """
    Verifica se a data de ida é menor que a data de hoje
    """

    if data_id < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que hoje'