import telebot
from datetime import datetime

chave_api="6291101075:AAE9jixwLVZeJrf2YNmmI_bInIlL6qbZSFs"

bot=telebot.TeleBot(chave_api)

Hora=datetime.now().hour

if Hora < 12:
    mens_boa="Boa dia !!"
elif Hora <= 18:
    mens_boa="Bom Tarde!!"
elif Hora > 18:
    mens_boa="Boa noite !!"


#opções de ecolhas do bot
@bot.message_handler(commands=["1"])
def opcao1 (mensagem):
    bot.reply_to(mensagem,"Curiosidade sobre iot tal")
@bot.message_handler(commands=["2"])
def opcao2 (mensagem):
    bot.reply_to(mensagem,"iot resumo tal")
@bot.message_handler(commands=["3"])
def opcao3 (mensagem):
    bot.reply_to(mensagem,"o inicio de tudo e tal")
@bot.message_handler(commands=["4"])
def opcao4 (mensagem):
    bot.reply_to(mensagem,"Noticias fresquinha e tal")
@bot.message_handler(commands=["start"])
def ammor (mensagem):
    nome=mensagem.chat.first_name

    bot.send_message(mensagem.chat.id,f"""{mens_boa} Tudo bom com você {nome} ? 
Eu sou um Robô que vai te ensinar de forma resumida sobre o que é IOT 
        Bom, o que voce gostaria de saber? 
                /1 - Curisidade sobre Iot
                /2 - Um resumo sobre o assunto Iot
                /3 - Noticias que acabaram de sair sobre Iot 
    """)


#Boas vindas
def verificar (mensagem): 
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    nome=mensagem.chat.first_name
    bot.reply_to(mensagem,f"""Desculpe {nome} eu não entendi, escolha uma das opções abaixo !
                /1 - Curisidade sobre Iot
                /2 - Um resumo sobre o assunto Iot
                /3 - Noticias que acabaram de sair sobre Iot
    """)
    amor(mensagem)
                 


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



bot.polling()