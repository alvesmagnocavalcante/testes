import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def executar() -> int:
    print("Iniciando Google Chrome...", flush=True)

    driver = webdriver.Chrome()

    try:
        print("Acessando o Google...", flush=True)
        driver.get("https://www.google.com")

        print("Procurando campo de pesquisa...", flush=True)
        search_box = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )

        print("Pesquisando por capivara...", flush=True)
        search_box.send_keys("capivara" + Keys.ENTER)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        print("Pesquisa concluída.", flush=True)

        time.sleep(5)

        driver.save_screenshot("resultado_capivara.png")
        print("Captura de tela salva.", flush=True)

        return 0

    except Exception:
        print("Erro durante a automação.", flush=True)
        driver.save_screenshot("erro_selenium.png")
        raise

    finally:
        print("Fechando navegador...", flush=True)
        driver.quit()


if __name__ == "__main__":
    try:
        sys.exit(executar())
    except Exception as erro:
        print(f"Falha: {erro}", flush=True)
        sys.exit(1)