
import json
import urllib.request
import time


def main():
    url = "https://jsonplaceholder.typicode.com/users/1"

    print("Iniciando teste de requisição HTTP...")
    inicio = time.perf_counter()

    try:
        with urllib.request.urlopen(url, timeout=15) as resposta:
            status = resposta.status
            dados = json.load(resposta)

        duracao = time.perf_counter() - inicio

        print(f"Status HTTP: {status}")
        print(f"Tempo de resposta: {duracao:.2f}s")
        print(f"Nome: {dados['name']}")
        print(f"Email: {dados['email']}")
        print("TESTE CONCLUÍDO COM SUCESSO!")

    except Exception as erro:
        print(f"FALHA NA REQUISIÇÃO: {erro}")
        raise


if __name__ == "__main__":
    main()
