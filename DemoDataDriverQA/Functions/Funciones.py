from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class funcionesGlobales:
    def __init__(self, driver):
        self.driver = driver

    def navegar(self, url):
        try:
            self.driver.get(url)
            print("Ingreso a URL exitoso")
        except TimeoutException as ex:
            print(f"Timeout al navegar a la URL: {ex.msg}")
            return False
        except Exception as ex:
            print(f"Error al navegar a la URL: {str(ex)}")
            return False

    def globalInput(self, selector,texto):
        try:
            input_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
            if input_element.is_enabled():
                print("Escribiendo en el campo {} el texto -> {} ".format(selector,texto))
                return input_element  # Devuelve el elemento WebElement
            else:
                print("Este elemento NO está presente")
                return None
        except TimeoutException as ex:
            print(f"Timeout al esperar elemento: {ex.msg}")
            return None
        except Exception as ex:
            print(f"Error al obtener el elemento: {str(ex)}")
            return None

    def clicInput(self, selector):
        try:
            input_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
            input_element.click()
            print("Clic realizado en el elemento")
        except TimeoutException as ex:
            print(f"Timeout al esperar elemento: {ex.msg}")
            return None
        except Exception as ex:
            print(f"Error al hacer clic en el elemento: {str(ex)}")
            return None

    def Existe(self, selector):
        try:
            input_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", input_element)
            print(f"El elemento {selector} -> existe")
            return "Existe"
        except TimeoutException as ex:
            print(f"Timeout al esperar elemento: {ex.msg}")
            return "No Existe"
        except Exception as ex:
            print(f"Error al verificar la existencia del elemento: {str(ex)}")
            return "No Existe"



