# Introdução à Ciência de Dados, 2018.2 - UFAL
Repositório do projeto da disciplina Introdução à Ciência de Dados, semestre 2018.2, pela Universidade Federal de Alagoas. 

#### Observação:
Instruções relacionadas ao WebScraper podem ser encontradas na branch [WebScraper](https://github.com/victoraccete/ICD_20182/tree/webScraper).

#### Dependências necessárias:
- Pandas
- Geopandas
- Plotly
- Bokeh
- Matplotlib
#### Instalação
##### Conda
```
conda install -c plotly plotly 
```
```
conda install -c conda-forge geopandas
```
```
conda install pandas
```
```
conda install -c bokeh bokeh 
```
```
conda install -c conda-forge matplotlib 
```

#### Instruções de uso
Após baixar todos os arquivos com o WebScraper, os arquivos ficarão no diretório Downloads do computador, por padrão. Para mais informações, favor verificar o readme da branch [WebScraper](https://github.com/victoraccete/ICD_20182/tree/webScraper). Caso os relatórios baixados não estejam no diretório de Downloads, o código precisará ser alterado para ler na pasta desejada. 

Prefira executar o código a partir do diretório do usuário, para evitar problemas com os diretórios. 

Uma vez que os arquivos estiverem baixados, o código [cleanandmerge.py](https://github.com/victoraccete/ICD_20182/blob/master/cleanandmerge.py) irá ler todos os arquivos, tratar e organizar os dados e agrupar num único dataframe que será exportado como um arquivo .csv no diretório de execução do código. 

Uma vez que o cleanandmerge.py tiver finalizado e corretamento exportado o .csv, o [Jupyter Notebook](https://github.com/victoraccete/ICD_20182/blob/master/map_plot.ipynb) pode ser executado para visualizar os demais tratamentos de dados e os mapas e gráficos gerados. 
