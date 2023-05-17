from gep import ComputerRegistration
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import threading
import os
computer_registration = ComputerRegistration()
computer_registration.open_website('http://localhost:3000/machines')

computer_registration.register_computer('fdghtrd754634653yteu5876980svsa@$#$', '#W#$W', 'SDE##$%%EW', 1 )
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
class Gep4Thread(threading.Thread):
    def run(self):
        os.system("python gep4.py")

gep4_thread = Gep4Thread()
gep4_thread.start()

computer_registration.driver.quit()
