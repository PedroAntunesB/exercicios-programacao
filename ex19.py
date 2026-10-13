import requests

cep = input("Digite o CEP (somente números): ").strip()

if not cep.isdigit() or len(cep) != 8:
    print("CEP inválido. Digite exatamente 8 números.")
else:
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)

        if resposta.status_code == 200:
            dados = resposta.json()

            if "erro" in dados:
                print("CEP não encontrado.")
            else:
                print("\n--- Endereço encontrado ---")
                print("CEP:", dados["cep"])
                print("Logradouro:", dados["logradouro"])
                print("Bairro:", dados["bairro"])
                print("Cidade:", dados["localidade"])
                print("Estado:", dados["uf"])
        else:
            print("Erro na requisição:", resposta.status_code)

    except requests.RequestException as erro:
        print("Não foi possível consultar a API:", erro)

'''

Qual URL foi utilizada? https://viacep.com.br/ws/{cep}/json/, substituindo {cep} pelo CEP informado.

Qual método HTTP foi utilizado? GET.

Qual código HTTP representa sucesso? 200 OK.

Em qual formato os dados foram recebidos? JSON.

Qual é a diferença entre requisição e resposta HTTP? A requisição é a mensagem enviada pelo cliente ao servidor; a resposta é a mensagem que o servidor devolve.
'''