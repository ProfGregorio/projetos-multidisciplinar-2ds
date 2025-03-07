import pywhatkit
import datetime

# Obter o horário atual e somar + 1minuto
f = datetime.datetime.now() + datetime.timedelta(seconds=61)

# Programar para 1 minuto à frente
horas = f.hour
minutos = f.minute   # Agenda para o próximo minuto

# Enviar mensagem
#pywhatkit.sendwhatmsg("+5515991564560", "Olá! Esta é uma mensagem de teste.", f.hour, f.minute)
print("Mensagem programada com sucesso!")

# # Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("IS5jUzVoIti5XUK3LWR91F", "Hey All!", f.hour, f.minute)

# # Send a WhatsApp Message to a Group instantly
#pywhatkit.sendwhatmsg_to_group_instantly("IS5jUzVoIti5XUK3LWR91F", "Hey All!")
  