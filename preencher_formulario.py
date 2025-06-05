from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get("file:///C:/Users/Raul%20Guilherme/atividade-testes/formulario.html")

time.sleep(0.8)

navegador.find_element(By.ID, "nome").send_keys("Raul Guilherme")
time.sleep(0.8)

navegador.find_element(By.ID, "ra").send_keys("2301151")
time.sleep(0.8)

navegador.find_element(By.ID, "dia").send_keys("10")
time.sleep(0.8)
navegador.find_element(By.ID, "mes").send_keys("06")
time.sleep(0.8)
navegador.find_element(By.ID, "ano").send_keys("2005")
time.sleep(0.8)

navegador.find_element(By.ID, "curso").send_keys("Análise e Desenvolvimento de Sistemas")
time.sleep(0.8)

navegador.find_element(By.ID, "aproveitamento").send_keys("10")
time.sleep(0.8)

navegador.find_element(By.ID, "sugestoes").send_keys("Mais atividades como essa da prova")
time.sleep(0.8)

navegador.find_element(By.ID, "observacoes").send_keys("Gostei muito da matéria, valeu professor!")
time.sleep(0.8)

navegador.find_element(By.TAG_NAME, "button").click()

time.sleep(3)
navegador.quit()
