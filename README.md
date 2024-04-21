# webscrappingembrapa
this code MVP make web scraping on website http://vitibrasil.cnpuv.embrapa.br/ utilizing python and the library: beautifulsoup 

# pip install beautifulsoup4
# pip install requests


# Executar ambiente:
## .\env\Scripts\activate

# Executar função chamada
## cd ./env/Scripts
## python manager.py

# parametros 1 : producao, processamento, comercializacao, importacao, exportacao
# parametros 2 para PROCESSAMENTO: Viniferas = 01 Americanas e híbridas = 02 Uvas de mesa = 03 Sem classificação = 04
# parametros 2 para IMPORTACAO: Vinhos de mesa = 01 Espumantes = 02 Uvas frescas = 03 Uvas passas = 04 Suco de uva = 05
# parametros 2 para EXPORTACAO: Vinhos de mesa = 01 Espumantes = 02 Uvas frescas = 03  Suco de uva = 04
# parametro 3: ano inicial
# parametro 4: ano final, se não tiver deixar vazio

para testa basta mudar os parametros em:


if __name__ == "__main__":
    asyncio.run(main('processamento', '01', 1970,2022))
