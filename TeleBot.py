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
    bot.reply_to(mensagem,"""The Internet of Things (IoT) refers to the interconnected network of physical devices, vehicles, appliances, and other objects that are embedded with sensors, software, and network connectivity, allowing them to collect and exchange data. These devices can be controlled and monitored remotely, enabling them to interact with their environment and with each other in new and innovative ways.
The IoT has the potential to revolutionize many areas of our lives, from healthcare and transportation to home automation and industrial manufacturing. By connecting objects and devices to the internet, we can create new applications and services that improve efficiency, increase safety, and enhance the overall quality of life for individuals and communities.
Some examples of IoT devices include smart thermostats, fitness trackers, security systems, smart home appliances, and industrial sensors. As the technology continues to develop, we can expect to see even more innovative uses of the IoT in the future.
""")
@bot.message_handler(commands=["2"])
def opcao2 (mensagem):
    bot.reply_to(mensagem,"""Improved efficiency and productivity: IoT devices can help automate tasks and reduce the need for human intervention, leading to increased efficiency and productivity.
Cost savings: IoT devices can help reduce costs by optimizing resource utilization, reducing waste, and minimizing downtime.
Enhanced safety and security: IoT devices can be used to monitor and control potentially hazardous situations, improving safety and security in a variety of environments.
Improved customer experiences: IoT devices can be used to provide personalized and context-aware services to customers, enhancing their overall experience.
Better decision making: IoT devices can generate vast amounts of data that can be analyzed to provide insights and inform decision-making.
Environmental benefits: IoT devices can be used to monitor and optimize energy consumption, reducing carbon emissions and helping to mitigate climate change.
Healthcare benefits: IoT devices can be used to monitor patients and provide personalized care, leading to improved health outcomes.
""")
@bot.message_handler(commands=["3"])
def opcao3 (mensagem):
    bot.reply_to(mensagem,"""Security risks: IoT devices can be vulnerable to cyberattacks, which can compromise personal data, networks, and even physical safety.
Privacy concerns: IoT devices can collect a lot of data about users, leading to privacy concerns if this data is not properly secured or managed.
Interoperability issues: IoT devices may not be able to communicate with each other if they use different protocols or standards, leading to interoperability issues that can limit their usefulness.
Complexity: IoT systems can be complex to design, deploy, and manage, requiring specialized skills and expertise.
Reliability: IoT devices may be subject to hardware or software failures, leading to downtime and disruptions.
Cost: IoT devices can be expensive, especially for large-scale deployments, which can limit their adoption in some contexts.
Ethical considerations: The widespread adoption of IoT devices raises ethical questions about their impact on society, such as the potential for job displacement or increased surveillance.
""")
@bot.message_handler(commands=["4"])
def opcao4 (mensagem):
    bot.reply_to(mensagem,"""Smart homes: IoT devices such as smart thermostats, smart lighting systems, and smart locks can be used to automate and control various aspects of a home, including temperature, lighting, security, and entertainment.
Healthcare: IoT devices such as wearables, smart medical devices, and remote monitoring systems can be used to monitor patients' health and provide personalized care, improving patient outcomes and reducing healthcare costs.
Industrial automation: IoT sensors and devices can be used to monitor and optimize industrial processes, improving efficiency, reducing downtime, and increasing safety.
Agriculture: IoT sensors can be used to monitor soil moisture, weather conditions, and crop health, enabling precision agriculture and optimizing yields.
Smart cities: IoT devices can be used to monitor and manage various aspects of city infrastructure, including traffic, lighting, waste management, and public safety.
Retail: IoT devices can be used to provide personalized shopping experiences and optimize supply chain management, improving customer satisfaction and reducing costs.
Transportation: IoT sensors can be used to monitor traffic and optimize transportation systems, improving safety and reducing congestion.
Energy management: IoT devices can be used to monitor and optimize energy consumption in buildings and homes, reducing costs and improving sustainability
""")
@bot.message_handler(commands=["start"])
def ammor (mensagem):
    nome=mensagem.chat.first_name

    bot.send_message(mensagem.chat.id,f"""{mens_boa} Tudo bom com você {nome} ? 
Eu sou um Robô que vai te ensinar de forma resumida sobre o que é IOT 
        Bom, o que voce gostaria de saber? 
                /1 - What is the internet of things?
                /2 - Advantages of using Internet of Things (IoT) devices
                /3 - Disadvantages of using Internet of Things (IoT) devices
                /4 - Practical examples of IoT
    """)


#Boas vindas
def verificar (mensagem): 
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    nome=mensagem.chat.first_name
    bot.reply_to(mensagem,f"""Desculpe {nome} eu não entendi, escolha uma das opções abaixo !
                /1 - What is the internet of things?
                /2 - Advantages of using Internet of Things (IoT) devices
                /3 - Disadvantages of using Internet of Things (IoT) devices
                /4 - Practical examples of IoT
    """)
                 




bot.polling()