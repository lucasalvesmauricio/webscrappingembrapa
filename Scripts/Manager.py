from ProdProcCome import extrairDadosProdProcCome
from ImportaExporta import extrairImportaExporta


import asyncio


async def extrair_dados_async(tipo, ano, opcao):



    link = ''
    if(tipo == 'producao'):
        link = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02"
    if(tipo == 'processamento'):
        link = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao=subopt_{opcao}"
    if(tipo == 'comercializacao'):
        link = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04"
    if(tipo == 'importacao'):
        link = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_{opcao}"
    if(tipo == 'exportacao'):
        link = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_{opcao}"

    if(tipo == 'producao' or tipo == 'processamento' or tipo == 'comercializacao'): 
        return extrairDadosProdProcCome(link, ano)
    else:
        return extrairImportaExporta(link, ano)

data =[]






async def main(tipo, subMenu, anoInicial, anoFinal=None ):
    
     # Se anoFinal não for fornecido, realizar a busca apenas para o anoInicial
    if anoFinal is None:
        anos = [anoInicial]
    else:
        anos = range(anoInicial, anoFinal + 1)


    tasks = [ extrair_dados_async(tipo, ano, subMenu) for ano in anos]
    resultados = await asyncio.gather(*tasks)
    for resultado in resultados:
        data.append(resultado)

#parametros 1 : producao, processamento, comercializacao, importacao, exportacao
#parametros 2 para PROCESSAMENTO: Viniferas = 01 Americanas e híbridas = 02 Uvas de mesa = 03 Sem classificação = 04
#parametros 2 para IMPORTACAO: Vinhos de mesa = 01 Espumantes = 02 Uvas frescas = 03 Uvas passas = 04 Suco de uva = 05
#parametros 2 para EXPORTACAO: Vinhos de mesa = 01 Espumantes = 02 Uvas frescas = 03  Suco de uva = 04
#parametro 3: ano inicial
#parametro 4: ano final 
if __name__ == "__main__":
    asyncio.run(main('processamento', '01', 1970,2022))

# Exibindo a lista de dados
print(data)