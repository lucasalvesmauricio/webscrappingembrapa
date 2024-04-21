import requests
from bs4 import BeautifulSoup


total = 0

def extrairImportaExporta(link, ano, opcao):
    try:
        

        requisicao = requests.get(link)
        print(requisicao)

        if requisicao.status_code == 200:
            # Analisando o HTML com BeautifulSoup
            soup = BeautifulSoup(requisicao.text, "html.parser")

            # Selecionando tabela
            tabela = soup.find('table', class_='tb_base tb_dados')
            tbody = tabela.find('tbody')

            # Inicializando lista para armazenar os dados
            produtos = []
            
            totalQuantidade = 0
            totalValor = 0
            if tabela:
                # Buscando todas as linhas da tabela que contêm itens e subitens
                
                linhas = tbody.find_all('tr')
                for linha in linhas:
                    
                    dados = linha.find_all('td')
                    pais = dados[0].get_text(strip=True)
                    quantidade = removerPontosConverterParaInt(dados[1].get_text(strip=True))
                    if isinstance(quantidade, int):
                        totalQuantidade = totalQuantidade + quantidade
                    valor = removerPontosConverterParaInt(dados[2].get_text(strip=True))
                    if isinstance(valor, int):
                        totalValor = totalValor + valor
                    # Adicionar os dados na lista de produtos
                    produtos.append({'país': pais, 'quantidade': quantidade, 'valor': valor})

                

            else:
                print("Tabela não encontrada.")
        
            dados_completos = {
                "ano": ano,
                "totalQuantidade": totalQuantidade,
                "totalValor": totalValor,
                "produtos": produtos
            }

            return dados_completos


        else:
            print("Erro ao acessar a página:", requisicao.status_code)

    except Exception as e:
        print("Ocorreu um erro:", e)
        return (404)


def removerPontosConverterParaInt(valor):
    global total
    try:
        # Verificar se a string contém apenas números e pontos
        if all(caractere.isdigit() or caractere == '.' for caractere in valor):
            # Remover os pontos
            valor_sem_pontos = valor.replace('.', '')
            # Converter para inteiro
            numero_inteiro = int(valor_sem_pontos)
            total = total + numero_inteiro
            return numero_inteiro
        else:
            return valor
    except Exception as e:
        print("Ocorreu um erro ao remover pontos e converter para inteiro:", e)

