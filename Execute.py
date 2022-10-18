#created by Wolf.py 404
#agradecimento especial a Glitch404
azul="\033[36m"
roxo="\033[35m"
branco="\033[00m"
amarelo="\033[32m"

import time
import os
import whois
os.system("clear")
print(azul+"olá! seja bem vindo ao script de consultar dados de um site")
def prog():
    print("\n")
    site=input("digite o site que deseja consultar a seguir: "+roxo)
    dados=whois.whois(site)
    print("\n")
    print("pera la amigao, estamos consultanto.."+amarelo)
    time.sleep(2)
    print("\n")
    print(dados.text)
prog()
while True:
    re= str(input(roxo+"deseja continuar?"+amarelo+"[S/N]))
    re.strip()
    re.upper()
    if re=="S":
        prog()
    elif re=="N":
        break
    else:
        print("desculpe... não entendi..")
print("\n")
print(roxo+"fechando...")
time.sleep(2)
print("\n")
print("Obrigado por vir! volte sempre!"+branco)
