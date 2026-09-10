import sys
import time

from DrissionPage import Chromium, ChromiumOptions


def executar() -> int:
    browser = None

    try:
        print("Configurando navegador...", flush=True)

        opcoes = ChromiumOptions(read_file=False)
        opcoes.auto_port()
        opcoes.set_argument("--start-maximized")

        # Use somente se o DrissionPage não localizar o Chrome:
        # opcoes.set_browser_path(
        #     r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        # )

        print("Iniciando Google Chrome...", flush=True)
        browser = Chromium(opcoes)
        pagina = browser.latest_tab

        print("Acessando o Google...", flush=True)
        pagina.get("https://www.google.com")

        print("Localizando campo de pesquisa...", flush=True)
        campo_pesquisa = pagina.ele("@name=q", timeout=20)

        if not campo_pesquisa:
            raise RuntimeError("Campo de pesquisa não encontrado.")

        print("Pesquisando por capivara...", flush=True)
        campo_pesquisa.input("capivara\n")

        print("Aguardando resultados...", flush=True)
        resultado = pagina.ele("#search", timeout=20)

        if not resultado:
            raise RuntimeError("Resultados da pesquisa não foram carregados.")

        print("Pesquisa concluída com sucesso.", flush=True)

        time.sleep(5)
        return 0

    except Exception as erro:
        print(f"Falha durante a automação: {erro}", flush=True)
        return 1

    finally:
        if browser is not None:
            print("Fechando navegador...", flush=True)
            browser.quit()


if __name__ == "__main__":
    sys.exit(executar())
