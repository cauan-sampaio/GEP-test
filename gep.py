from asyncio import Event
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.get("http://localhost:3000/computers")
driver.current_url
sleep(3)

# Clicar no botão "Adicionar"
adicionar = driver.find_element(By.ID, 'Add')
adicionar.click()

# Encontrar janela
def encontra_janela(palavra: str) -> bool:
    windows = driver.window_handles 
    for win in windows:
        driver.switch_to.window(win)
    if palavra in driver.current_url:
        print(f'Encontrei a janela {driver.current_url}')
        return True
    print(f'Não encontrei nenuma janela com a palavra: {palavra}')
    return False

encontra_janela('http://localhost:3000/computers')
sleep(3)

# Preencher campo "Patrimonio"
patrimonio = driver.find_element(By.ID, 'patrimony-textfield')
patrimonio.click()
sleep(3)
patrimonio.send_keys(' jjhjgj-1221344321+77686656')

# Preencher campo "Maquina"
maquina = driver.find_element(By.ID, 'abbreviation-textfield')
maquina.click()
sleep(3)
maquina.send_keys(' pc 011111')

# Preencher campo "Des"
des = driver.find_element(By.ID, 'description-textfield')
des.click()
sleep(3)
des.send_keys('Intel i5 4 geração, memória RAM: 8 GB, HD:1TB, placa de vídeo:Integrada')

# Selecionar espaço
espa = driver.find_element(By.ID, 'space-name-textfield')
espa.click()
sleep(3)
espa.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/form/div/div[4]/ul/li[1]').click()

# Clicar no botão "Salvar"
save = driver.find_element(By.ID, 'save-bnt')
sleep(3) 
save.click()
sleep(2)

# Capturar o alerta "Computador cadastrado com sucesso"
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    if "Computador cadastrado com sucesso" in alert.text:
        print("Computador cadastrado com sucesso")
        alert.accept()
except TimeoutException:
    print("Alerta não encontrado ou expirado")


