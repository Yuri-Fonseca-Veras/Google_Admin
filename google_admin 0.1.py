# ________________________________Instalações Necessárias________________________________#
# 1) Playwright: pip install playwright pytest-playwright
# 2) Playwright navegadores: python -m playwright install
# 3) TQDM: pip install tqdm
# 4) Pytz: pip install json


from playwright.sync_api import sync_playwright
import os
from time import sleep
from tqdm import tqdm
import json

os.system('cls' if os.name == 'nt' else 'clear')
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

google_email = dados["email"]  
google_senha = dados["senha"]  
last_user_google = None
ultima_opcao = None

## Links ##
google_admin = "https://admin.google.com"

    
with sync_playwright() as p:
    # Inicia o navegador
    browser = p.firefox.launch(headless=True)
    # Abre uma nova página
    page = browser.new_page()

# _______ Funções ________#   
    def texto_console(conteudo):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(conteudo)
        sleep(3)

    def up_down(up, down):
        """Move a seta para cima ou para baixo."""
        for _ in range(up):
            page.keyboard.press("ArrowUp")
        for _ in range(down):
            page.keyboard.press("ArrowDown")

    def user(numero_user):
        # Localizar o elemento pelo XPath e obter o valor do input
        locator = page.locator('xpath=/html/body/div[8]/div[2]/header/div[2]/div[2]/div[2]/form/div/div/div/div/div/div[1]/input[2]')
        user_google = locator.input_value()  # Obtém o texto presente no input
        print(f"{numero_user}: {user_google}")

#________________________________________________________________________________________________#    # Insere a URL da página que você deseja acessar
    page.goto(google_admin)
# Defina as etapas do login
    etapas_login = [
        "Iniciando login...",
        "Preenchendo e-mail...",
        "Clicando em próximo...",
        "Preenchendo senha...",
        "Clicando em entrar..."
    ]

# Crie uma barra de progresso
    with tqdm(total=len(etapas_login), desc="Login em Progresso") as barra_progresso:
        # Iniciando login...
        texto_console("Iniciando login...")
        page.wait_for_timeout(5000)
        barra_progresso.update(1)  # Atualize a barra de progresso

        # Preenchendo e-mail...
        page.locator('xpath=//*[@id="identifierId"]').fill(google_email)
        page.wait_for_timeout(5000)
        barra_progresso.update(1)  # Atualize a barra de progresso

        # Clicando em próximo...
        page.click('xpath=//*[@id="identifierNext"]/div/button/span')
        page.wait_for_timeout(5000)
        barra_progresso.update(1)  # Atualize a barra de progresso

        # Preenchendo senha...
        page.locator('xpath=//*[@id="password"]/div[1]/div/div[1]/input').fill(google_senha)
        page.wait_for_timeout(2000)
        barra_progresso.update(1)  # Atualize a barra de progresso

        # Clicando em entrar...
        page.click('xpath=//*[@id="passwordNext"]/div/button/span')
        page.wait_for_timeout(5000)
        barra_progresso.update(1)  # Atualize a barra de progresso

    os.system('cls' if os.name == 'nt' else 'clear')
    buscar_user = input("Por favor, informe o nome do usuário ou e-mail que você deseja buscar: ")
    texto_console("Buscando usuário...")


    ## Buscando usuário ##
    page.wait_for_timeout(5000)
    page.locator('xpath=/html/body/div[8]/div[2]/header/div[2]/div[2]/div[2]/form/div/div/div/div/div/div[1]/input[2]').fill(buscar_user)
    page.wait_for_timeout(9000)

    ## Usuários achados ##
    texto_console('Usuários encontrador: ')
    # Inicializar a variável para rastrear o último valor

    # Verificar interações com base em condições
    up_down(0, 2)
    user("1.")
    up_down(0, 1)
    user("2.")
    up_down(0, 1)
    user("3.")
    up_down(0, 1)
    user("4.")
    up_down(0, 1)
    user("5.")