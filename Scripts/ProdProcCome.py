import requests
from bs4 import BeautifulSoup




def extrairDadosProdProcCome(link, ano):


    requisicao = requests.get(link)
    print (requisicao)
    
    if requisicao.status_code == 200:
        # Analisando o HTML com BeautifulSoup
        soup = BeautifulSoup(requisicao.text, "html.parser")

        # Selecionando tabela
        tabela = soup.find('table', class_='tb_base tb_dados')

        # Inicializando lista para armazenar os dados
        produtos = []
        totalQuantidade = 0
        if tabela:
            # Buscando todas as linhas da tabela que contêm itens e subitens
            linhas = tabela.find_all('tr')

            item_atual = None

            for linha in linhas:
                # Verificando se é um item
                if linha.find('td', class_='tb_item'):
                    if item_atual:
                        produtos.append(item_atual)
                    item_atual = {
                        "produto": linha.find('td', class_='tb_item').get_text(strip=True),
                        "quantidade": removerPontosConverterParaInt(linha.find_all('td', class_='tb_item')[1].get_text(strip=True)),
                        "subitem": []
                    }
                # Verificando se é um subitem
                elif linha.find('td', class_='tb_subitem'):
                    subitem_quantidade = linha.find_all('td', class_='tb_subitem')
                    subitem_nome = subitem_quantidade[0].get_text(strip=True)
                    subitem_quantidade = removerPontosConverterParaInt(subitem_quantidade[1].get_text(strip=True))
                    if isinstance(subitem_quantidade, int):
                        totalQuantidade = totalQuantidade + subitem_quantidade
                    subitem = {
                        "item": subitem_nome,
                        "quantidade":  subitem_quantidade
                    }
                    item_atual["subitem"].append(subitem)

            if item_atual:
                produtos.append(item_atual)

        else:
            print("Tabela não encontrada.")

        # Exibindo dados
        dados_completos = {
            "ano": ano,
            "totalQuantidade": totalQuantidade,
            "produtos": produtos
        }
        return dados_completos

    else:
        print("Erro ao acessar a página:", requisicao.status_code)

def  removerPontosConverterParaInt(valor):
    # Verificar se a string contém apenas números e pontos
    if all(caractere.isdigit() or caractere == '.' for caractere in valor):
        # Remover os pontos
        valor_sem_pontos = valor.replace('.', '')
        # Converter para inteiro
        numero_inteiro = int(valor_sem_pontos)
        return numero_inteiro
    else:
        return valor
