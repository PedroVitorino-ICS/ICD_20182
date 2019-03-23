import pandas as pd

def read_df(filename):
    table = pd.read_html(filename)
    return table[0]

def clean_df(df):
    df = df.drop(columns={df.columns[6], df.columns[8], df.columns[10], 
                          df.columns[12]})
    df = rename_df_columns(df)
    return delete_total_rows(df)

def rename_df_columns(df): 
    df.columns = ['região', 'cod uf', 'uf', 'cod ibge', 'município', 
                  'peso muito baixo', 'peso baixo', 'peso adequado', 
                  'peso elevado', 'total']
    return df

def insert_year_and_sex(df, year, sex):
    df.insert(5, 'sexo', 'F')
    df.insert(0, 'ano', '2008')
    return df

def delete_total_rows(df):
    # https://stackoverflow.com/questions/35186291/how-do-i-delete-rows-not-starting-with-x-in-pandas-or-keep-rows-starting-with
    # Fazendo com que df receba apenas os valores que não começam com 'TOTAL'
    # sem o ~ ele recebe todos os que começam com 'TOTAL', mas o contrário é o desejado
    # para depuração: print(df[df['região'].astype(str).str.startswith('TOTAL')])
    return df[~df['região'].astype(str).str.startswith('TOTAL')]

#Até o AcompEstadoNutricional10, é do sexo feminino
def female_appends():
    for i in range(0,11):
        filename = 'Downloads/AcompEstadoNutricional'
        print(i)
        if(i == 0 or i != 0):
            buff = read_df(filename + '.xls')
            # criar com o ano 2008
        else:
            appendix = str(i)
            filename = filename + ' (' + appendix + ')'
            buff = read_df(filename + '.xls')
            # Criar com o ano 2008+i
            # AQUI: função para concatenar os buffers
    return buff

df = read_df('Downloads/AcompEstadoNutricional.xls')
df = clean_df(df)
df = insert_year_and_sex(df, 2008, 'F')
dataframe = df
buff = female_appends()