import pywhatkit
import schedule
import time
import datetime

#https://github.com/Ankit404butfound/PyWhatKit/blob/master/pywhatkit/whats.py
#https://schedule.readthedocs.io/en/stable/examples.html

# Função para envio da mensagem
def enviar_mensagem():
    grupo_id = "IS5jUzVoIti5XUK3LWR91F"  
    mensagem = "Oi, este é um lembrete automático!"
    f = datetime.datetime.now() + datetime.timedelta(seconds=61)
        # Programar para 1 minuto à frente
    horas = f.hour
    minutos = f.minute   # Agenda para o próximo minuto    
    try:
        pywhatkit.sendwhatmsg_to_group(grupo_id, mensagem, horas, minutos)
        print(f"Mensagem enviada com sucesso às {horas}:{minutos}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Agendar envio diário às 
#schedule.every().day.at("20:45").do(enviar_mensagem)
#schedule.every(1).minutes.do(enviar_mensagem)
schedule.every(15).seconds.do(enviar_mensagem)


print("Automatizador de Mensagens Ativo. Pressione Ctrl+C para sair.")

# Loop infinito para manter o programa rodando
while True:
    schedule.run_pending()
    time.sleep(1)