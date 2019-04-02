# Introdução à Ciência de Dados, 2018.2 - UFAL
Repositório do projeto da disciplina Introdução à Ciência de Dados, semestre 2018.2, pela Universidade Federal de Alagoas. 

## Instruções para instalação do WebScraper
O Chromedriver já está no repositório. No entanto, ele é referente às versões 71 à 73 do Chrome. Versões mais antigas ou versões mais novas devem ser baixadas [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads).

A instalação da biblioteca Selenium pode ser feita através de:
```
conda install -c conda-forge selenium 
```
Ou de:
```
pip install selenium
```
## Instruções de utilização
O Chromedriver deve permanecer no mesmo diretório de execução do WebScraper. 

O primeiro passo é executar o Chromedriver e não finalizá-lo enquanto o código não terminar de rodar e os downloads forem concluídos. 

Importante: se o Chromedriver for finalizado antes dos downloads serem concluídos, alguns arquivos não serão baixados. 


Após executar o Chromedriver, o código poderá ser executado. Então é só aguardar. Os downloads irão para o diretório de downloads do Chrome, que por padrão é a pasta Downloads. 

### Em caso de falhas
Recomenda-se finalizar a execução do WebScraper e é importante que, na pasta downloads, sejam excluídos todos os arquivos baixados pelo WebScraper. Os arquivos começam com o nome AcompEstadoNutricional. 

Então pode-se executar novamente o WebScraper.
