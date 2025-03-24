# Instalações Necessárias
# 1) Playwright: pip install playwright pytest-playwright
# 2) Playwright navegadores: python -m playwright install
# 3) TQDM: pip install tqdm

from playwright.sync_api import sync_playwright
import os
from time import sleep
from tqdm import tqdm
import json

# Limpa a tela
os.system('cls' if os.name == 'nt' else 'clear')

# Mensagem de boas-vindas
print("""
───▐▀▄─────────▄▀▌
───▐▓░▀▄▀▀▀▀▀▄▀░▓▌
───▐░▓░▄▀░░░▀▄░▓░▌
────█░░▌█▐░▌█▐░░█
─▄▄▄▐▀░░░▀█▀░░░▀▌▄▄▄
█▐▐▐▌▀▄░▀▄▀▄▀░▄▀▐▌▌▌█
▀▀▀▀▀▀▀▀▀▄▄▄▀▀▀▀▀▀▀▀▀
BEM-VINDO AO RESET 
SENHA DE E-MAIL!
""")

## Configurações de Login ##
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)

# Variáveis de login
google_email = dados["email"]
google_senha = dados["senha"]
nova_senha_01 = dados["reset_senha_01"]
nova_senha_02 = dados["reset_senha_02"]
last_user_google = None
ultima_opcao = None

## Links ##
google_admin = "https://admin.google.com"

# Inicia o navegador
with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto(google_admin)
    # Funções auxiliares
    def texto_console(conteudo):
        """Limpa a tela e exibe uma mensagem."""
        os.system('cls' if os.name == 'nt' else 'clear')
        print(conteudo)
        sleep(3)

    def up_down(up, down, velocidade=200):
        """Move a seta para cima ou para baixo."""
        for _ in range(up):
            page.keyboard.press("ArrowUp")
            page.wait_for_timeout(velocidade)
        for _ in range(down):
            page.keyboard.press("ArrowDown")
            page.wait_for_timeout(velocidade)

    def user():
        """Obtém o valor do input do usuário."""
        locator = page.locator('xpath=/html/body/div[8]/div[2]/header/div[2]/div[2]/div[2]/form/div/div/div/div/div/div[1]/input[2]')
        user_google = locator.input_value()
        return user_google

    # Acessa a página do Google Admin

    # Etapas do login
    etapas_login = [
        "Iniciando login...",
        "Preenchendo e-mail...",
        "Clicando em próximo...",
        "Preenchendo senha...",
        "Clicando em entrar...",
    ]

    # Barra de progresso para o login
    with tqdm(total=len(etapas_login), desc="Login em Progresso") as barra_progresso:
        # Iniciando login...
        texto_console("Iniciando login...")
        page.wait_for_timeout(5000)
        barra_progresso.update(1)

        # Preenchendo e-mail...
        page.locator('xpath=//*[@id="identifierId"]').fill(google_email)
        page.wait_for_timeout(5000)
        barra_progresso.update(1)

        # Clicando em próximo...
        page.click('xpath=//*[@id="identifierNext"]/div/button/span')
        page.wait_for_timeout(5000)
        barra_progresso.update(1)

        # Preenchendo senha...
        page.locator('xpath=//*[@id="password"]/div[1]/div/div[1]/input').fill(google_senha)
        page.wait_for_timeout(2000)
        barra_progresso.update(1)

        # Clicando em entrar...
        page.click('xpath=//*[@id="passwordNext"]/div/button/span')
        page.wait_for_timeout(5000)
        barra_progresso.update(1)

    # Limpa a tela e solicita o nome do usuário
    os.system('cls' if os.name == 'nt' else 'clear')
    buscar_user = input("Por favor, informe o nome do usuário ou e-mail que você deseja buscar: ")
    texto_console("Buscando usuário...")

    # Busca o usuário
    page.wait_for_timeout(5000)
    page.locator('xpath=/html/body/div[8]/div[2]/header/div[2]/div[2]/div[2]/form/div/div/div/div/div/div[1]/input[2]').fill(buscar_user)
    page.wait_for_timeout(8000)

    # Exibe usuários encontrados
    texto_console('Usuários encontrados: ')

    # Variáveis para rastrear a busca
    numero_para_busca = 1
    numero_para_user = 1
    rodada = 8

    up_down(0, 1, 200)
    for i in range(9):
        up_down(0, numero_para_busca)

        if user() == buscar_user:
            up_down(0, rodada)
            break

        print(f'{numero_para_user}: {user()}')

        numero_para_user += 1
        rodada -= 1

    up_down(9, 0, 150)

    # Solicita a escolha do usuário
    escolha_user = input("Escolha uma opção: ")
    texto_console("Resetando senha...")
    escolha_user_feita = int(escolha_user)
    numero_para_user = 1
    page.wait_for_timeout(2000)

    # Seleciona o usuário escolhido
    for i in range(escolha_user_feita):
        up_down(0, 1)
    page.keyboard.press('Enter')

    # Tenta resetar a senha
    try:
        page.wait_for_timeout(5000)
        page.locator("xpath=/html/body/div[8]/c-wiz/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/span/c-wiz/div/div[3]/span/div/div/div[1]/div/span/span/div/div[2]").dblclick()
        page.wait_for_timeout(5000)
        page.click('xpath=//*[@id="c79"]')
    except:
        print("Senha não pode ser resetada!")
        browser.close()

    # Função para colocar a nova senha
    def colocando_senha():
        page.keyboard.press('Enter')
        page.wait_for_timeout(3000)
        page.locator('xpath=//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/div[2]/div[2]/span').click()
        page.wait_for_timeout(3000)
        page.click('xpath=//*[@id="SecurityTab"]/span[2]')
        page.wait_for_timeout(3000)
        texto_console("Tirando desafio de login")
        page.click('xpath=//*[@id="yDmH0d"]/c-wiz/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div/span/div/div/div[3]/span/div/div/div/div[2]/div/div[1]/div[2]/div[7]/div[1]/div/div[1]/header')
        page.wait_for_timeout(3000)
        page.click('xpath=//*[@id="yDmH0d"]/c-wiz/div/div[1]/div/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div/div/span/div/div/div[3]/span/div/div/div/div[2]/div/div[1]/div[2]/div[7]/div[1]/div/div[2]/div/div/div[1]/div/div[2]')

    # Tenta colocar a nova senha
    try:
        page.locator('xpath=//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/span/c-wiz/c-wiz/div[2]/div/div/div[1]/div/div[1]/input').fill(nova_senha_01)
        print(f"Tentando senha {nova_senha_01}")
        colocando_senha()
    except:
        page.locator('xpath=//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/span/c-wiz/c-wiz/div[2]/div/div/div[1]/div/div[1]/input').fill(nova_senha_02)
        print(f"Tentando senha {nova_senha_02}")
        colocando_senha()

    # Mensagem de sucesso
    texto_console("Senha resetada!!!")
    browser.close()
