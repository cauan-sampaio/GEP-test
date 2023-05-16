from gep import ComputerRegistration
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait



computer_registration = ComputerRegistration()
computer_registration.open_website('http://localhost:3000/machines')

computer_registration.register_computer('jjhjgj-1221344321+77686656', 'pc 011111',
                                        'Intel i5 4 geração, memória RAM: 8 GB, HD:1TB, placa de vídeo:Integrada', 1)

try:
    # Realizar tratamento
    wait = WebDriverWait(computer_registration.driver, 10)
    wait.until(EC.alert_is_present())
    alert = computer_registration.driver.switch_to.alert
    if "Computador cadastrado com sucesso" in alert.text:
        print("Computador cadastrado com sucesso")
        alert.accept()
except TimeoutException:
    print("Alerta não encontrado ou expirado")

# Iniciar gep2.py em uma thread separada



