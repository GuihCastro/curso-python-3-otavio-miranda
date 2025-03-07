# type: ignore

# from pathlib import Path
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

# ROOT_FOLDER = Path(__file__).parent
# DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chrome.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    # chrome_service = Service(executable_path=DRIVER_PATH)

    try:
        browser = webdriver.Chrome(
            # service=chrome_service,
            options=chrome_options,
        )
    except Exception as e:
        print('Erro ao criar o navegador! ', e)

    return browser


if __name__ == '__main__':
    WAIT = 10

    try:
        print('Abrindo o navegador...')
        browser = make_chrome_browser()
        browser.get('https://www.bing.com/?cc=br')

        print('Aguardando os elementos...')
        search_reject = WebDriverWait(browser, WAIT).until(
            EC.presence_of_element_located(
                (By.ID, 'bnp_btn_reject')
            )
        )
        search_input = WebDriverWait(browser, WAIT).until(
            EC.presence_of_element_located(
                (By.ID, 'sb_form_q')
            )
        )

        print('Rejeitando cookies...')
        search_reject.send_keys(Keys.ENTER)

        print('Digitando a busca...')
        search_input.send_keys('Mariana Livraes')

        print('Buscando...')
        search_input.send_keys(Keys.ENTER)

        print('Localizando os resultados...')
        results = browser.find_element(By.ID, 'b_results')
        links = results.find_elements(By.TAG_NAME, 'a')

        print('Acessando o primeiro link...')
        links[0].click()

        sleep(WAIT)
        print('Finalizado! Fechando o navegador...')
    except Exception as e:
        print('ERRO! ', e)
