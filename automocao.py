from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get("https://sistemas.ufmt.br/ufmt.portalsistemas")

# Encontrar o campo de entrada de texto e preenchê-lo
#navegador = webdriver.Chrome()
#campo_texto = navegador.find_element_by_id("//*[@id="usuario"]")
#campo_texto.send_keys("6537421")

botao_enviar = navegador.find_element_by_id('xpath','/html/body/main/div[2]/div/form/div/div[3]/button')
botao_enviar.click()