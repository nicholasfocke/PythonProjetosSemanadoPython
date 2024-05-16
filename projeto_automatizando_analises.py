import yfinance
import pyautogui
import pyperclip

ticker = input("Digite o código do Fundo desejado: ")
dados = yfinance.Ticker(ticker)
tabela = dados.history("2mo")


fechamento = tabela.Close
print(fechamento)

maximo = fechamento.max()
minimo = fechamento.min()
atual = fechamento.iloc[-1] # ou fechamento[-1]

print(maximo)
print(minimo)
print(atual)

destinatario = "digiteemailaqui@gmail.com"
assunto = "Analise Fundos imobiliários" 
mensagem = f"""
Boa noite,

Segue abaixo as análises do Fundo {ticker} dos ultimos 2 meses:

Cotação Máxima: R${round(maximo,2)}
Cotação Mínima: R${round(minimo,2)}
Cotação Atual: R${round(atual,2)}

Atenciosamente,
Nicholas.
"""

pyautogui.PAUSE = 3

pyautogui.click(x=1147, y=1055)

pyperclip.copy("https://mail.google.com/mail/u/1/#inbox")

pyautogui.hotkey("ctrl", "t")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

pyautogui.click(x=146, y=195)

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.press("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
#pyautogui.click(x=1297, y=999) #botao de enviar do gmail