import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

def initialize_driver():
    driver = webdriver.Chrome()
    driver.get("http://dabsistemas.saude.gov.br/sistemas/sisvanV2/relatoriopublico/index")
    os.makedirs('relats', exist_ok=True) # Criando a pasta para colocar os relatorios baixados
    print(driver.title)
    return driver

def choose_report(index, driver):
    driver.implicitly_wait(6) # para dar tempo de carregar os elementos da página
    elements = [];
    # a classe btn-success refere-se aos botões de selecionar relatório
    elements = driver.find_elements_by_class_name("btn-success");
    print(elements[index].text)
    elements[index].click() # clicando no primeiro relatorio (estado nutricional)

def year_select(driver):
    driver.implicitly_wait(6)
    select = Select(driver.find_element_by_id("nuAno"))
    select.select_by_visible_text("2008")

driver = initialize_driver()
choose_report(0, driver)
year_select(driver)
