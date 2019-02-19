import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://dabsistemas.saude.gov.br/sistemas/sisvanV2/relatoriopublico/index")
print(driver.title)

#os.makedirs('relats', exist_ok=True) # Criando a pasta para colocar os relatorios baixados

driver.implicitly_wait(6) # para dar tempo de carregar os elementos da página

# a classe btn-success refere-se aos botões de selecionar relatório
elements = [];
elements = driver.find_elements_by_class_name("btn-success");
print(elements[0])
print(elements[0].text)
elements[0].click() # clicando no primeiro relatorio (estado nutricional)

#driver.close()
