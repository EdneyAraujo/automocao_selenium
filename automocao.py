from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#rom selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

#navegador = webdriver.Chrome(service=servico)

#ABRE O NAVEGADOR
navegador.get("https://sistemas.ufmt.br/ufmt.portalsistemas")

navegador.find_element('xpath', '//*[@id="usuario"]').send_keys("04545103")
navegador.find_element('xpath', '//*[@id="senha"]').send_keys("12212")
navegador.find_element('xpath', '/html/body/main/div[2]/div/form/div/div[3]/button').click()
#navegador.find_element('xpath', '//*[@id="ListTodos"]/div/div[2]/div[1]/div/div[2]/div[7]/span/a').click()
WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ListTodos"]/div/div[2]/div[1]/div/div[2]/div[7]/span/a')))
navegador.find_element(By.XPATH, '//*[@id="ListTodos"]/div/div[2]/div[1]/div/div[2]/div[7]/span/a').click()
#time.sleep(10)

# Encontrar o campo de entrada de texto e preenchê-lo
#navegador = webdriver.Chrome()
#campo_texto = navegador.find_element_by_id('xpath','/html/body/main/div[2]/div/form/div/div[1]/input')
#campo_texto.send_keys('6537421')

#botao_enviar = navegador.find_element_by_id('xpath','//*[@id="usuario"]')
#botao_enviar.click()