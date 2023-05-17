from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep


class ComputerRegistration:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_website(self, url):
        self.driver.get(url)

    def register_computer(self, patrimonio, maquina, des, space):
        sleep(3)
        # Clicar no botão "Adicionar"
        adicionar = self.driver.find_element(By.ID, 'Add')
        adicionar.click()

        sleep(3)
        # Preencher campo "Patrimonio"
        patrimonio_element = self.driver.find_element(By.XPATH, '//*[@id="patrimony-textfield"]')
        patrimonio_element.click()
        sleep(3)
        patrimonio_element.send_keys(patrimonio)

        # Preencher campo "Maquina"
        maquina_element = self.driver.find_element(By.ID, 'abbreviation-textfield')
        maquina_element.click()
        sleep(3)
        maquina_element.send_keys(maquina)

        # Preencher campo "Des"
        des_element = self.driver.find_element(By.ID, 'description-textfield')
        des_element.click()
        sleep(3)
        des_element.send_keys(des)

        # Selecionar espaço
        espa_element = self.driver.find_element(By.ID, 'space-name-textfield')
        espa_element.click()
        sleep(3)
        space_element = espa_element.find_element(By.XPATH, f'/html/body/div[3]/div/div[3]/form/div/div[4]/ul/li[{space}]')
        space_element.click()

        # Clicar no botão "Salvar"
        save = self.driver.find_element(By.ID, 'save-bnt')
        sleep(3)
        save.click()
        sleep(2)
# Criar computador e clicar no botão de cancelar        
class ComputerRegistrationCancel:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_website(self, url):
        self.driver.get(url)

    def register_computer(self, patrimonio, maquina, des, space):
        sleep(3)
        # Clicar no botão "Adicionar"
        adicionar = self.driver.find_element(By.ID, 'Add')
        adicionar.click()

        sleep(3)
        # Preencher campo "Patrimonio"
        patrimonio_element = self.driver.find_element(By.XPATH, '//*[@id="patrimony-textfield"]')
        patrimonio_element.click()
        sleep(3)
        patrimonio_element.send_keys(patrimonio)

        # Preencher campo "Maquina"
        maquina_element = self.driver.find_element(By.ID, 'abbreviation-textfield')
        maquina_element.click()
        sleep(3)
        maquina_element.send_keys(maquina)

        # Preencher campo "Des"
        des_element = self.driver.find_element(By.ID, 'description-textfield')
        des_element.click()
        sleep(3)
        des_element.send_keys(des)

        # Selecionar espaço
        espa_element = self.driver.find_element(By.ID, 'space-name-textfield')
        espa_element.click()
        sleep(3)
        space_element = espa_element.find_element(By.XPATH, f'/html/body/div[3]/div/div[3]/form/div/div[4]/ul/li[{space}]')
        space_element.click()
        
        cancel = self.driver.find_element(By.ID, 'cancel-bnt')
        sleep(3)
        cancel.click()
        sleep(3)


