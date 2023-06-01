import telebot
from datetime import datetime

chave_api="6291101075:AAE9jixwLVZeJrf2YNmmI_bInIlL6qbZSFs"

bot=telebot.TeleBot(chave_api)

Hora=datetime.now().hour

if Hora < 12:
    mens_boa="Bom dia !!"
elif Hora <= 18:
    mens_boa="Bom Tarde!!"
elif Hora > 18:
    mens_boa="Boa noite !!"


@bot.message_handler(commands=["start"]or["menu"])
def init (mensagem):
    nome=mensagem.chat.first_name

    bot.send_message(mensagem.chat.id,f"""{mens_boa} {nome} Escolha um idioma...(Choose Language....)
/Ingles
/Portugues
    """)

#Repostas em ingles do Bot
    
@bot.message_handler(func=lambda menssage: "/Ingles" in menssage.text)
def language (mensagem):
    nome=mensagem.chat.first_name    
    bot.reply_to(mensagem,f"""Everything good with you {nome}?
I am a Robot that will teach you in a nutshell what IOT is
Well, what would you like to know?
/Option_1 - What is the internet of things?
/Option_2 - Advantages of using Internet of Things (IoT) devices
/Option_3 - Disadvantages of using Internet of Things (IoT) devices
/Option_4 - Practical examples of IoT
/Who are your creators ? 
    """)

    @bot.message_handler(func=lambda menssage: "/Option_1" in menssage.text)
    def option1 (mensagem):
        bot.reply_to(mensagem,"""The Internet of Things (IoT) refers to the interconnected network of physical devices, vehicles, appliances, and other objects that are embedded with sensors, software, and network connectivity, allowing them to collect and exchange data. These devices can be controlled and monitored remotely, enabling them to interact with their environment and with each other in new and innovative ways.
The IoT has the potential to revolutionize many areas of our lives, from healthcare and transportation to home automation and industrial manufacturing. By connecting objects and devices to the internet, we can create new applications and services that improve efficiency, increase safety, and enhance the overall quality of life for individuals and communities.
Some examples of IoT devices include smart thermostats, fitness trackers, security systems, smart home appliances, and industrial sensors. As the technology continues to develop, we can expect to see even more innovative uses of the IoT in the future.
    """)
        
    @bot.message_handler(func=lambda menssage: "/Option_2" in menssage.text)
    def option2 (mensagem):
        bot.reply_to(mensagem,"""Improved efficiency and productivity: IoT devices can help automate tasks and reduce the need for human intervention, leading to increased efficiency and productivity.
Cost savings: IoT devices can help reduce costs by optimizing resource utilization, reducing waste, and minimizing downtime.
Enhanced safety and security: IoT devices can be used to monitor and control potentially hazardous situations, improving safety and security in a variety of environments.
Improved customer experiences: IoT devices can be used to provide personalized and context-aware services to customers, enhancing their overall experience.
Better decision making: IoT devices can generate vast amounts of data that can be analyzed to provide insights and inform decision-making.
Environmental benefits: IoT devices can be used to monitor and optimize energy consumption, reducing carbon emissions and helping to mitigate climate change.
Healthcare benefits: IoT devices can be used to monitor patients and provide personalized care, leading to improved health outcomes.
    """)
        
    @bot.message_handler(func=lambda menssage: "/Option_3" in menssage.text)
    def option3 (mensagem):
        bot.reply_to(mensagem,"""Security risks: IoT devices can be vulnerable to cyberattacks, which can compromise personal data, networks, and even physical safety.
Privacy concerns: IoT devices can collect a lot of data about users, leading to privacy concerns if this data is not properly secured or managed.
Interoperability issues: IoT devices may not be able to communicate with each other if they use different protocols or standards, leading to interoperability issues that can limit their usefulness.
Complexity: IoT systems can be complex to design, deploy, and manage, requiring specialized skills and expertise.
Reliability: IoT devices may be subject to hardware or software failures, leading to downtime and disruptions.
Cost: IoT devices can be expensive, especially for large-scale deployments, which can limit their adoption in some contexts.
Ethical considerations: The widespread adoption of IoT devices raises ethical questions about their impact on society, such as the potential for job displacement or increased surveillance.
    """)
        
    @bot.message_handler(func=lambda menssage: "/Option_4" in menssage.text)
    def option4 (mensagem):
        bot.reply_to(mensagem,"""Smart homes: IoT devices such as smart thermostats, smart lighting systems, and smart locks can be used to automate and control various aspects of a home, including temperature, lighting, security, and entertainment.
    Healthcare: IoT devices such as wearables, smart medical devices, and remote monitoring systems can be used to monitor patients' health and provide personalized care, improving patient outcomes and reducing healthcare costs.
    Industrial automation: IoT sensors and devices can be used to monitor and optimize industrial processes, improving efficiency, reducing downtime, and increasing safety.
    Agriculture: IoT sensors can be used to monitor soil moisture, weather conditions, and crop health, enabling precision agriculture and optimizing yields.
    Smart cities: IoT devices can be used to monitor and manage various aspects of city infrastructure, including traffic, lighting, waste management, and public safety.
    Retail: IoT devices can be used to provide personalized shopping experiences and optimize supply chain management, improving customer satisfaction and reducing costs.
    Transportation: IoT sensors can be used to monitor traffic and optimize transportation systems, improving safety and reducing congestion.
    Energy management: IoT devices can be used to monitor and optimize energy consumption in buildings and homes, reducing costs and improving sustainability
    """)
    @bot.message_handler(func=lambda menssage: "/Who" in menssage.text)
    def option4 (mensagem):
        bot.reply_to(mensagem,"""My creators the students:
Antonio 
João
Pedro
Yan
    """)
        
        
    
    @bot.message_handler(func=verificar)
    def reply(mensagem):
        nome=mensagem.chat.first_name
        bot.reply_to(mensagem,f"""{nome} i am sorry, i did not understand, Choose one option below !
/Option_1 - What is the internet of things?
/Option_2 - Advantages of using Internet of Things (IoT) devices
/Option_3 - Disadvantages of using Internet of Things (IoT) devices
/Option_4 - Practical examples of IoT
""")

    return

#Repostas em Portugues do Bot

@bot.message_handler(func=lambda menssage: "/Portugues" in menssage.text)
def idioma (mensagem):
    nome=mensagem.chat.first_name    
    bot.reply_to(mensagem,f"""Tudo bom com você {nome} ? 
Eu sou um Robô que vai te ensinar de forma resumida sobre o que é IOT 
Bom, o que voce gostaria de saber?                 
/Opcao_1 - O que é a Internet das coisas ?
/Opcao_2 - Vantagens de usar a dispositivos inteligentes(Iot).
/Opcao_3 - Desvantagens de usar dispositivos inteligentes (Iot).
/Opcao_4 - Exemplos praticos de Iot.
/Quem são seus criadores ? 
    """)
    
    @bot.message_handler(func=lambda menssage: "/Opcao_1" in menssage.text)
    def opcao1 (mensagem):
        bot.reply_to(mensagem,"""A Internet das Coisas (IoT) refere-se à rede interconectada de dispositivos físicos, veículos, aparelhos e outros objetos que são incorporados com sensores, software e conectividade de rede, permitindo que eles coletem e troquem dados.
Esses dispositivos podem ser controlados e monitorados remotamente, permitindo que interajam com seu ambiente e entre si de maneiras novas e inovadoras.
A IoT tem o potencial de revolucionar muitas áreas de nossas vidas, desde saúde e transporte até automação residencial e manufatura industrial. Ao conectar objetos e dispositivos à internet, podemos criar novos aplicativos e serviços que melhoram a eficiência, aumentam a segurança e melhoram a qualidade de vida geral de indivíduos e comunidades.
Alguns exemplos de dispositivos IoT incluem termostatos inteligentes, rastreadores de condicionamento físico, sistemas de segurança, eletrodomésticos inteligentes e sensores industriais. À medida que a tecnologia continua a se desenvolver, podemos esperar ver usos ainda mais inovadores da IoT no futuro.
    """)
        
    @bot.message_handler(func=lambda menssage: "/Opcao_2" in menssage.text)
    def opcao2 (mensagem):
        bot.reply_to(mensagem,"""Eficiência e produtividade aprimoradas: os dispositivos IoT podem ajudar a automatizar tarefas e reduzir a necessidade de intervenção humana, levando a maior eficiência e produtividade.
Economia de custos: os dispositivos IoT podem ajudar a reduzir custos otimizando a utilização de recursos, reduzindo o desperdício e minimizando o tempo de inatividade.
Segurança e proteção aprimoradas: os dispositivos IoT podem ser usados para monitorar e controlar situações potencialmente perigosas, melhorando a segurança em diversos ambientes.
Experiências aprimoradas do cliente: os dispositivos IoT podem ser usados para fornecer serviços personalizados e com reconhecimento de contexto aos clientes, aprimorando sua experiência geral.
Melhor tomada de decisão: os dispositivos IoT podem gerar grandes quantidades de dados que podem ser analisados para fornecer insights e informar a tomada de decisões.
Benefícios ambientais: os dispositivos IoT podem ser usados para monitorar e otimizar o consumo de energia, reduzindo as emissões de carbono e ajudando a mitigar as mudanças climáticas.
Benefícios para a saúde: os dispositivos IoT podem ser usados para monitorar pacientes e fornecer atendimento personalizado, levando a melhores resultados de saúde.
    """)
        
    @bot.message_handler(func=lambda menssage: "/Opcao_3" in menssage.text)
    def opcao3 (mensagem):
        bot.reply_to(mensagem,"""Riscos de segurança: os dispositivos IoT podem ser vulneráveis a ataques cibernéticos, que podem comprometer dados pessoais, redes e até mesmo a segurança física.
Preocupações com a privacidade: os dispositivos IoT podem coletar muitos dados sobre os usuários, levando a preocupações com a privacidade se esses dados não forem protegidos ou gerenciados adequadamente.
Problemas de interoperabilidade: os dispositivos IoT podem não conseguir se comunicar entre si se usarem protocolos ou padrões diferentes, levando a problemas de interoperabilidade que podem limitar sua utilidade.
Complexidade: os sistemas de IoT podem ser complexos para projetar, implantar e gerenciar, exigindo habilidades e conhecimentos especializados.
Confiabilidade: os dispositivos IoT podem estar sujeitos a falhas de hardware ou software, levando a paralisações e interrupções.
Custo: os dispositivos IoT podem ser caros, especialmente para implantações em larga escala, o que pode limitar sua adoção em alguns contextos.
Considerações éticas: A adoção generalizada de dispositivos IoT levanta questões éticas sobre seu impacto na sociedade, como o potencial de deslocamento de empregos ou aumento da vigilância.
    """)
        
    @bot.message_handler(func=lambda menssage: "/Opcao_4" in menssage.text)
    def opcao4 (mensagem):
        bot.reply_to(mensagem,"""Casas inteligentes: dispositivos IoT, como termostatos inteligentes, sistemas de iluminação inteligentes e fechaduras inteligentes, podem ser usados para automatizar e controlar vários aspectos de uma casa, incluindo temperatura, iluminação, segurança e entretenimento.
Cuidados de saúde: dispositivos IoT, como wearables, dispositivos médicos inteligentes e sistemas de monitoramento remoto, podem ser usados para monitorar a saúde dos pacientes e fornecer atendimento personalizado, melhorando os resultados dos pacientes e reduzindo os custos de saúde.
Automação industrial: sensores e dispositivos IoT podem ser usados para monitorar e otimizar processos industriais, melhorando a eficiência, reduzindo o tempo de inatividade e aumentando a segurança.
Agricultura: os sensores de IoT podem ser usados para monitorar a umidade do solo, as condições climáticas e a saúde das culturas, permitindo a agricultura de precisão e otimizando os rendimentos.
Cidades inteligentes: os dispositivos IoT podem ser usados para monitorar e gerenciar vários aspectos da infraestrutura da cidade, incluindo tráfego, iluminação, gerenciamento de resíduos e segurança pública.
Varejo: os dispositivos IoT podem ser usados para fornecer experiências de compras personalizadas e otimizar o gerenciamento da cadeia de suprimentos, melhorando a satisfação do cliente e reduzindo custos.
Transporte: os sensores IoT podem ser usados para monitorar o tráfego e otimizar os sistemas de transporte, melhorando a segurança e reduzindo o congestionamento.
Gerenciamento de energia: dispositivos IoT podem ser usados para monitorar e otimizar o consumo de energia em edifícios e residências, reduzindo custos e melhorando a sustentabilidade
    """)
        
    @bot.message_handler(func=lambda menssage: "/Quem" in menssage.text)
    def option4 (mensagem):
        bot.reply_to(mensagem,"""Meus criadores são os estudantes:
Antonio 
João
Pedro
Yan
    """)


    @bot.message_handler(func=verificar)
    def responder(mensagem):
        nome=mensagem.chat.first_name
        bot.reply_to(mensagem,f"""Desculpe, {nome} não entendi, Escolha uma opção !
/Opcao_1 - O que é Internet das coisas(Iot)?
/Opcao_2 - Vantagens de utilizar disposições inteligente (Iot)
/Opcao_3 - Desvantagens de utilizar disposições inteligente (Iot)
/Opcao_4 - Exemplos práticos de Iot:
    """)
    return

 


def verificar (mensagem): 
   
   return True


    


#Loop infite
bot.polling()
