# 🚀 WhatsApp Mass Dispatcher - (v1.0)

Fiz esse script em Python para automatizar o envio de mensagens personalizadas via WhatsApp Web, utilizando tecnicas de **RPA (Robotic Process Automation)**. O foco principal é a eficiência operacional e a economia de recursos do sistema através da lógica de aba única.

---

## 🛠️ Funcionalidades

* **Sanitização de Dados:** Limpeza automática de números (remove espaços, hifens e valida o DDI +55).
* **Gestão de Memória:** Reaproveita a mesma aba do navegador para todos os envios, evitando travamentos por excesso de processos.
* **Segurança Antispam:** Intervalo configurável entre disparos (padrão 300s) para emular o comportamento humano e proteger o chip contra banimentos é ir aquecendo aos poucos.
* **Tratamento de Caracteres:** Suporte total a emojis e acentuação via codificação de URL.

---

## 📋 Pré-requisitos

Antes de rodar o script, você precisa ter o **Python** instalado e as seguintes bibliotecas:

1.  **Atualizar o Gerenciador de Pacotes:**
    ```bash
    py -m pip install --upgrade pip
    ```

2.  **Instalar Bibliotecas de Controle:**
    ```bash
    py -m pip install pyautogui pyperclip
    ```

---

## 🏗️ Anatomia do Script

### 1. Ferramentas Utilizadas
* `webbrowser`: Interface para abertura do navegador.
* `pyautogui`: Robo de controle de interface gráfica (mouse e teclado).
* `pyperclip`: Gerenciamento da área de transferência para evitar erros de digitação.
* `urllib.parse.quote`: Codificação de mensagens para formato de URL seguro.

### 2. Fluxo de Operação
* **Aquecimento:** O script inicia o WhatsApp Web e aguarda 30 segundos(ou o tempo que você deseja deixar) para a autenticação manual via QR Code.
* **Navegação Inteligente:** Utiliza o atalho `Ctrl + L` para focar na barra de endereços e injetar o link direto do chat com o cliente.
* **Foco e Disparo:** O robô realiza um clique central na tela para garantir o foco da janela ativa antes de pressionar `Enter` tudo isso utilizando o proprio computador.

---

## 🚀 Como Utilizar

1.  **Configuração de Contatos:**
    No arquivo `disparador_mage.py`, insira os números na variável `numeros_brutos` dentro das aspas triplas:
    ```python
    numeros_brutos = """
    61-99999-9999
    61 98888-8888
    """
    ```

2.  **Configuração da Mensagem:**
    Edite a variável `MENSAGEM_PADRAO` com o texto desejado.

3.  **Execução:**
    Abra o terminal na pasta do projeto e execute:
    ```bash
    py disparador_mage.py
    ```

4.  **Atenção:** > **⚠️ IMPORTANTE:** Uma vez iniciado, não utilize o mouse ou teclado. O script emula comandos físicos e qualquer interferência pode desviar o foco do robô, ele irá focar somente em um navegador, caso seja aberto outras abas ele não envia a mensagem é pula a sequencia do número.

---

## 📑 Resumo de Comandos de Automação

| Comando | Função Técnica |
| :--- | :--- |
| `pyautogui.hotkey('ctrl', 'l')` | Ele foca na barra de navegação. |
| `pyperclip.copy(link)` | Copia o link formatado para a memória. |
| `pyautogui.hotkey('ctrl', 'v')` | Cola o link na barra de endereços. |
| `pyautogui.press('enter')` | Confirma o carregamento ou envio. |
| `time.sleep(X)` | Pausa o sistema para aguardar o carregamento do DOM do site para não saturar. |

---

## ✒️ Desenvolvedor
* **Matheus Carvalho** - *Sistemas de Informação*