import time
from logica_bot import WhatsappBot
from webscraping import Webscraping

bot_wpp = WhatsappBot()
bot_scraping = Webscraping
check = 1 #Valor default 0
check_1 = 1 #Valor default 0
bot_wpp.enviar_texto_validacao()


while True:
    try:
        data_hora = datetime.datetime.now()
        horario_cliente = str(data_hora.strftime("%H"))
        minuto_cliente =int(data_hora.strftime("%M"))

        if((horario_cliente == "23") and (00 < minuto_cliente < 30) and (check_1 == 0)):
            print("Moveu arquivos")
            bot_wpp.verificador_relatorios() #Mover relatorios para pasta de backup
            check_1 = 0 #DEFALUT 1        

        if((horario_cliente == "23") and (30 < minuto_cliente <= 60)and (check_1 == 1) and (check == 1)):
            print("Reiniciando checks")
            #bot_wpp.enviar_texto_validacao() #DESCOMENTAR QUANDO COLOCAR PARA VALER
            check = 1 #DEFALUT 0
            check_1 = 1 #DEFALUT 0

        if (horario_cliente == "13" and check == 0):
            bot_scraping.dados_futuro_vencimento()    #Baixando relatorios
            bot_scraping.notificar_futuro_vencimento() #Notificacao para os clientes
            print("Notificacao para clientes que venceram em 3 dias")
            bot.dados_atrasados()
            bot.notificar_atrasados()
            print("Notificaçao para os clientes que o plano venceu hoje")
            check = 1
    except:
        pass

    try:
        bot_wpp.ultimas_notificacoes()
    except:
        time.sleep(5)

    
