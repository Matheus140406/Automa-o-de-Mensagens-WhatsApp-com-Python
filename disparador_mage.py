import webbrowser
import pyautogui
import time
import sys
import pyperclip
from urllib.parse import quote

#Coloque o número que você vai usar para enviar as mensagen
NUMERO_ORIGEM = "+556195707957" 

#Coloque os números do clientes que você quer enviar as mensagens, um por linha, no formato:
# Coloque do jeito que está na tabela
numeros_brutos = """

"""
#Coloque sua mensagem dentro do paranteses
MENSAGEM_PADRAO = """ """

def limpar_e_formatar(texto_bruto):
    linhas = texto_bruto.strip().split('\n')
    lista_limpa = []
    for n in linhas:
        limpo = n.replace("-", "").replace(" ", "").strip()
        if not limpo.startswith("+"):
            limpo = "+55" + limpo if not limpo.startswith("55") else "+" + limpo
        lista_limpa.append(limpo)
    return lista_limpa

def executar_automacao():
    destinatarios = limpar_e_formatar(numeros_brutos)
    total = len(destinatarios)
    
    print(f"==========================================")
    print(f"CANAL MAGE SISTEMAS: {NUMERO_ORIGEM}")
    print(f"MODO: Aba Única (Economia de Memória)")
    print(f"==========================================\n")

    webbrowser.open("https://web.whatsapp.com")
    print("Aguardando 30 segundos para o carregamento inicial...")
    time.sleep(30)

    for indice, cliente in enumerate(destinatarios, 1):
        try:
            print(f"[{indice}/{total}] Processando: {cliente}...")
            
            msg_codificada = quote(MENSAGEM_PADRAO)
            link_whatsapp = f"https://web.whatsapp.com/send?phone={cliente}&text={msg_codificada}"
            
            pyautogui.hotkey('ctrl', 'l') 
            time.sleep(1)
            
            pyperclip.copy(link_whatsapp)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            
            time.sleep(15) 
            
            largura, altura = pyautogui.size()
            pyautogui.click(largura / 2, altura / 2)
            time.sleep(2)
            
            pyautogui.press('enter')
            print(f"✅ Mensagem enviada para {cliente}")

            if indice < total:
                print(f"⏳ Intervalo de 300s antes do próximo contato...")
                time.sleep(300)

        except Exception as e:
            print(f"❌ Erro em {cliente}: {e}")
            continue

if __name__ == "__main__":
    executar_automacao()  