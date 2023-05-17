from gep import ComputerRegistrationCancel
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import threading
import os
computer_registration_cancel = ComputerRegistrationCancel()
computer_registration_cancel.open_website('http://localhost:3000/machines')

computer_registration_cancel.register_computer('fdghtrd754634653yteu5876980svsa@$#$', '#W#$W', 'SDE##$%%EW',1)
try:
    # Realizar tratamento
    wait = WebDriverWait(computer_registration_cancel.driver, 10)
    wait.until(EC.alert_is_present())
    alert = computer_registration_cancel.driver.switch_to.alert
    if "Computador cadastrado com sucesso" in alert.text:
        print("Computador cadastrado com sucesso")
        alert.accept()
except TimeoutException:
    print("Alerta não encontrado ou expirado")

class Gep5Thread(threading.Thread):
    def run(self):
        os.system("python gep5.py")

gep4_thread = Gep5Thread()
gep4_thread.start()

computer_registration_cancel.driver.quit()
