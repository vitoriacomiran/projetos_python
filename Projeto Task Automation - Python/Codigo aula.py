# Passo 1: entrar https://dlp.hashtagtreinamentos.com/python/intensivao/login
# instalar o pyautogui: pip install pyatogui
import pyautogui
import time
# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho de teclado

pyautogui.PAUSE = 0.5 
# não é um comando, é uma configuração padrão para dar tempo do sistema ler

# vai dar uma pausa de meio segundo em cada comando

# abrir o navegador
# apertar a tecla win
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(2)

# Passo 2: fazer login
# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# dar uma pausa específica
time.sleep(3)
# na página auxiliar foi verificada a posição do mouse para colocar as coordenadas
pyautogui.click(x=779, y=389)
pyautogui.write("vitoriacmn@gmail.com")
pyautogui.press("tab")
pyautogui.write("0000")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: importar a base de dados
# pip install pandas
import pandas

# criar uma variável tabela, para ler uma base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: cadastrar 1 produto
time.sleep(3)
pyautogui.click(x=765, y=277)

# faz a localização do item na tabela, para a base de dados pandas, usa []
# texto = string str()
# para cada linha da tabela ele deve executar todos os comandos novamente

linha = 0 
for linha in tabela.index:
    #selecionar o primeiro campo
    pyautogui.click(x=765, y=277)
    
    #código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    #isna comando que verifica se o valor é vazio
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Passo 5: repetir o processo de cadastro até acabar os produtos
    #voltar ao inicio da tela para recomeçar

    pyautogui.scroll(5000)
