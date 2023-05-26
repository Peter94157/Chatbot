import os
import PySimpleGUI as sg

#BOT EM SI
def start():
    #boas Vindas
    print("Olá, tudo bom ? Eu sou um Robô que vai ter ensinar de forma resumida sobre o que é IOT")
    #Roubando dados kkkk
    Nome=input("Qual o seu nome ?")
    Email=input("Qual o seu endereço de e-mail")
    while True:
        #Repostas 
        resposta=input(f"{os.linesep}{os.linesep} Bom {Nome}, o que voce gostaria de saber?{os.linesep}"
                    f" [1] - Sobre Iot curisosidade, {os.linesep} [2] - Iot resumo,{os.linesep} [3] - Iot inicio,"
                    f"{os.linesep} [4] - noticias atuais {os.linesep}{os.linesep}")
        Processando(Nome,resposta)


#PROCESSAR AS INFORMAÇÕES
def Processando(Nome,resposta):
    if resposta== '1':
        print(f"Bem {Nome}, Curiosidade sobre iot tal{os.linesep}")
    elif resposta== '2':
        print(f"Então {Nome}, iot resumo tal{os.linesep}")
    elif resposta== '3':
        print(f"{Nome} o inicio de tudo e tal{os.linesep}")
    elif resposta== '4':
        print(f"{Nome} Noticias fresquinha e tal{os.linesep}")
    else:
        print(f"{Nome}, por favor Escolha apenas as opções ja mencionadas acima!!{os.linesep}")
    


#TeleBot 


@bot.message_handler(responder)
def amor (mensagem,msg): 
    msg=mensagem.text
    if msg.lower()=="giulia" or msg.lower()=="giulia" or msg.lower()=="giu":
        bot.reply_to(mensagem,"OII amor da minha vida")
        part2(mensagem,msg)
        return True
    else:
        part2(mensagem,msg)

         

def part2 (mensagem,msg):
    txt="""Eu sou um Robô que vai te ensinar de forma resumida sobre o que é IOT 
        Bom, o que voce gostaria de saber? (Clique em alguma das opções)
                    /1 - Sobre Iot curisosidade,
                    /2 - Iot resumo, 
                    /3 - Iot inicio,
                    /4 - noticias atuais"""
    bot.send_message(mensagem.chat.id,txt)
    return True


start()
