
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.maximize_window()
        driver.get("https://www.google.com")

        pesquisa = wait.until(
            EC.visibility_of_element_located((By.NAME, "q"))
        )

        pesquisa.send_keys("Selenium Python")
        pesquisa.send_keys(Keys.ENTER)

        wait.until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        print(f"Título: {driver.title}")
        print(f"URL: {driver.current_url}")
        print("Teste executado com sucesso!")

    except Exception as erro:
        print(f"Erro na automação: {erro}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
