# Instalar as dependências
- `pip install beautifulsoup4`
- `pip install requests`

## Executar ambiente:
- `.\env\Scripts\activate`

## Executar função chamada
- `cd ./env/Scripts`
- `python manager.py`

## Parâmetros:
- Parâmetro 1: producao, processamento, comercializacao, importacao, exportacao
- Parâmetro 2 para PROCESSAMENTO: Viniferas = 01, Americanas e híbridas = 02, Uvas de mesa = 03, Sem classificação = 04
- Parâmetro 2 para IMPORTACAO: Vinhos de mesa = 01, Espumantes = 02, Uvas frescas = 03, Uvas passas = 04, Suco de uva = 05
- Parâmetro 2 para EXPORTACAO: Vinhos de mesa = 01, Espumantes = 02, Uvas frescas = 03, Suco de uva = 04
- Parâmetro 3: ano inicial
- Parâmetro 4: ano final (deixe vazio se não houver)

Para testar, basta mudar os parâmetros em:

```python
if __name__ == "__main__":
    asyncio.run(main('processamento', '01', 1970, 2022))
