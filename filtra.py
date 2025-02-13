import pandas as pd

def filtrar_csv(arquivo_entrada, arquivo_saida, coluna_filtro, valor_filtro):
    """
    Filtra um arquivo CSV baseado em uma coluna e um valor específico.

    :param arquivo_entrada: Caminho do arquivo CSV de entrada.
    :param arquivo_saida: Caminho do arquivo CSV de saída.
    :param coluna_filtro: Nome da coluna para aplicar o filtro.
    :param valor_filtro: Valor a ser filtrado na coluna especificada.
    """
    try:
        # Lendo o CSV
        df = pd.read_csv(arquivo_entrada, sep=',')
        
        # Aplicando o filtro
        df_filtrado = df[df[coluna_filtro] == valor_filtro]
        
        # Salvando o resultado
        df_filtrado.to_csv(arquivo_saida, index=False, sep=',')
        print(f"Arquivo filtrado salvo como: {arquivo_saida}")
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

# Caminhos do arquivo
arquivo_entrada = "test-dataset.csv"
arquivo_saida = "test-dataset-filtrado.csv"

# Definir critérios de filtragem
coluna_filtro = "ClientCountry"  # Filtro por país do cliente
valor_filtro = "us"  # Apenas registros dos EUA

# Aplicar filtro
filtrar_csv(arquivo_entrada, arquivo_saida, coluna_filtro, valor_filtro)
