from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

def initialize_driver():
    driver = webdriver.Chrome()
    driver.get("http://dabsistemas.saude.gov.br/sistemas/sisvanV2/relatoriopublico/index")
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

def month_select(driver):
    driver.implicitly_wait(2)
    select = Select(driver.find_element_by_id("nuMes"))
    select.select_by_visible_text("TODOS")

def groupby_select(driver):
    driver.implicitly_wait(2)
    select = Select(driver.find_element_by_name("tpFiltro"))
    select.select_by_visible_text("MUNICÍPIO")

def state_and_city_select(driver):
    driver.implicitly_wait(2)
    select = Select(driver.find_element_by_id("coUfIbge"))
    select.select_by_visible_text("TODOS")
    driver.implicitly_wait(1)
    select = Select(driver.find_element_by_id("coMunicipioIbge"))
    select.select_by_visible_text("TODOS")

def region_select(driver):
    driver.implicitly_wait(2)
    select = Select(driver.find_element_by_name("st_cobertura"))
    select.select_by_visible_text("TODAS")

def age_select(driver):
    driver.implicitly_wait(1)
    select = Select(driver.find_element_by_name("nu_ciclo_vida"))
    select.select_by_visible_text("CRIANÇA")
    driver.implicitly_wait(5)
    select = Select(driver.find_element_by_id("nu_idade_inicio"))
    select.select_by_visible_text("0")
    select = Select(driver.find_element_by_id("nu_idade_fim"))
    select.select_by_visible_text("< 2 anos")

def sex_select(driver):
    driver.implicitly_wait(1)
    select = Select(driver.find_element_by_name("ds_sexo2"))
    select.select_by_visible_text("FEMININO")

def download_report(driver):
    element = driver.find_element_by_id("Download")
    element.click()

if __name__ == '__main__':
    driver = initialize_driver()
    choose_report(0, driver)
    year_select(driver)
    month_select(driver)
    groupby_select(driver)
    state_and_city_select(driver)
    region_select(driver)
    age_select(driver)
    sex_select(driver)
    download_report(driver)

