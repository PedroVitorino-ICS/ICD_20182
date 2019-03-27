import pandas as pd

# Essa função existe porque queremos apenas um único caractere
def get_sex_character(sex):
    if isinstance(sex, str):
        return sex[0]
    else:
        return None

def read_df(filename):
    table = pd.read_html(filename)
    return table[0]

def clean_df(df, filename):
    df = df.drop(columns={df.columns[6], df.columns[8], df.columns[10], 
                          df.columns[12]})
    df = rename_df_columns(df)
    sex = get_sex_character(find_sex(filename))
    year = find_year(filename)
    df = insert_year_and_sex(df, year, sex)
    return delete_total_rows(df)

def rename_df_columns(df): 
    df.columns = ['região', 'cod uf', 'uf', 'cod ibge', 'município', 
                  'peso muito baixo', 'peso baixo', 'peso adequado', 
                  'peso elevado', 'total']
    return df

def insert_year_and_sex(df, year, sex):
    df.insert(5, 'sexo', sex)
    df.insert(0, 'ano', year)
    return df

# ENTRA: o arquivo
# RETORNA: str contendo o sexo em letras capitais. 
def find_sex(file):
    with open(file) as f:
        head = [next(f) for x in range(400)]
        # apenas as 400 primeiras linhas porque com certeza esta nessa margem
    for i in head:
        index = head.index(i)
        if('MASCULINO' in head[index]):
            return 'MASCULINO'
        elif('FEMININO' in head[index]):
            return 'FEMININO'
        else:
            if(index >= len(head)):
                print("Não foi possível encontrar o sexo.")
    return None

def find_year(file):
    with open(file) as f:
        head = [next(f) for x in range(400)]
        # apenas as 400 primeiras linhas porque com certeza esta nessa margem
    for i in head:
        index = head.index(i)
        if('Ano: </strong>' in head[index]):
            year = head[index].split('Ano: </strong>', 1)[1]
            return int(year[:4])
    print("Não foi possível encontrar o ano.")
    return None    

def delete_total_rows(df):
    # https://stackoverflow.com/questions/35186291/how-do-i-delete-rows-not-starting-with-x-in-pandas-or-keep-rows-starting-with
    # Fazendo com que df receba apenas os valores que não começam com 'TOTAL'
    # sem o ~ ele recebe todos os que começam com 'TOTAL', mas o contrário é o desejado
    # para depuração: print(df[df['região'].astype(str).str.startswith('TOTAL')])
    return df[~df['região'].astype(str).str.startswith('TOTAL')]


def clean_and_merge_all_files():
    for i in range(0,4):
        filename = 'Downloads/AcompEstadoNutricional'
        print('Index: ' + str(i))
        if(i == 0):
            df = read_df(filename + '.xls')
            df = clean_df(df, filename + '.xls')
            print(filename + '.xls')
        else:
            appendix = str(i)
            filename = filename + ' (' + appendix + ')'
            buff = read_df(filename + '.xls')
            buff = clean_df(buff, filename + '.xls')
            df = df.append(buff)
    return df
                

############ MAIN ################
filename = 'Downloads/AcompEstadoNutricional.xls'
#df = read_df(filename)
#df = clean_df(df, filename)
df = clean_and_merge_all_files()
#dtaframe = df