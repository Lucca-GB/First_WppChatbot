#importamos as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#navegamos até o wpp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10)

#definimos os contatos ou grupos e msgs a ser enviada
contatos = ['G1', 'G2', 'G3']
mensagem = '1' 
mensagem2 = '\n 2'
mensagem3 = '\n 3'
mensagem4 = '\n 4'
mensagem5 = '\n 5'
mensagem6 = '\n 6'
mensagem7 = '\n 7'
mensagem8 = '\n 8'
mensagem9 = '\n 9'
mensagem10 = '\n 10'

#buscamos contatos/grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#enviamos mensagens para o contato/grupo

def enviar_mensagem(mensagem, mensagem2, mensagem3, mensagem4, mensagem5, mensagem6, mensagem7, mensagem8, mensagem9, mensagem10):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    campo_mensagem[1].send_keys(mensagem, mensagem2, mensagem3, mensagem4, mensagem5, mensagem6, mensagem7, mensagem8, mensagem9, mensagem10)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem, mensagem2, mensagem3, mensagem4, mensagem5, mensagem6, mensagem7, mensagem8, mensagem9, mensagem10)
    
#campo de pesquisa 'copyable-text selectable-text'
#campo de msg privada 'copyable-text selectable-text'
