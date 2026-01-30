import requests
try:
    resposta = requests.get("https://pudim.com.br")
    if resposta.status_code == 200:
        print(f"\033[1;32mSite do pudim está ativo!\033[m")
except requests.exceptions.ConnectionError:
    print(f"\033[1;31mErro! Não consigo acessar o site do pudim por erro de conexão.\033[m")
else:
    print(f'\033[1;32mConexão bem-sucedida!\033[m')