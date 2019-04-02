import plotly 
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

def setup_df():
    plotly.tools.set_credentials_file(username='pedro.vitorino20',
                                  api_key='warhero23')        
    df = pd.read_csv('DfUnic.csv')
    df.head()    
    states_df = df.groupby(['cod uf', 'uf', 'sexo', 'ano'], as_index = False).sum()
    states_df = states_df.drop('cod ibge', axis = 1)
    return states_df


def create_plots(state_cod, states_df):
    df_statesM = states_df[states_df['cod uf']==state_cod][states_df['sexo'] 
                            == 'M']
    state_name = df_statesM['uf'].iloc[0]
    
    
    df_statesM.ano = pd.to_datetime(states_df.ano, format='%Y')
    
    trace0 = go.Scatter(
                    x=df_statesM.ano,
                    y=df_statesM['peso muito baixo'],
                    name = "Peso Muito Baixo",
                    line = dict(color = '#990000'),
                    opacity = 0.8)
    
    trace1 = go.Scatter(
                    x=df_statesM.ano,
                    y=df_statesM['peso baixo'],
                    name = "Peso Baixo",
                    line = dict(color = 'orange'),
                    opacity = 0.8)
                    
    trace2 = go.Scatter(
                    x=df_statesM.ano,
                    y=df_statesM['peso adequado'],
                    name = "Peso Adequado",
                    line = dict(color = 'green'),
                    opacity = 0.8)
    
    trace3 = go.Scatter(
                    x=df_statesM.ano,
                    y=df_statesM['peso elevado'],
                    name = "Peso Elevado",
                    line = dict(color = 'blue'),
                    opacity = 0.8)
        
    df_states_F = states_df[states_df['cod uf']==state_cod][states_df['sexo'] 
                            == 'F']
    
    df_states_F.ano = pd.to_datetime(df_states_F.ano, format='%Y')
    
    trace4 = go.Scatter(
                    x=df_states_F.ano,
                    y=df_states_F['peso muito baixo'],
                    name = "Peso Muito Baixo",
                    line = dict(color = '#990000'),
                    opacity = 0.8,
                    xaxis='x2',
                    yaxis='y2')
    
    trace5 = go.Scatter(
                    x=df_states_F.ano,
                    y=df_states_F['peso baixo'],
                    name = "Peso Baixo",
                    line = dict(color = 'orange'),
                    opacity = 0.8,
                    xaxis='x2',
                    yaxis='y2')
                    
    trace6 = go.Scatter(
                    x=df_states_F.ano,
                    y=df_states_F['peso adequado'],
                    name = "Peso Adequado",
                    line = dict(color = 'green'),
                    opacity = 0.8,
                    xaxis='x2',
                    yaxis='y2')
    
    trace7 = go.Scatter(
                    x=df_states_F.ano,
                    y=df_states_F['peso elevado'],
                    name = "Peso Elevado",
                    line = dict(color = 'blue'),
                    opacity = 0.8,
                    xaxis='x2',
                    yaxis='y2')
    
    trace8 = go.Box(y = states_df.loc[states_df['sexo'] == "M", 'peso muito baixo'],
                    name = 'Peso Muito Baixo-M',
                    marker = {'color': '#ff0000'},
                    xaxis='x3',
                    yaxis='y3')
                             
    trace9 = go.Box(y = states_df.loc[states_df['sexo'] == "F", 'peso muito baixo'],
                    name = 'Peso Muito Baixo-F',
                    marker = {'color': '#ffcccc'},
                    xaxis='x3',
                    yaxis='y3')
                              
    trace10 = go.Box(y = states_df.loc[states_df['sexo'] == "M", 'peso baixo'],
                    name = 'Peso Baixo-M',
                    marker = {'color': '#ff8000'},
                    xaxis='x3',
                    yaxis='y3')
                              
    trace11 = go.Box(y = states_df.loc[states_df['sexo'] == "F", 'peso baixo'],
                    name = 'Peso Baixo-F',
                    marker = {'color': '#ffff99'},
                    xaxis='x3',
                    yaxis='y3')
    
    trace12 = go.Box(y = states_df.loc[states_df['sexo'] == "M", 'peso adequado'],
                    name = 'Peso Adequado-M',
                    marker = {'color': '#006600'},
                    xaxis='x3',
                    yaxis='y3')
                              
    trace13 = go.Box(y = states_df.loc[states_df['sexo'] == "F", 'peso adequado'],
                    name = 'Peso Adequado-F',
                    marker = {'color': '#99ff99'},
                    xaxis='x3',
                    yaxis='y3')
    
    trace14 = go.Box(y = states_df.loc[states_df['sexo'] == "M", 'peso elevado'],
                    name = 'Peso Elevado-M',
                    marker = {'color': '#000080'},
                    xaxis='x3',
                    yaxis='y3')
                              
    trace15 = go.Box(y = states_df.loc[states_df['sexo'] == "F", 'peso elevado'],
                    name = 'Peso Elevado-F',
                    marker = {'color': '#b3daff'},
                    xaxis='x3',
                    yaxis='y3')
    
    layout = go.Layout(
            dict(title = "Estado Por Peso " + state_name),
            xaxis=dict(
            title = "Masculino", 
            domain=[0, 0.45]
        ),
        yaxis=dict(
            domain=[0, 0.45]
        ),
         xaxis2=dict(
            title = "Feminino",
            domain=[0.55, 1]
        ),
        yaxis2=dict(
            domain=[0, 0.45],
            anchor='x2'
        ),
        xaxis3=dict(
            domain=[0, 1],
            anchor='y3'
        ),
        yaxis3=dict(
            domain=[0.55, 1]
        )
    )
        
    data = [trace0,trace1, trace2, trace3, trace4, trace5, trace6, trace7,
            trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15]
    
    fig = dict(data=data, layout=layout)
    return fig

def generate_plots_for_all_states(states_df):
    # Criando esse novo DF para ter um DF apenas como uma lista de todos os
    # estados e seus respectivos códigos
    states_only = states_df.groupby(['cod uf', 'uf'], as_index = False).sum()
    for index, row in states_only.iterrows():
        fig = create_plots(row['cod uf'], states_df)
        py.plot(fig, filename = 'plots/' + str(int(row['cod uf']))+ '.html', 
                auto_open=False)

states_df = setup_df()
generate_plots_for_all_states(states_df)
#fig = create_plots(27, states_df)
#url = py.plot(fig, filename = str(state_cod))

