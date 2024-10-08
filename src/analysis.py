import pandas as pd

def calcular_total_vendas(df_vendas, df_produtos):

    try:
        df_vendas_produtos = pd.merge(df_vendas, df_produtos, left_on='produto_id', right_on='id')
        df_vendas_total = df_vendas_produtos.groupby('nome')['valor'].sum().reset_index()
        return df_vendas_total
    except KeyError as e:
        print(f"Erro ao calcular total de vendas: coluna não encontrada {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro inesperado ao calcular total de vendas: {e}")
        return pd.DataFrame()

def calcular_vendas_por_cliente(df_vendas, df_clientes):
  
    try:
        df_vendas_clientes = pd.merge(df_vendas, df_clientes, left_on='cliente_id', right_on='id')
        df_vendas_total_clientes = df_vendas_clientes.groupby('nome')['valor'].sum().reset_index()
        return df_vendas_total_clientes
    except KeyError as e:
        print(f"Erro ao calcular vendas por cliente: coluna não encontrada {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro inesperado ao calcular vendas por cliente: {e}")
        return pd.DataFrame()
